Development environment
=======================

Various code repositories and third-party software packages are required to update the firmware on CHIL instruments and dataloggers, as well as receive and decode the packets that they transmit. 

This page describes instructions for setting up a development environment on a Windows PC so that you can:

* reprogram CHIL instruments with new measurement settings
* update firmware on CHIL dataloggers to the latest version
* decode and interpret packets from CHIL instruments and dataloggers

.. important::

  Follow the instructions carefully, **do not use** default options for all the installation steps!

Installation steps
------------------
The installation instructions below were tested on 2026-05-21 using a Windows laptop without a internet connection. If you find any issues with the instructions below, let us know by `sending an email <mailto:hawkinsj22@cardiff.ac.uk>`__.

The latest files for the development environment are stored in a ZIP archive (``childev.zip``).

**Archive folder structure:**

* ``firmware/`` instrument and datalogger firmware.
* ``installers/`` third-party software installers.
* ``software/`` CHIL developed software and Python libraries.
* ``vscode_extensions/`` useful extensions for Visual Studio Code.

Download installation files
^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you have an offline version of the  ``childev.zip`` archive (``childev-offline.zip``), this should already contain the necessary files to setup the environment. For licensing reasons, we cannot host the full archive online because of the use of third-party software. 

.. important::
  
  Before starting the installation process, download third-party software installers :ref:`listed below <third-party-software>` and copy them to the `installers` directory in your `childev` folder. 

  Key installers to ensure you have downloaded are **VS Code**, **STM32CubeIDE** and **Python 3.14**.

We recommend keeping local copies of the offline installers on your machine, a hard drive or USB flash drive in case you need to reset your development environment while in the field.

Install VS Code
^^^^^^^^^^^^^^^
1. Located in `childev/installers`, run `VSCodeUserSetup-x64-1.121.0.exe`.
2. Select "I accept the agreement" on the following splash screen and install the software to the default location.
3. Ensure that "Add to PATH" is selected and optionally select to create a desktop icon.

Install PlatformIO
^^^^^^^^^^^^^^^^^^
1. Open VS Code and open the "Extensions" menu (`View > Extensions` from the top menu bar).
2. Select the `Install from VSIX` option from the three dots (`...`) menu at the top of the extensions screen. Navgiate to the `childev/vscode_extensions` folder and install the following extensions

    * VS Code cpptools: `ms-vscode.cpptools-1.32.2-win32-x64.vsix`
    * VS Code cpptools extension: `ms-vscode.cpptools-extension-pack-1.5.1.vsix`
    * VS Code cpp-devtools: `ms-vscode.cpp-devtools-0.5.13.vsix`
    * VS Code cmake-tools: `ms-vscode.cmake-tools-1.23.52.vsix`
    * PlatformIO: `platformio.platformio-ide-3.3.4-win32-x64.vsix`

3. Extract the contents of `.platformio.zip` folder from `childev/installers` to `C:/Users/[username]/.platformio` - make sure you don't end up with a nested folder (i.e. `.platformio/.platformio/...`). This is a large ZIP archive so might take some time!
4. Restart your PC.

Install datalogger firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^
I recommend setting up a folder for GitHub repositories (either `C:/repos` or `C:/Users/{username}/repos`). From here on, the 'repos' folder refers to whichever of these two options you've used!

For CHIL repositories, I recommend storing these in a folder named `chil` within your `repos` folder.

1. Extract the datalogger firmware `childev/firmware/datalogger-2023-main.zip` to `repos/chil/datalogger-2023` (**Note:** `-main` has been dropped from the end of the new folder). Again, double check that you haven't nested any folders.
2. Extract the `chillib-v20260521` library to `repos/chil/chillib`, removing the trailing `-v20260521` from the folder name.
3. Open VS Code and open the `repos/chil/datalogger-2023` folder. If prompted to trust the authors of the repository, confirm that you trust us!
4. Press `CTRL+SHIFT+P`, type in `PlatformIO: Build` to the text box at the top of the screen and press enter. This will compile the Datalogger firmware. An output terminal should appear at the bottom of the screen and show a `[SUCCESS]` message - this might take a while the first time you run the build command.
5. If you have a datalogger board (or just the Arduino Feather M0) to hand, plug it into the USB connection of the laptop, press `CTRL+SHIFT+P` and type `PlatformIO: Upload`. Press enter and the firmware should be uploaded to the datalogger.

