.. _devenv:

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

.. note::

    These instructions assume that you **do not have access to the Internet**. Even if you do, it is worthwhile disabling your WiFi or Ethernet connection while installing the software to ensure that it can be replicated in the field.

The installation instructions below were tested on 2026-05-21 using a Windows laptop without a internet connection. If you find any issues with the instructions below, let us know by `sending an email <hawkinsj22@cardiff.ac.uk>`__.

The latest files for the development environment are stored in a ZIP archive (``childev.zip``) which should have a folder structure matching the below:

*   ``firmware/`` instrument and datalogger firmware.

    *   ``2023/`` 2023 firmware.

        *   ``Arduino/`` Arduino versions of datalogger firmware.
        *   ``PlatformIO/`` PlatformIO versions of datalogger firmware.

    *   ``2026/`` 2026 firmware.

* ``installers/`` third-party software installers.
* ``software/`` CHIL developed software and Python libraries.
* ``vscode_extensions/`` useful extensions for Visual Studio Code.
* ``wheels/`` Python wheels for installing modules offline.

Step 1: Download installation files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Extract** ``childev.zip`` **to a folder named** ``C:\tools\childev`` **on your PC**. 

.. figure:: /_static/img/setup/folder_childev.png

    Folder structure of the ``C:\tools\childev`` folder.

If you are using a **complete version of** ``childev.zip`` **you can skip the remainder of this step**. 

We cannot host the complete ``childev.zip`` archive online because of the inclusion of installers for third-party software. Before continuing to the next step, download these third-party software installers (also :ref:`listed below <third-party-software>`) and copy them to the `installers` directory in your ``C:\tools\childev`` folder. 

.. list-table:: Third-party software installers.
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

We recommend keeping local copies of the offline installers on your machine, a hard drive or USB flash drive in case you need to reset your development environment while in the field. 

Step 2: Setup code repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this step, you will create a local copy of all the firmware and software for the CHIL instruments and datalogger on your PC.

**If you are using the provided versions of firmware and software from** ``childev.zip``, you will need to extract the following folders to your hard drive. Source folder refers to the location within ``chilldev.zip`` and destination folder refers to the path on your hard drive.

.. important::

    When extracting ZIP archives, you can end up with "nested" folders with the same name as the repository. For example, extracting ``archive.zip`` can result in a folder structure of ``archive\archive\``. The following instructions **assume that you have manually de-nested any folders** after extraction.

.. list-table:: Firmware and software folders for the latest version of CHIL instruments.
    :header-rows: 1

    * - Source folder
      - Destination folder
    * - ``firmware\2026\chillib-20260521.zip``
      - ``C:\chil\chillib``
    * - ``firmware\2026\cryoegg-2025-20260521.zip``
      - ``C:\chil\cryoegg-2025``
    * - ``firmware\2026\cryowurst-2026-20260611.zip``
      - ``C:\chil\cryowurst-2026``  
    * - ``firmware\2026\datalogger-firmware-2026-20261023.zip``
      - ``C:\chil\datalogger-firmware-2026``
    * - ``software\cryodecoder-2.1.0-beta.zip``
      - ``C:\chil\cryodecoder-2.1.0-beta```

Older verisons of firmware and software for the 2023 versions of CHIL instruments and dataloggers are also available. The receiver firmware is available in two formats: one to be used with VS Code and Platform IO and one to be used with Arduino IDE.

.. list-table:: Archive firmware and software folders for older versions of CHIL instruments.
    :header-rows: 1

    * - Source folder
      - Destination folder
    * - ``software\CryoeggPacketDecoder_Python314.zip``
      - ``C:\chil\CryoeggPacketDecoder```
    * - ``software\cryowurst-packet-decoder-DualChannel-2024-withKellerandIMUaccel.zip``
      - ``C:\chil\cryowurst-packet-decoder``
    * - ``firmware\2023\cryoegg-2022.zip``
      - ``C:\chil\cryoegg-2022``
    * - ``firmware\2023\cryowurst-2023.zip``
      - ``C:\chil\cryowurst-2023``
    * - ``firmware\2023\Arduino\datalogger-2023-cryoegg-arduino``
      - ``C:\chil\datalogger-2023-cryoegg-arduino``
    * - ``firmware\2023\Arduino\datalogger-2023-cryowurst-arduino``
      - ``C:\chil\datalogger-2023-cryowurst-arduino``
    * - ``firmware\2023\Arduino\datalogger-2023-cryoegg-platformio``
      - ``C:\chil\datalogger-2023-cryoegg-platformio``
    * - ``firmware\2023\Arduino\datalogger-2023-cryowurst-platformio``
      - ``C:\chil\datalogger-2023-cryowurst-platformio``

