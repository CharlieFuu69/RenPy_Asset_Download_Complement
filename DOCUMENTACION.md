<p align="center">
  <img width="176" height="200" src="https://user-images.githubusercontent.com/77955772/184478128-93046a80-f326-43c9-9960-efdcd61f03b6.png">
</p>

<h1 align = "center"> RADC - Ren'Py Asset Download Complement </h1>

## Documentación del complemento (Válido para la v1.3)

En este archivo Markdown encontrarás información detallada sobre los elementos que puedes usar de este sistema de descargas. Esto aplica bastante para los usuarios que quieran crear screens propias y omitir las plantillas que se incluyen en este complemento.
Esta Mini-documentación considera que posees conocimientos abundantes sobre el <ins>_Lenguaje de Pantallas de Ren’Py_</ins> y conocimientos fundamentales de Python, ya que son necesarios para poder utilizar el complemento y crear UI customizada.
La información estará distribuida en dos ítems generales:

- Uso de las Screens prefabricadas (plantilla).
- Uso de los métodos de las clases que conforman al complemento de descargas.

Se incluirán también ejemplos de uso para cada una de ellas para una mejor comprensión.

---

## 1. Uso de las Screens prefabricadas de RADC

Las screens prefabricadas se incluyen para facilitar los primeros pasos usando este complemento. En este ítem verás la estructura de esas screens, acompañadas de los ejemplos de cómo deben ser llamados.

------

#### 1.1. Screen `download(url, savepath = None)`:

Esta screen se encarga de ejecutar la descarga de un archivo, en caso de que se tenga la URL física del archivo en un servidor/host. Recibe dos parámetros posicionales:

- **`url` (String):** _Recibe como argumento una cadena con **la URL que apunta al archivo en el servidor**. Este parámetro es obligatorio para usar esta screen._
- **`savepath` (String):** _Si no es `None`, es una cadena con **la ruta donde quieres guardar el archivo** descargado, indicando también el nombre del archivo. Si solo señalas el nombre del archivo, este será descargado en la carpeta base de tu juego (o en la carpeta de Ren’Py si aún estás arrancando el juego con el Launcher de Ren’Py)._

**Ejemplo de descarga en la carpeta base de tu juego:**

```renpy
## Aquí empieza tu juego
label start:
    $ link = “https://www.ejemplo.com/nombre_del_archivo.zip”
    call screen download(url = link, savepath = “nombre_del_archivo.zip”)
    ## Esto descargará "nombre_del_archivo.zip" en la carpeta base
```

**Ejemplo de descarga en el interior de la carpeta “game” de tu juego:**

```renpy
## Aquí empieza tu juego
label start:
    $ link = “https://www.ejemplo.com/nombre_del_archivo.zip”
    $ path = searchpath() + “/nombre_del_archivo.zip”
    call screen DownloadNow(url = link, savepath = path)
    ## Esto descargará "nombre_del_archivo.zip" en la ruta “/game/nombre_del_archivo.zip” de tu juego
```

------

#### 1.2. Screen `mediafire_dl(shared_url, savepath = None)`:

Esta screen, a diferencia de `download()`, es para ejecutar descargas de archivos alojados en la nube de Mediafire. A su vez, utiliza a la screen `download()` para realizar la descarga una vez que haya encontrado la URL final de descarga de Mediafire.

> _**NOTA:** Esta screen también puede usarse para descargar archivos desde AnonFiles (Ver detalles en README.MD)._

- **`shared_url` (String):** _Recibe una cadena con **la URL compartida del archivo** alojado en Mediafire. La URL compartida es el que te entrega Mediafire para compartir tu archivo con el resto del mundo. Este parámetro es obligatorio._
- **`savepath` (String):** _Si no es `None`, al igual que en la screen `download()`, es una cadena con el nombre del archivo o la ruta de descarga del archivo._

**Ejemplo de descarga en la carpeta base de tu juego:**

```renpy
## Aquí empieza tu juego
label start:
    $ link = “https://www.mediafire.com/file/.../nombre_del_archivo.zip/file”
    call screen mediafire_dl(shared_url = link, savepath = “nombre_del_archivo.zip”)
    ## Esto descargará el ZIP en la carpeta base
```

**Ejemplo de descarga en el interior de la carpeta “game” de tu juego:**

```renpy
## Aquí empieza tu juego
label start:
    $ link = “https://www.mediafire.com/file/.../nombre_del_archivo.zip/file”
    $ path = searchpath() + “/nombre_del_archivo.zip”
    call screen mediafire_dl(shared_url = link, savepath = path)
    ## Esto descargará el ZIP en la ruta “/game/nombre_del_archivo.zip” de tu juego
```