Install STM32CubeIDE
^^^^^^^^^^^^^^^^^^^^
You will need to use STM32CubeIDE to program CHIL instruments which use the STM32L4 series of microcontrollers - this includes Cryoeggs, Cryowurst, Cryobeans, SmartSnowStake, etc.

1. Unzip the installer located with `st-stm32cubeide_2.1.1_28236_20260312_0043_x86_64.exe.zip` to a location of your choice.
2. Run the installer file (`st-stm32cubeide_2.1.1_28236_20260312_0043_x86_64.exe`).
3. If prompted to install any drivers (i.e. for ST-LINK) then do so.
4. Launch the STM32CubeIDE software. When prompted to select a directory as a workspace update the filepath to `C:/Users/sgljh3/STM32CubeIDE/chil` and select `Launch`.

When STM32CubeIDE has loaded, you're ready to setup the development environment for a CHIL instrument.

Setup STM32CubeIDE environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Within the `chil` workspace you have just created in STM32CubeIDE (see previous step!), we can import the firmware libraries for CHIL instrumentation.

Add `chillib` library
"""""""""""""""""""""
1. Select File > Import.... A dialog box will open. Choose the option General > Existing Projects into Workspace and press `Next >`.
2. Browse for the `chillib` folder in `repos/chil/chillib` and select it as the root directory. If succesful, you should see a project named 'chillib' in the Projects window. Press `Finish`.

Add `cryoegg-2025` library
""""""""""""""""""""""""""
1. Extract `childev/firmware/cryoegg-2025-v20260521` to `repos/chil/cryoegg-2025`. Ensure that there are no nested folders and that you've removed the trailing `-v20260521` from the folder name. 
2. Select File > Import... and the option General > Existing Projects into Workspace then press `Next >`.
3. Set the root directory as `repos/chil/cryoegg-2025/firmware/cryoegg-2025`.
4. If the `cryoegg-2025` project shows up in the Projects folder, press `Finish`.

You should now be able to build and debug the Cryoegg.

Install Python 3.14
^^^^^^^^^^^^^^^^^^^
Run the installer `python-3.14.5-amd64.exe` located in `childev/installers/`.

1. Select **Customize installation** and "Add python.exe to PATH" before proceeding.
2. On the Optional Features menu, ensure all options are selected except for "for all users".
3. On the Advanced Options menu:

   * Install Python 3.14 for all users [✓]
   * Associated files with Python [✓]
   * Create shorcuts for installed applications [✓]
   * Add Python to environment variables [✓]
   * Modify the install location to `C:/python/python314/`.

4. Press install and wait for the installation to complete.

References and links
--------------------

.. _third-party-software:

Third-party software
^^^^^^^^^^^^^^^^^^^^
The various third-party software tools that make up the development and deployment environment for CHIL isntruments and dataloggers are listed below.

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Name
    - Used for
    - Version
    - URL
  * - **VS Code**
    - Text editor and development environment CHIL datalogger firmware.
    - v1.121.0
    - `Download <https://code.visualstudio.com/updates/v1_121>`__
  * - **Python**
    - Programming environment for CHIL packet decoding software.
    - v3.14.0+
    - `Download <https://www.python.org/downloads/release/python-3140/>`__
  * - **STM32CubeIDE**
    - STM32 microcontroller development environment for instrument firmware.
    - v2.1.1
    - `Download (login required) <https://community.st.com/stm32cubeide-mcus-28/stm32cubeide-2-1-1-released-163841>`__
  * - **Radiocrafts RCTools**
    - Programming radio module IDs and debugging.
    - v1.98
    - `Download (login required) <https://radiocrafts.com/resources/supporting-software-and-software-tools/#wirelessmbusrctools>`__

.. _firmware:

Firmware and software
^^^^^^^^^^^^^^^^^^^^^
GitHub is used to store and provide version control for CHIL instrument and datalogger firmware, as the `cryodecoder <https://chilcardiff.github.io/cryodecoder/>`__ Python library which is used to decode packets.

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Library name
    - Description
    - Release
    - URL
  * - chillib
    - Shared firmware library
    - v20260521 
    - https://github.com/CHILCardiff/chillib/tree/v20260521
  * - cryoegg-2025 
    - Cryoegg firmware and design files
    - v20260521
    - https://github.com/CHILCardiff/cryoegg-2025/tree/v20260521
  * - cryowurst-2026
    - Cryowurst firmware and design files
    - N/A
    - https://github.com/CHILCardiff/cryowurst-2026/
  * - cryodecoder
    - Python package and CLI interface to decode CHIL packets
    - N/A
    - https://github.com/CHILCardiff/cryodecoder/