Alternatively, it is possible clone the newer (2026) firmware from GitHub so that you can keep it updated to the latest version. **If you are cloning firmware from GitHub**, you will need to clone the following repositories using the command

.. code-block:: shell

    git clone [repository_url] [destination_folder]

The repository URL and destination folders are given in the table below:

.. list-table::
    :header-rows: 1

    * - Repository name
      - Repository URL
      - Destination folder
    * - chillib
      - `https://github.com/chilcardiff/chillib`__
      - ``C:\chil\chillib``
    * - cryoegg-2025
      - `https://github.com/chilcardiff/cryoegg-2025`__
      - ``C:\chil\cryoegg-2025``
    * - cryowurst-2026
      - `https://github.com/chilcardiff/cryowurst-2026`__
      - ``C:\chil\cyrowurst-2026``
    * - datalogger-firmware-2026
      - `https://github.com/chilcardiff/datalogger-firmware-2026`__
      - ``C:\chil\datalogger-firmware-2026``
    * - cryodecoder
      - `https://github.com/chilcardiff/cryodecoder`__
      - ``C:\chil\cryodecoder``

Once you have cloned all of the repositories above, you are ready to proceed to the next step.

Step 3: Install Python 3.14
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run the installer ``python-3.14.5-amd64.exe`` located in ``C:\tools\childev\installers``.

#. Select **Customize installation** and "Add python.exe to PATH" before proceeding.

.. figure:: /_static/img/setup/python_customise_path.png

    Initialise a custom installation of Python 3.14.

#. On the Optional Features menu, ensure all options are selected except for "for all users".

.. figure:: /_static/img/setup/python_optional_features.png

    Optional installation features for Python 3.14.

#. On the Advanced Options menu:

   * Install Python 3.14 for all users [?] (user choice)
   * Associated files with Python [✓]
   * Create shorcuts for installed applications [✓]
   * Add Python to environment variables [✓]
   * Modify the install location to ``C:\python\python314``.

.. figure:: /_static/img/setup/python_advanced_options.png

    Advanced options for Python 3.14 install.

#. Press install and wait for the installation to complete.

.. figure:: /_static/img/setup/python_complete.png

    Successful installation of Python 3.14.

#. Restart your PC.

Step 4: Install cryodecoder
^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Open a terminal (command prompt) window and navigate to the folder where you have extracted the repositories.

#. Navigate to the repository folder, create a virtual environment and activate it using the steps below:

.. code-block::

    cd C:/chil
    python -m venv .env
    .\.env\Scripts\activate

.. figure:: /_static/img/setup/cmd_virtual_env.png

    Create and activate  virtual environment.

#. **Once the virtual environment is activated**, install cryodecoder in editable mode using the following command:

.. note:: 

    You will need to change ``C:\tools\childev\wheels`` to the path where you extracted the ``childev\wheels`` folder.

    You will also need to change ``cryodecoder-2.1.0-beta`` to the name of your *cryodecoder* folder in ``C:\chil``.

.. code-block::

    python -m pip install --no-index --find-links=C:\tools\childev\wheels -e ./cryodecoder-2.1.0-beta

.. figure:: /_static/img/setup/cmd_success_install.png

    Successful install of cryodecoder (and requirements) in editable mode.

#. You can validate that cryodecoder has installed by running the ``cryodecoder --help`` command.

.. figure:: /_static/img/setup/cmd_cryodecoder_help.png

    Help message from cryodecoder, indicating a successful install.

Step 5: Install VS Code
^^^^^^^^^^^^^^^^^^^^^^^

#. Located in ``C:\tools\childev\installers``, run `VSCodeUserSetup-x64-1.121.0.exe`.
#. Select "I accept the agreement" on the following splash screen and install the software to the default location.

.. figure:: /_static/img/setup/vscode_agreement.png

    Accept license agreement for VS Code.

