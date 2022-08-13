[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[renpy]: https://renpy.org/

[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/Licencia-CC--BY--SA%204.0-brightgreen
[renpy-shield]: https://img.shields.io/badge/Software-Ren'Py-red

# RADC - Ren'Py Asset Download Complement

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa] [![RenPy][renpy-shield]][renpy]

¡Hola! Te presento a RADC, un complemento de descargas In-Game que puedes integrar en juegos desarrollados con el motor "Ren'Py".

## ¿Para qué sirve RADC?
RADC es un complemento que le da la facilidad a tu juego para descargar contenido desde un servidor. Puedes utilizarlo para que tu juego descargue distintos tipos de archivos en el disco, y que el jugador (o el mismo juego) los pueda utilizar posterior a su descarga. Un ejemplo de implementación de RADC en tu juego, podría ser para descargar DLCs.

Este complemento se basa en el módulo `wget` (hecho en Python), que puedes encontrar [aquí en PyPI](https://pypi.org/project/wget/).

## ¿Qué tiene de bueno RADC?
RADC puede mostrar el progreso de descarga de forma visual en tu juego, mostrando una barra de progreso, señalando el tamaño descargado/tamaño total de la descarga (en Megabytes), y el porcentaje descargado en total (mira los Screenshots de abajo para que te hagas la idea).
Puede realizar la descarga de un archivo almacenado en un servidor, y también posee compatibilidad para descargar archivos desde Mediafire en caso de que no dispongas de un servidor de paga. Simplemente proporciona la URL del archivo a descargar, ¡RADC se encargará del resto!

## ¿Y qué tal la compatibilidad entre sistemas operativos?
Este complemento ha sido probado exitósamente en Windows y Android. Por razones de actividad intensa de I/O, en versiones de Android puede haber "lag" durante la descarga de algún archivo, pero la descarga en sí no se ve afectada de ninguna manera.

---

## ¿Cómo añadir el complemento RADC a un proyecto de Ren'Py?:

- **Paso 1:** Descarga el archivo `RADC_v1.1a.zip` de este release, en tu computadora.
- **Paso 2:** Extrae las carpetas `radc` y `python-packages`, y coloca estas carpetas en el interior de la carpeta `game` de tu proyecto.
- **Paso 3:** ¡Empieza a usar RADC en tu proyecto! El archivo `script.rpy` contiene un ejemplo para que puedas ejecutar descargas.

![ic_warning](https://user-images.githubusercontent.com/77955772/143798585-2a612721-a193-4ec0-af5f-811c6bef6c4c.png) Recomiendo encarecidamente leer el archivo `Documentacion_RADC.pdf` incluido en el paquete ZIP de este release. Contiene instrucciones de uso con fragmentos de código incluido e información sobre las clases, métodos y screens que puedes usar de RADC.

¡Recuerda! Esta versión es un pre-lanzamiento por lo que puede tener errores. Si tienes dudas sobre cómo usar RADC, puedes contactarme en [Telegram @CharlieFuu69](https://t.me/CharlieFuu69)

---
## Capturas de RADC en funcionamiento:

![screenshot0001](https://user-images.githubusercontent.com/77955772/143798053-b7cf4bcc-8c35-40a2-94ed-cd137c9b023c.png)
![screenshot0002](https://user-images.githubusercontent.com/77955772/143798067-5f6ec5b6-61fb-4dd7-8697-742d8232f736.png)
![screenshot0003](https://user-images.githubusercontent.com/77955772/143798085-8947be9c-1360-4a37-b8c9-73386af4c252.png)

---

## Licencia de este complemento :

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa] [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Este complemento está protegido con la licencia del repositorio ["Codigos_RenPy"](https://github.com/CharlieFuu69/Codigos_RenPy), es decir, la licencia [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa]. Tienes permiso de modificar el complemento y compartirlo, con la única condición de que me atribuyas el contenido original :3

##### WGET:
_Public domain by anatoly techtonik <techtonik@gmail.com>
Also available under the terms of MIT license
Copyright (c) 2010-2015 anatoly techtonik_
