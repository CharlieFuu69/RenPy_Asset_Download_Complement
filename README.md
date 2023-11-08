[license]: https://www.gnu.org/licenses/gpl-3.0
[renpy]: https://renpy.org/

[license-badge]: https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge&logo=creativecommons
[license-image]: https://www.gnu.org/graphics/gplv3-with-text-136x68.png
[renpy-shield]: https://img.shields.io/badge/Software-Ren'Py-red
[build-shield]: https://img.shields.io/badge/Build-Passing-green

<p align="center">
  <img width="176" height="200" src="https://user-images.githubusercontent.com/77955772/184478128-93046a80-f326-43c9-9960-efdcd61f03b6.png">
</p>

<h1 align = "center"> RADC - Ren'Py Asset Download Complement </h1>

[![license-badge]][license] [![RenPy][renpy-shield]][renpy] ![build-shield]

> ![ic_warning](https://user-images.githubusercontent.com/77955772/143798585-2a612721-a193-4ec0-af5f-811c6bef6c4c.png) **ADVERTENCIA:** En estos momentos, RADC está siendo reacondicionado debido a múltiples reportes de bugs, por lo que no se recomienda utilizar en juegos en fase de producción.
> El proceso de reacondicionado de RADC, implica los siguientes cambios:
> 
> - [x] Eliminar la dependencia de WGET para realizar las descargas.
> - [x] Realizar el proceso de descarga de manera nativa (esto es muy bueno).
> - [ ] Recompatibilización de RADC para que sea completamente Cross-Platform.
> - [x] Modificaciones a la interfaz de descargas por defecto.
> - [x] Agregar medidor de ancho de banda de descarga en tiempo real (kB/s o MB/s).
> - [ ] Eliminar soporte para Mediafire (Los nuevos filtros de Cloudflare dificultan el mantenimiento de esta característica).
> - [x] Agregar soporte de descargas de GitHub mediante GitHub API (Requerirá severas modificaciones a la documentación).
> - [x] Agregar contador de bloques descargados (ahora se podrán hacer descargas de lotes de archivos como una descarga única).

* **Versión Actual: `v1.3a` - [¡Descargar aquí!](https://github.com/CharlieFuu69/RenPy_Asset_Download_Complement/releases/tag/v1.3a)**

¡Hola! Te presento a RADC, un complemento de descargas In-Game que puedes integrar en juegos desarrollados con el motor "Ren'Py".

## ¿Para qué sirve RADC?

RADC es un complemento que le da la facilidad a tu juego para descargar contenido desde un servidor. Puedes utilizarlo para que tu juego descargue distintos tipos de archivos en el disco, y que el jugador (o el mismo juego) los pueda utilizar posterior a su descarga. Un ejemplo de implementación de RADC en tu juego, podría ser para descargar DLCs.

Este complemento se basa en el módulo `wget` (hecho en Python), que puedes encontrar [aquí en PyPI](https://pypi.org/project/wget/).

## ¿Qué tiene de bueno RADC?

RADC puede mostrar el progreso de descarga de forma visual en tu juego, mostrando una barra de progreso, señalando el tamaño descargado/tamaño total de la descarga (en Megabytes), y el porcentaje descargado en total (mira los Screenshots de abajo para que te hagas la idea).
Puede realizar la descarga de un archivo almacenado en un servidor, o si no tienes para costear un servidor, también posee compatibilidad para descargar archivos desde [Mediafire](https://www.mediafire.com/) y [Anonfiles](https://anonfiles.com/). ¡Simplemente proporciona la URL del archivo a descargar, y RADC se encargará del resto!

## ¿Y qué tal la compatibilidad entre sistemas operativos?

Este complemento ha sido probado exitósamente en Windows y Android. Por razones de actividad intensa de I/O, en versiones de Android puede haber "lag" durante la descarga de algún archivo, pero la descarga en sí no se ve afectada de ninguna manera.

---

## ¿Cómo añadir el complemento RADC a un proyecto de Ren'Py?:

- **Paso 1:** Descarga el archivo `RADC_v1.3a.zip` de este release, en tu computadora.
- **Paso 2:** Extrae las carpetas `radc` y `python-packages`, y coloca estas carpetas en el interior de la carpeta `game` de tu proyecto.
- **Paso 3:** ¡Empieza a usar RADC en tu proyecto! El archivo `script.rpy` contiene un ejemplo para que puedas ejecutar descargas.

![ic_warning](https://user-images.githubusercontent.com/77955772/143798585-2a612721-a193-4ec0-af5f-811c6bef6c4c.png) Recomiendo encarecidamente leer la [Documentación de RADC](DOCUMENTACION.md). Contiene instrucciones de uso con fragmentos de código incluido e información sobre las clases, métodos y screens que puedes usar de RADC.

¡Recuerda! Este complemento aún esta bajo pruebas, por lo que puede tener errores. Si encontraste un error de funcionamiento, reportalo en la sección <ins>**"Issues"**</ins> del repositorio o contáctame en [Telegram @CharlieFuu69](https://t.me/CharlieFuu69)

---

## Capturas de RADC en funcionamiento:

![screenshot0001](https://user-images.githubusercontent.com/77955772/143798053-b7cf4bcc-8c35-40a2-94ed-cd137c9b023c.png)
![screenshot0002](https://user-images.githubusercontent.com/77955772/143798067-5f6ec5b6-61fb-4dd7-8697-742d8232f736.png)
![screenshot0003](https://user-images.githubusercontent.com/77955772/143798085-8947be9c-1360-4a37-b8c9-73386af4c252.png)

---

## Licencia de este complemento :

[![license-image]][license]

Este complemento está protegido bajo la licencia **[GPL v3.0](https://www.gnu.org/licenses/gpl-3.0)**.

##### WGET:

_Public domain by anatoly techtonik <techtonik@gmail.com>
Also available under the terms of MIT license
Copyright (c) 2010-2015 anatoly techtonik_
