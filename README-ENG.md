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
  <a href="https://github.com/CharlieFuu69/RenPyHub-Plugin">
    <img src="https://github.com/user-attachments/assets/eb856e26-472d-4fa4-8eba-6d4691be6e95"/>
  </a>
</p>

<p align="center">
  <a href="https://github.com/CharlieFuu69/RenPyHub-Plugin/releases/latest">
    <img src="https://github.com/user-attachments/assets/d334dcc4-66d6-4904-801a-0e8293ef2788"/>
  </a>
  <a href="https://github.com/CharlieFuu69/RenPyHub-Plugin/wiki">
    <img src="https://github.com/user-attachments/assets/6ca0675a-b636-4172-a2b0-d4363d657599"/>
  </a>
</p>


Hello! Meet **Ren'PyHub!**, an in-game download plugin that you can integrate into games developed with the "Ren'Py" engine.

### 1. What is "Ren'PyHub"?

**Ren'PyHub** is an asset management plugin that allows your game to download remote assets and also deliver in-game updates using the GitHub infrastructure. A possible use case for this plugin is if your game is fairly large (>1 GB), and you plan to update it periodically. In this case (depending on how you have organized your RPA packages), if you make a minor change to your game code, the player won't have to redownload the entire game just to update a small snippet.

You can also enable the game to compare versions in case you update the game executable itself. For example, if your executable has version `v1.0`, and you have created a general update with a version `v1.1`, **Ren'PyHub** also has the ability to report that a new version of your game is available.

---

### 2. Ren'PyHub Features

The features of Ren'PyHub as an Asset Manager are as follows:

* **Hash-based update checking:**

  _**Ren'PyHub** checks if your game's resources have been updated on GitHub, leveraging the GitHub API and implementing SHA-256 hash-based resource checking._

* **Supports public and private repositories:**

  _Don't want to openly expose your game's RPA packages to the public? **Ren'PyHub** can work with private repositories without any problems!_

* **You can create a "maintenance phase":**

  _Have you seen some games set maintenance periods? If you wish, you can disable the game during maintenance periods._

* **Detailed Download Display:**
  _The data handlers that make up the plugin allow you to display detailed download information, such as:_

  - _Overall download progress (automatic `B/kB/MB/GB` conversion)_
  - _Total download percentage._
  - _Download speed (or rather, bandwidth in MB/s)._
  - _Count of blocks (RPA packets) downloaded._

* **Fail-safe downloads:**

  _WiFi disconnected? Did you move the Ethernet cable? No problem. If your downloads are interrupted, the download will resume at the exact byte where the interruption occurred once the internet connection is restored, without having to start the download process from scratch._

---

### 3. Cross-OS Compatibility.

This plugin has been tested on **Windows** and **Linux** distributions such as _"Linux Mint"_ and _"Ubuntu"_. Android compatibility will be worked in over time, as it is still possible to read RPA packages on mobile devices.

---

### 4. Do you want to test Ren'PyHub in a sample project?

> [!TIP]
> _Be sure to read the **[Ren'PyHub Documentation][documentation]** to get a better understanding of how this plugin works._

If you want to test Ren'PyHub without any commitments on your real projects, try cloning the repository into your Ren'Py project folder using:
```
git clone https://github.com/CharlieFuu69/RenPyHub-Plugin.git
```
Or, download the project ZIP file and manually unzip it into your Ren'Py project folder:

<img width="40%" height="40%" alt="image" src="https://github.com/user-attachments/assets/922b213f-30e3-47f6-ae8c-87fd73230cc5" />

---

### 5. Want to start using this plugin in your game?

Download the `RenPyHub-Plugin.zip` file from the **[Latest release][latest-release]** of this repository. To understand how this plugin works, start by reading the **[Ren'PyHub Documentation][documentation]**, which includes instructions, details of the classes/functions, and a deployment tutorial that will walk you through the entire process, from creating your repository to integrating Ren'PyHub into your game.

---

### 5. License

[![license-image]][license]

This plugin is distributed under the **[GPL v3.0][license]** license. If you use this plugin, please include a reference to this repository.
