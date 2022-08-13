## ElectroBasicsYT - CharlieFuu69
## RADC - Ren'Py Asset Download Complement

## COMPATIBILIDAD DE PLATAFORMAS:
##       Windows: [Funciona]
##       Android: [Funciona]
##       Linux: [Aún no comprobado]

# ----------------------------------------------------------------------------------------------------------------- #

init python:
    ## Módulos necesarios
    import os, wget, threading, ssl, re, requests

    def searchpath():
        """Retorna la ruta donde Ren'Py pretende leer los Assets del juego. Útil si quieres
        descargar un archivo que posteriormente sea leído por el juego.

        En el caso de Android, la carpeta /game en la ruta pública no está creada. En ese caso,
        os.mkdir() se encargará de crear la carpeta si no existe."""

        path = (config.gamedir if renpy.windows else os.environ["ANDROID_PUBLIC"] + "/game")

        if not os.path.exists(path):
            os.mkdir(path)

        return path

    # --------------------------------------------------------------------------------------------------------------- #
    ## Obtención de URL de descarga (Mediafire)

    class MediafireGetFile(threading.Thread):
        """Esta clase se encarga de obtener la URL final de un archivo almacenado en
        Mediafire."""

        def __init__(self, shared_url):
            """Inicializa y construye los atributos de la clase."""

            super(MediafireGetFile, self).__init__()
            self.daemon = True ## Ejecuta el hilo como un daemon

            self.shared_url = shared_url ## La URL compartida

            self.fetch_finish = False ## Bandera de recuperación terminada
            self.url_end = [] ## La URL definitiva extraida
            self.fetch_exception = None ## Bandera de excepciones

        def status(self):
            """Retorna bool si la recuperación ha terminado o no."""
            return self.fetch_finish

        def end_url(self):
            """Retorna la URL final de descarga."""
            return self.url_end

        def runtime_exception(self):
            """Retorna True si hubo una excepción o no, durante la recuperación."""
            if isinstance(self.fetch_exception, Exception):
                return True
            return False

        def run(self):
            """Realiza el raspado de la URL compartida."""

            ## Encabezados para pasar en solicitud GET
            headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

            try:
                ssl._create_default_https_context = ssl._create_unverified_context

                for k in self.shared_url:
                    r = requests.get(k, headers = headers)
                    url = re.findall('"((http|ftp)s?://.*?)"', r.text)

                    ## Recorre las URLs encontradas en busca de la URL final
                    ## Las URL finales de Mediafire empiezan siempre con "https://download"
                    for i in url:
                        if i[0].startswith("https://download"):
                            self.url_end.append(i[0])
                        else:
                            pass

            except Exception as fetcherr:
                self.fetch_exception = fetcherr

            finally:
                self.fetch_finish = True
                renpy.restart_interaction()

    # --------------------------------------------------------------------------------------------------------------- #
    ## Manipulador de descargas principal

    class DownloadHandler(threading.Thread):
        """Esta clase se encarga de ejecutar y hacer el seguimiento de una descarga solicitada."""

        def __init__(self, url, savepath = None):
            """Constructor de la clase. Recibe los siguientes argumentos:

                url (Obligatorio):
                    La URL del archivo que quieres descargar. Debe ser un archivo físico, no una
                    prevista web.

                savepath:
                    Si no es None, es una cadena con la ruta física del dispositivo donde se guardará
                    el archivo."""

            super(DownloadHandler, self).__init__()
            self.daemon = True

            self.endpoint_url = url
            self.dl_path = savepath

            self.dl_current = 0.0
            self.dl_total = 0.0
            self.dl_percent = 0.0

            self.dl_status = False
            self.exception_output = None

        @property
        def gauge(self):
            """Retorna el porcentaje descargado para ser interpretado por una barra de progreso."""
            return (self.dl_percent or 0.0)

        @property
        def sizelist(self):
            """Retorna una lista con los MB descargados y los MB totales del archivo a descargar."""
            return [self.dl_current, self.dl_total]

        def status(self):
            """Retorna True si la descarga ha finalizado, de lo contrario, retorna False."""
            return self.dl_status

        def runtime_exception(self):
            """Retorna True si se presenta un error en la descarga."""

            if isinstance(self.exception_output, Exception):
                return True
            return False

        def progress_handler(self, current, total, *args, **kwargs):
            """Calcula el progreso de la descarga."""
            current, total = map(float, (current, total))
            if total > .0:
                self.dl_percent = (current / total)
                self.dl_current = round((current / 1048576), 2)
                self.dl_total = round((total / 1048576), 2)
                renpy.restart_interaction()

        def run(self):
            """Inicia la descarga en un contexto SSL no verificado para evitar errores de descarga
            por conflictos con los certificados de seguridad."""

            ssl._create_default_https_context = ssl._create_unverified_context

            try:
                wget.download(self.endpoint_url, self.dl_path, bar = self.progress_handler)
            except Exception as ex:
                self.exception_output = ex
                self.dl_percent = 0.0
            finally:
                self.dl_status = True
                renpy.restart_interaction()