#. Use the default installation folder and press *Next*.
#. Use the default start menu folder and press *Next*.
#. Ensure that "Add to PATH" is selected and optionally select to create a desktop icon.

.. figure:: /_static/img/setup/vscode_path.png

    Set PATH option for VS Code.

#. Press *Install* and wait for the installation to complete.

.. figure:: /_static/img/setup/vscode_launch.png

    Launch VS Code once installation has finished.

#. Once the installation has completed, load VS Code and proceed to the next step of installing PlatformIO.


.. note:: 
    If you receive any notifications or prompts regarding GitHub and AI-powered development, these can be ignored **unless you are using GitHub to manage your repositories**. 

.. important::
    If you are connected to the internet, ignore any prompts to update VS Code or the extensions (next step).

Step 6: Install PlatformIO
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open VS Code and open the "Extensions" menu (`View > Extensions` from the top menu bar).

.. figure:: /_static/img/setup/vscode_extensions.png

    Open Extensions menu in VS Code.

2. Select the `Install from VSIX` option from the three dots (`...`) menu at the top of the extensions screen. 

.. figure:: /_static/img/setup/vscode_installfromvsix.png

    Install extesions from VSIX files in VS Code.

3. Navgiate to the `childev/vscode_extensions` folder and install the following extensions:

    * VS Code cpptools: `ms-vscode.cpptools-1.32.2-win32-x64.vsix`
    * VS Code cpptools extension: `ms-vscode.cpptools-extension-pack-1.5.1.vsix`
    * VS Code cpp-devtools: `ms-vscode.cpp-devtools-0.5.13.vsix`
    * VS Code cmake-tools: `ms-vscode.cmake-tools-1.23.52.vsix`
    * PlatformIO: `platformio.platformio-ide-3.3.4-win32-x64.vsix`

4. Extract the contents of `.platformio.zip` folder from `childev/installers` to `C:/Users/[username]/.platformio` - make sure you don't end up with a nested folder (i.e. `.platformio/.platformio/...`). This is a large ZIP archive so might take some time!

.. figure:: /_static/img/setup/platformio_folder.png

    Copy the contents of the ``.platformio`` folder to match this figure.

4. Restart your PC.

Step 7: Install datalogger firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the example below, the 2026 firmware is setup (`datalogger-firmware-2026-*`). If you are using the older (2023) version of the datalogger, complete the same steps for `datalogger-2023-cryoegg` or `datalogger-2023-cryowurst`.

.. note:: 

    Alternative versions of the datalogger firmware for Arduino IDE are available in the ``datalogger-2023-*-arduino`` folders. Follow the instructions :ref:`here <devenvarduino>`.

1. If you haven't already, extract the contents of the datalogger firmware ``firmware/2026/datalogger-firmware-2026-*`` to ``C:/chil/datalogger-firmware-2026``. Double check that you haven't nested any folders - firmware folder should contain the ``data/``, ``lib/`` and ``src/`` folders.
2. Extract the contents of `firmware/chillib-*` library to `C:/chil/chillib-*`. As above, check to avoid nested folders.
3. Open VS Code and open the `C:/chil/datalogger-firmware-2026` folder. 

.. note:: 
    
    If prompted to trust the authors of the repository, confirm that you trust us!

    Alternatively, you may need to press "Restricted Mode" in the bottom left of the window and agree to trust the folder.

.. figure:: /_static/img/setup/vscode_trust.png

    Trust the repository before being able to proceed.

4. Open ``platform.ini`` and replace ``symlink://../chillib`` with the path to the *chillib* folder you just extracted (i.e. ``C:/chil/chillib-*``). 
5. Wait for the library manager to finish installing the project libraries.

.. figure:: /_static/img/setup/platformio_libraries.png

    Update *chillib* location and allow PlatformIO to install libraries.

4. Press `CTRL+SHIFT+P`, type in `PlatformIO: Build` to the text box at the top of the screen and press enter. This will compile the Datalogger firmware. An output terminal should appear at the bottom of the screen and show a `[SUCCESS]` message - this might take a while the first time you run the build command.

.. figure:: /_static/img/setup/platformio_build.png

    Build the project to verify all dependencies have been installed.

5. If you have a datalogger board (or just the Arduino Feather M0) to hand, plug it into the USB connection of the laptop, press `CTRL+SHIFT+P` and type `PlatformIO: Upload`. Press enter and the firmware should be uploaded to the datalogger.

