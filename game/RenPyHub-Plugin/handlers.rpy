## CharlieFuu69
## Ren'PyHub Digital Asset Manager (DAM) Plugin

## Script: Manipuladores de datos.

## © 2025 CharlieFuu69 - GNU GPL v3.0

################################################################################

init python:
    import requests
    import os
    import json
    import hashlib
    import time

    ## ---------------------------------------------------------------------- ##
    ## FUNCIONES

    def sha256sum(fn, bufsize):
        """
        Esta función se encarga de obtener el Hash SHA-256 de un archivo en el
        disco.

        Posee 2 parámetros obligatorios:

        - fn (str):
            La ruta del archivo a digerir.

        - buf_size (int):
            Un entero que indica el tamaño máximo de cada fragmento de archivo a
            analizar. Idealmente debe ser un múltiplo de 8 (Ejemplo: 1024, 4096, etc.)


        Retorna:
            sha256sum() -> (tuple) (
                (str) Hash digerido al escanear el archivo.
                (float) Tiempo que tomó digerir el archivo, en segundos.
            )
        """

        rv = (None, 0.0)
        start = time.time()

        if os.path.exists(fn):
            h = hashlib.sha256()

            with open(fn, 'rb') as f:
                while True:
                    data = f.read(bufsize)

                    if not data:
                        break

                    h.update(data)

            rv = (h.hexdigest(), round(time.time() - start, 6))

        return rv


    def datasize(length):
        """
        Esta función convierte un valor de bytes en un formato de kB, MB o GB,
        según el valor especificado en `length`.

        Retorna una string formateada con la unidad de medida de datos respectiva.
        """

        length = float(length)

        for dlen, unit, prefmt in _LENGTH_CONST:
            if length >= dlen:
                return prefmt % (length/dlen, unit)
            elif length < 1024.0:
                return f"{length} B"
            else:
                continue


    def setup_headers():
        """
        Esta función se encarga de dar el formato definitivo a los Headers
        HTTP para cada tipo de petición a realizar por los manipuladores de
        datos.
        """

        rv = {
            "status" : {
                "Accept" : "application/vnd.github.raw+json"
            },

            "index" : {
                "Accept" : "application/vnd.github+json"
            },

            "download" : {
                "Accept" : "application/octet-stream"
            }
        }

        if FINE_GRAINED_TOKEN:
            for rtype, header in rv.items():
                if rtype != "download" and IS_PUBLIC_REPO:
                    continue

                header["Authorization"] = f"token {FINE_GRAINED_TOKEN}"
                rv[rtype] = header

        return rv


    ## ---------------------------------------------------------------------- ##
    ## CLASES (MANIPULADORES DE DATOS)

    class UpdateHandler():
        """
        Esta clase es un gestor completo para manipular las actualizaciones de
        paquetes en el juego, al utilizar GitHub como CDN para el juego.

        Parámetros opcionales al instanciar:

        - bufsize (int):
            Si quieres modificar el tamaño de búfer utilizado para el escaneo
            de paquetes, este debe ser un número entero indicando el tamaño en
            bytes, idealmente un múltiplo de 8.

            (Por defecto: 1048576 bytes)

        - http_timeout (int):
            Este valor corresponde al tiempo considerado para una petición, en
            segundos, antes de considerar un 'tiempo de respuesta agotado'.

            (Por defecto: 10)
        """

        def __init__(self, bufsize=1048576, http_timeout=10):

            ## ------------------------ CONFIGURACIÓN ----------------------- ##

            ## Argumentos opcionales
            self.bufsize = bufsize
            self.timeout = http_timeout

            ## ---------------------------- DATOS --------------------------- ##

            ## Información del servidor
            self.info = None

            ## Índice de assets formateado
            self.resources = list()
            self.downloads = list()
            self.local_scan = dict()

            self.download_size = 0

            ## --------------------------- STATUS --------------------------- ##

            ## Estado de la secuencia completa
            self.process_done = False
            self.exc_output = None
            self.exit = None


        def get_cdn_index(self):
            """
            Este método se encarga de obtener los datos de estado del servidor
            (archivo `game_status.json`), y el índice del release donde se almacenan
            los paquetes descargables (API GitHub).
            """

            print("Acquiring remote index...")

            queries = {"status" : _STATUS_ENDPOINT, "index" : _INDEX_ENDPOINT}

            responses = dict() ## Respuestas de GitHub (status y API)
            rv = dict()        ## Datos útiles recopilados
            fixed_idx = list() ## Índice formateado con los datos útiles
            cdn_size = 0       ## Tamaño total de recursos en GitHub


            ## --------------------- OBTENCIÓN DE DATOS --------------------- ##

            ## Peticiones HTTP requeridas para comprobar actualizaciones
            for rtype, endpoint in queries.items():
                print(f"[GET]: {endpoint}")
                r = requests.get(endpoint,
                    headers=_HEADERS[rtype],
                    timeout=self.timeout)

                ## ¿Es una respuesta satisfactoria?
                if r.ok:
                    responses[rtype] = r.json()
                else:
                    raise Exception(__("Respuesta no válida (HTTP %s)") % r.status_code)


            ## --------------------- AJUSTES DEL ÍNDICE --------------------- ##

            print("Fixing remote index...")

            status = responses["status"]["server"]
            resources = responses["index"]

            ## Recorre la lista de assets en la respuesta de la API
            for asset in resources["assets"]:
                fixed_idx.append({
                    "name" : asset["name"],
                    "url" : asset["url"],
                    "hash" : asset["digest"].split(":")[1],
                    "size" : asset["size"]
                })

                cdn_size += asset["size"]

            rv["online"] = status["online"]
            rv["match_ver"] = config.version == status["version"]
            rv["index"] = fixed_idx

            ## Información de juego
            self.info = status
            self.resources = fixed_idx

            print(f"Current CDN data size is: {datasize(cdn_size)}")

            return rv


        def get_block_diffs(self):
            """
            Este método busca las diferencias entre los hash de los paquetes
            escaneados durante la fase init, y los hash recibidos desde el
            servidor (GitHub). Si los hashes difieren entre sí, se asume que
            un determinado paquete o varios paquetes necesitan actualización.

            En el caso de no encontrar un paquete que el índice asume que debería
            existir en el juego, se agrega a la cola como un paquete más a
            descargar.
            """

            pending_list = list()
            pending_size = 0
            scantime = list()

            print("Scanning local asset blocks...")
            print(f"\n| {"PACKAGE": ^18} | {"SHA-256 (CDN)": ^64} | {"STATUS": ^10} | {"SCAN TIME": ^10} |")
            print(f"|{"-" * 113}|")

            ## Recorre la lista de paquetes preparada
            for asset in self.resources:
                path = os.path.join(config.gamedir, asset["name"])  ## Ruta local donde debería estar el paquete
                h_out, took = sha256sum(path, bufsize=self.bufsize) ## Escaneo de archivos (h_out es `None` si el archivo no existe)
                hash_match = h_out == asset["hash"]                 ## Match del hash local y el hash del servidor.

                ## Comparación de hashes o detección de paquetes existentes
                if hash_match:
                    result = ("READY", "#AAFFAA")

                else:
                    pending_list.append(asset)
                    pending_size += asset["size"]

                    if h_out:
                        result = ("CHANGED", "#FFFFAA")
                        os.remove(path)
                    else:
                        result = ("PENDING", "#FF9999")

                self.local_scan[asset["name"]] = h_out
                scantime.append(took)

                print(f"| {asset["name"] : ^18} | {asset["hash"]: ^32} | {result[0]: ^10} | {took: ^10} |")


            ## Lista los archivos que deben ser actualizados/descargados
            self.downloads = pending_list
            self.download_size = sum([i["size"] for i in pending_list])

            ## Tiempo total usado en el procedimiento de hashing (escaneo)
            total_time = round(sum(scantime), 2)

            ## Media de tiempo usado para escanear los archivos
            avg_time = round(total_time / len(scantime), 2)

            ## Actualización de pop-up en la UI
            if len(pending_list) > 0:
                print(f"Expected download size: {datasize(self.download_size)}")

            print(f"Asset scanning process took: {total_time} sec (Avg: {avg_time} sec/block)")
            print("Scanning procedure ended.")


        def start(self):
            """
            Este método ejecuta todo el flujo correspondiente a la búsqueda
            de actualizaciones. Es necesario ejecutar dentro de un hilo mediante
            `threading.Thread()`, o bien, `renpy.invoke_in_thread()`.
            """

            ## Reinicio de los banderines de estado
            self.process_done = False
            self.exc_output = None
            self.exit = None

            try:
                data = self.get_cdn_index()

                ## ¿Fase de mantenimiento del juego?
                if not data["online"]:
                    self.exit = "offline"
                    print("Server under maintenance.")

                ## ¿La versión del cliente difiere de la versión en el servidor?
                elif not data["match_ver"]:
                    self.exit = "update"
                    print("Client update required.")

                else:
                    self.get_block_diffs()

                    if self.download_size > 0:
                        self.exit = "download"
                        print("Resource download needed.")

            except requests.exceptions.ConnectionError as network_err:
                self.exc_output = __("Error de conexión. Comprueba tu conexión a internet e intenta nuevamente.")
                print("ERROR: %s" %repr(network_err))

            except Exception as unknown_err:
                self.exc_output = str(unknown_err).replace("[", "[[")
                print("ERROR: %s" %repr(unknown_err))

            finally:
                time.sleep(2)
                self.process_done = True
                renpy.restart_interaction()


    class DownloadHandler():
        """
        Esta clase se encarga de gestionar el procedimiento de descarga de datos
        del juego. Utiliza los datos recopilados por la clase `UpdateHandler()`
        para descargar una cola de paquetes, y la lógica de descarga es a prueba
        de interrupciones. Toda descarga interrumpida de un paquete por fallos
        de conexión u otros, se reanudará desde el byte en el que ocurrió la
        falla.

        El constructor de la clase posee 1 parámetro obligatorio:

        - packages (list):
            Una lista de diccionarios que contienen la información de los paquetes
            a descargar. Cada diccionario contiene los siguientes datos:

            {
                "name": (str) Nombre del archivo,
                "url": (str) URL del archivo,
                "hash": (str) Hash MD5 del archivo,
                "size": (int) Tamaño del archivo en bytes
            }


        De manera opcional, el constructor posee los siguientes parámetros:

        - rootdir (str):
            Una cadena con la ruta donde los archivos descargados deben ser
            guardados en el disco.

            (Por defecto: config.gamedir)

        - buffer_size (int):
            Un número entero que representa el tamaño del búfer de descarga de
            datos, en Bytes.
            Idealmente, se recomienda un tamaño de búfer que sea un múltiplo de
            8.

            (Por defecto: 1024 bytes)

        - http_timeout (int):
            Un entero que representa la cantidad de segundos que se requiere para
            asumir que la conexión ha ocurrido "fuera de tiempo".

            (Por defecto: 10)
        """

        def __init__(self, packages, **kwargs):

            ## ------------------------ CONFIGURACIÓN ----------------------- ##

            self.packages = packages

            self.rootdir = kwargs.get("rootdir", config.gamedir)
            self.bufsize = kwargs.get("bufsize", 1024)
            self.timeout = kwargs.get("http_timeout", 10)

            self.headers = _HEADERS["download"]


            ## ---------------------------- DATOS --------------------------- ##

            ## Contador de bloques descargados
            self.block = [1, len(packages)]

            ## Contador de bytes generales de la descarga
            self.received = 0
            self.total = sum([i["size"] for i in packages])

            ## Contador de bytes para cada paquete
            self.pkg_received = 0
            self.pkg_total = 0

            ## Contadores para obtener la velocidad de descarga
            self.byte_stamp = 0
            self.clock = 0
            self.bytes_sec = 0


            ## --------------------------- STATUS --------------------------- ##

            self.process_done = False
            self.exc_output = None

            self.setup()


        def setup(self):
            """
            Este método ejecuta la limpieza de archivos temporales de descargas
            que fallaron en una sesión anterior de juego.

            La limpieza ocurre justo antes de iniciar la descarga actual.
            """

            print("Cleaning temp files...")

            for file in os.listdir(self.rootdir):
                if file.endswith(".tmp"):
                    os.remove(os.path.join(self.rootdir, file))


        def get_speed(self):
            """
            Este método se encarga de contar el tráfico de bytes para determinar
            la velocidad de la descarga en Bytes por segundo. El formateador
            de datos en pantalla se encarga de transformar los Bytes por segundo
            en una unidad de medida más grande (kilo, Mega, Giga).
            """

            if self.clock == 0.0:
                self.clock = time.time()
                self.byte_stamp = self.received

            if time.time() - self.clock >= 1.0:
                self.bytes_sec = self.received - self.byte_stamp
                self.clock = 0.0


        def fmt_callback(self):
            """
            Este método crea el formato del progreso de descarga para mostrar en
            la UI de juego, el cual debe ser llamado constantemente.
            """

            self.get_speed()

            mb_current = datasize(self.received)
            mb_total = datasize(self.total)
            mb_sec = datasize(self.bytes_sec)
            b_current, b_total = self.block
            pct = 0.0

            if self.total > 0:
                pct = round(100.0 * (self.received/self.total), 2)

            return f"{mb_current} / {mb_total}  {mb_sec}/s  ({b_current}/{b_total})  {pct:.02f}%"


        def start(self):
            """
            Este método se encarga de gestionar la descarga, escritura, reanudar
            descargas, e informar el progreso de descarga, incluyendo la velocidad
            de esta.
            """

            static_queue = tuple(self.packages)

            self.process_done = False
            self.exc_output = None

            if self.pkg_received > 0:
                print("Restarting interrupted download...")
            else:
                print("Starting batch download...")


            print("| PACKAGE            | SIZE          | BYTE OFFSET   |")
            print("+--------------------+---------------+---------------+")

            try:
                ## Iteración de la cola de descargas
                for data in static_queue:

                    ## Nombres de archivo
                    temp_fn = data["name"].split(".")[0] + ".tmp"
                    temp_file = os.path.join(self.rootdir, temp_fn)
                    end_file = os.path.join(self.rootdir, data["name"])

                    print(f"| {data['name']: ^18} | {data['size']: ^13} | {self.pkg_received: ^13} |")

                    ## Obtención de tamaño de paquete y ajuste de headers HTTP
                    self.pkg_total = data["size"]
                    self.headers["Range"] = f"bytes={self.pkg_received}-"

                    ## Petición de transmisión
                    r = requests.get(
                            data["url"],
                            headers=self.headers,
                            allow_redirects=True,
                            stream=True,
                            timeout=self.timeout
                        )

                    r.raise_for_status()

                    if r.ok:
                        with open(temp_file, "ab") as f:
                            ## Iteración de fragmentos de datos
                            for chunk in r.iter_content(self.bufsize):
                                d_size = len(chunk)
                                self.received += d_size
                                self.pkg_received += d_size

                                if chunk:
                                    f.write(chunk)

                        ## Elimina el archivo antíguo (si existe)
                        if os.path.exists(end_file):
                            os.remove(end_file)

                        os.rename(temp_file, end_file)

                        ## Elimina el primer paquete de la cola de descargas, y
                        ## reinicia contadores.
                        self.packages.pop(0)
                        self.pkg_received = 0
                        self.block[0] += 1

                    else:
                        raise Exception(__("Respuesta no válida (HTTP %s)") % r.status_code)

                print("All blocks are downloaded successfully.")

            except requests.exceptions.ConnectionError as network_err:
                self.exc_output = __("Error de conexión. Comprueba tu conexión a internet e intenta nuevamente.")
                print("ERROR: %s" %repr(network_err))

            except Exception as unknown_err:
                self.exc_output = str(unknown_err).replace("[", "[[")
                print("ERROR: %s" %repr(unknown_err))

            finally:
                self.process_done = True
                renpy.restart_interaction()


    ## ---------------------------------------------------------------------- ##
    ## CONSTANTES DE USO INTERNO

    _LENGTH_CONST = [
        (1024.0 ** 3, "GB", "%.02f %s"),
        (1024.0 ** 2, "MB", "%.02f %s"),
        (1024.0, "kB", "%d %s")
    ]

    _HEADERS = setup_headers()
    _STATUS_ENDPOINT = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/game_status.json"
    _INDEX_ENDPOINT = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/releases/tags/{RELEASE_TAG}"
