<!-- Links de utilidad pública --->
[license]: https://www.gnu.org/licenses/gpl-3.0
[renpy]: https://renpy.org/
[latest-release]: https://github.com/CharlieFuu69/RenPyHub-Plugin/releases/latest
[documentation]: https://github.com/CharlieFuu69/RenPyHub-Plugin/wiki

<!-- Badges del README --->
[renpy-badge]: https://img.shields.io/badge/Ren'Py-v8.4.1-red?style=for-the-badge&logo=python
[license-badge]: https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge&logo=creativecommons
[license-image]: https://www.gnu.org/graphics/gplv3-with-text-136x68.png
[status-badge]: https://img.shields.io/badge/Version%20Status-Stable-CCFF00?style=for-the-badge

<p align="center">
  <img width="100%" height="100%" alt="renpyhub-banner" src="https://github.com/user-attachments/assets/c69c9d56-8cf5-4e39-bc3f-170b5f116c94" />
</p>

[![license-badge]][license] [![renpy-badge]][renpy] ![status-badge]

<p align="center">
  <a href="https://github.com/CharlieFuu69/RenPyHub-Plugin/blob/master/README-ENG.md">
    <img src="https://github.com/user-attachments/assets/821b26ef-16a7-468f-ad1f-2c6d7bfeb72a"/>
  </a>
  <a href="https://github.com/CharlieFuu69/RenPyHub-Plugin/releases/latest">
    <img src="https://github.com/user-attachments/assets/f4180695-4835-4a32-ad89-839288cb7066"/>
  </a>
  <a href="https://github.com/CharlieFuu69/RenPyHub-Plugin/wiki">
    <img src="https://github.com/user-attachments/assets/8fd7b71e-f52a-4037-b3b1-8e0adb7cb064"/>
  </a>
</p>

¡Hola! Te presento a **Ren'PyHub!**, un plugin de descargas In-Game que puedes integrar en juegos desarrollados con el motor "Ren'Py".

### 1. ¿Qué es "Ren'PyHub"?

**Ren'PyHub** es un complemento de gestión de Assets que le permite a tu juego descargar recursos remotos, y también entregar actualizaciones In-Game usando la infraestructura de GitHub. Un caso de uso posible para este plugin, es que tu juego sea bastante grande (>1 GB), y pretendes actualizarlo cada cierto tiempo. En este caso (según como tengas organizados tus paquetes RPA), si realizas un cambio menor en el código de tu juego, no será necesario que el jugador tenga que redescargar todo el juego solo para actualizar un pequeño fragmento de este.

También puedes hacer que el juego pueda comparar versiones en caso de actualizar el ejecutable de tu juego en sí. Por ejemplo, si tu ejecutable tiene la versión `v1.0`, y has creado una actualización general con una versión `v1.1`, **Ren'PyHub** tiene también la capacidad de reportar que hay una nueva versión disponible de tu juego.

https://github.com/user-attachments/assets/808783df-b032-40b5-ad25-2f353dbcaecd

---

### 2. Características de Ren'PyHub.

A grandes rasgos **Ren'PyHub** es un sistema de gestión de recursos, y sus características son las siguientes:

* **Comprobación de actualizaciones basada en Hash:**

  _**Ren'PyHub** comprueba si los recursos de tu juego han sido actualizados en GitHub, apoyándose de la API de GitHub e implementando la comprobación de recursos basado en Hash SHA-256._

* **Compatible con repositorios públicos y privados:**

  _¿No quieres exponer abiertamente los paquetes RPA de tu juego al público? ¡**Ren'PyHub** puede trabajar con repositorios privados sin problemas!_

* **Puedes crear una "fase de mantenimiento":**

  _¿Has visto que algunos juegos establecen periodos de mantenimiento? Si lo deseas, puedes hacer que el juego no opere durante periodos de mantenimiento._

* **Visualización de descargas detallada en pantalla:**

  _Los manipuladores de datos que componen al plugin te permiten mostrar la información de descarga de manera detallada, tales como:_

  - _Progreso de descarga general (conversión `B/kB/MB/GB` automática)_
  - _Porcentaje total de descarga._
  - _Velocidad de descarga (o mejor dicho, ancho de banda en MB/s)._
  - _Conteo de bloques (paquetes RPA) descargados._

* **Descargas a prueba de errores:**

  _¿Se desconectó el WiFi? ¿Pasaste a mover el cable de Ethernet? No hay problema. Si las descargas se interrumpen, la descarga se reanudará en el byte exacto donde ocurrió la interrupción una vez que se restablezca la conexión a internet, sin la necesidad de empezar el proceso de descarga desde cero._

---

### 3. Compatibilidad entre sistemas operativos.

| Entorno     | Compatibilidad  |
| ----------- | --------------- | 
| Windows     | ✅ (Confirmada) |
| Linux dists | ✅ (Confirmada) |
| Android     | 📌 (Pendiente)  |

De manera efectiva, este plugin ha sido probado en Windows y en distribuciones de Linux como _"Linux Mint"_ y _"Ubuntu"_. La compatibilidad con Android se estará trabajando con el paso del tiempo, ya que igual es posible leer paquetes RPA en móviles.

---

### 4. ¿Quieres probar el funcionamiento de Ren'PyHub en un proyecto de prueba?

> [!TIP]
> _Asegúrate de leer la **[Documentación de Ren'PyHub][documentation]** para tener un mejor entendimiento del funcionamiento de este plugin._

Si quieres probar el funcionamiento de Ren'PyHub sin compromisos en tus proyectos reales, prueba clonando el repositorio en tu carpeta de proyectos de Ren'Py usando:
```
git clone https://github.com/CharlieFuu69/RenPyHub-Plugin.git
```
O bien, descarga el archivo ZIP del proyecto y descomprímelo manualmente en tu carpeta de proyectos de Ren'Py:

<img width="40%" height="40%" alt="image" src="https://github.com/user-attachments/assets/308ab1d1-4dfc-4a14-8534-28123c6cbcf9" />

---

### 5. ¿Quieres comenzar a utilizar este complemento en tu juego?

Descarga el archivo `RenPyHub-Plugin.zip` desde el **[Release más reciente][latest-release]** de este repositorio. Para entender cómo funciona este complemento, comienza leyendo la **[Documentación de Ren'PyHub][documentation]**, en el que se incluyen indicaciones, detalles de las clases/funciones, y un tutorial de implementación que te explicará todo el proceso, desde crear tu repositorio hasta integrar Ren'PyHub en tu juego.

---

### 6. Licencia de uso.

[![license-image]][license]

Este plugin se distribuye bajo la licencia **[GPL v3.0][license]**. Si utilizas este plugin, por favor, incluye una referencia a este repositorio.