.. figure:: /_static/img/setup/platformio_success.png

    Success message on completion of a successful build.

Step 8: Install STM32CubeIDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You will need to use STM32CubeIDE to program CHIL instruments which use the STM32L4 series of microcontrollers - this includes Cryoeggs, Cryowurst, Cryobeans, SmartSnowStake, etc.

#. Unzip the installer located in `C:\tools\childev\installers\st-stm32cubeide_2.1.1_28236_20260312_0043_x86_64.exe.zip` to a location of your choice.
#. Run the installer file (`st-stm32cubeide_2.1.1_28236_20260312_0043_x86_64.exe`). Press *Next >* when it loads to begin installation.

.. figure:: /_static/img/setup/stm32_begin.png

    Start the STM32CubeIDE installation.

#. Agree to the license and press *Next >*.
#. Use the default installation folder and press *Next >*.
#. When prompted to choose components to install, ensure that both *SEGGER J-Link drivers* and *ST-LINK* drivers are selected and press *Install >* to begin.

.. figure:: /_static/img/setup/stm32_drivers.png

    Ensure that ST-LINK and SEGGER J-Link drivers are selected to be installed.

#. Launch the STM32CubeIDE software.
#. When prompted to select a directory as a workspace update the filepath to `C:/Users/<username>/STM32CubeIDE/chil` and select `Launch`.

.. figure:: /_static/img/setup/stm32_path.png

    Set the path for the STM32CubeIDE workspace.

When STM32CubeIDE has loaded, you're ready to setup the development environment for a CHIL instrument. Close the *Information Center* view to reveal the Project Explorer.

Step 9: Setup STM32CubeIDE environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Within the ``chil`` workspace you have just created in STM32CubeIDE (see previous step!), we can import the firmware libraries for CHIL instrumentation.

Add `chillib` library
"""""""""""""""""""""
1. Select File > Import.... A dialog box will open. Choose the option General > Existing Projects into Workspace and press *Next >*.

.. figure:: /_static/img/setup/stm32_import.png

    Import *chillib* as an existing project.

2. Browse for the ``chillib-*`` folder in ``C:/chil`` and select it as the root directory. If succesful, you should see a project named ``chillib`` in the Projects window. Press *Finish*.

.. figure:: /_static/img/setup/stm32_import_path.png

    Select the *chillib* project.

Add instrument firmware
"""""""""""""""""""""""
Repeat the steps above for the following folders in ``C:/chil`` (or wherever you copied the repositories to).

* ``cryoegg-2025-*``
* ``cryoegg-2022`` (archive version of the Cryoegg firmware for pre-2026 hardware).
* ``cryowurst-2026-*``
* ``cryowurst-2023`` (archive version of the Cryowurst firmware for 2023 hardware).

.. note::

    The ``cryoegg-2025-*`` folder contains an additional project named ``test_IMU``. You can unselect this project before pressing *Finish* to avoid importing it into the workspace.

When finished, the project explorer in STM32CubeIDE should look like :numref:`Figure %s <fig_stm32_project_explorer>`.

.. _fig_stm32_project_explorer:

.. figure:: /_static/img/setup/stm32_all_projects.png

    All STM32 projects imported into STM32CubeIDE.

Step 10: Install Radiocrafts RCTools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.  Extract the MBUS tools from ``C:\tools\childev\installers`` and run ``MBUS-Tools_installer.msi``. Select *Next >* to proceed with the installation.

2.  Install the MBUS tools to the default recommended folder. Select whether to install it for all users (*Everyone*) or only the current user (*Just me*) as desired. Press *Next >* to continue.

.. figure:: /_static/img/setup/rctools_setup_folder.png

    Selecting the installation location for the Radiocrafts MBUS tools.

3.  Once the software has finished installing, press *Close* to complete the installation and verify the software has installed by locating it in the Windows menu.

.. figure:: /_static/img/setup/rctools_setup_check.png

    Verify that the Radiocrafts *MBUS-DEMO* and *MBUS-CCT* software have installed by searching from the Windows menu.

Third-party software and instrument firmware
--------------------------------------------

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

.. toctree::
  :hidden:

  Arduino IDE (archive) <devtools-2023>