---

## 2. Las Clases y Métodos de RADC para usar en una screen customizada

Este ítem está destinado a quienes deseen crear screens customizadas para descargar archivos en sus juegos. Por cierto, también puedes tener una referencia de cómo usarlos, observando el archivo [radc_screens.rpy (Código fuente)](https://github.com/CharlieFuu69/RenPy_Asset_Download_Complement/blob/59e9f1630a06daf9b2b933fcb1a5d159fef95f37/radc/radc_screens.rpy).
Ahora verás de forma detallada la utilidad de cada clase y sus métodos.

------

#### 2.1. Clase `DownloadHandler(url, savepath = None)`:

Esta clase es la encargada de ejecutar la descarga de un archivo desde una URL determinada. Hereda la clase `Thread` de la librería `threading` para ejecutar la descarga en un hilo aparte del que se ejecuta el juego.
Recibe los siguientes parámetros:

- **`url` (String):** _Recibe una cadena con la URL que apunta al archivo en un servidor._
- **`savepath` (String):** _Si no es `None`, es una cadena con la ruta de descarga incluyendo el nombre del archivo. Si no se pasa un argumento a este parámetro el archivo se descargará en la carpeta base del juego, o si aún estás desarrollando el juego se descargará en la carpeta base del SDK de Ren’Py._

Los métodos que pueden ser usados para tu juego, son los siguientes:

- `start()`: _Este método acciona el hilo de la descarga. Heredado de la librería `threading`._
- `status()`: _Este método comprueba si **el proceso de descarga ha finalizado**. Retorna True en caso de haber finalizado y False si aún se está llevando a cabo._
- `runtime_exception()`: _Este método comprueba si hubo una excepción durante el proceso de descarga. Si ocurrió un error, retorna `True`, de lo contrario retorna `False`._
- `gauge()`: _Este método retorna **el progreso de descarga en forma de porcentaje** (de 0 a 100%)._
- `sizelist()`: _Este método retorna una lista de dos elementos, donde el primer elemento señala los MB (Megabytes) descargados, y el segundo señala el tamaño total del archivo en MB. Puede servir si quieres mostrar el progreso de descarga en MB._

------

#### 2.2. Clase `SharedCloudGetFile(shared_url)`:

Esta clase de encarga de extraer la URL final de un archivo alojado en la nube de Mediafire, en base a la URL compartida de ese archivo. Al igual que `DownloadHandler()`, esta clase utiliza la librería `threading` para ejecutarse en un hilo distinto al que se ejecuta el resto del juego.
Recibe el siguiente parámetro:

- **`shared_url` (String):** _Recibe una cadena con la URL compartida del archivo alojado en Mediafire. Este parámetro es obligatorio para que la clase funcione correctamente._

Los métodos que pueden ser usados para tu juego, son los siguientes:

- `start()`: _Este método acciona el hilo para obtener la URL de descarga final. Heredado de la librería `threading`._
- `status()`: _Este método comprueba si el proceso de extracción de URL ha finalizado. Retorna `True` en caso de haber finalizado y `False` si aún se está llevando a cabo._
- `runtime_exception()`: _Este método comprueba si hubo una excepción durante el proceso de extracción. Si ocurrió un error, retorna `True`, de lo contrario retorna `False`._
- `end_url()`: _Este método retorna la URL final extraída respecto de la URL compartida de Mediafire._

------

#### 2.3. Función `searchpath()`:

Esta función integrada en RADC, puede ser útil si quieres descargar un archivo en un lugar donde Ren’Py pueda leerlo sin problemas.
En Windows, retorna la ruta física del sistema operativo hasta la carpeta `/game` de tu juego.
En Android, accede a la variable de entorno `ANDROID_PUBLIC`, retornando la ruta pública de la app (el juego), que por cierto, Ren’Py la usa como carpeta `/game` “virtual”, permitiendo operar archivos y leerlos en tu juego igual que como si estuviera en la carpeta `/game` real.
Normalmente en Android no existe la carpeta `/game`  en la ruta pública, por lo que si no existe, esta función la creará mientras es llamada en algún lugar del código de tu juego.

**Ejemplo de retorno en Windows:**

Si tu juego está en la carpeta “Documentos” de tu PC, debería retornar algo como:

```python
'C:\\Users\\[Tu usuario]\\Documents\\[Nombre de tu juego]/game'
```

**Ejemplo de retorno en Android:**

Si tu juego ha sido arrancado en Android, la función retornaría una ruta similar a esta:

```python
'/storage/emulated/0/Android/data/com.nombredelpaquete/files/game'
```
