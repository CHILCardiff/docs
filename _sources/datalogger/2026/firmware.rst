Firmware
========
Firmware for the 2026 version of the receiver is stored on GitHub here: https://github.com/chilcardiff/datalogger-firmware-2026. This version of the datalogger firmware was developed using Visual Studio Code and `PlatformIO`_ as the development environment. 

Unlike previous versions of the CHIL datalogger firmware, it is designed to work with all types of CHIL instruments and is backwards compatible with the 2023 instrument packet formats.

.. _PlatformIO: https://platformio.org/

Programming
-----------
To begin, open the datalogger case and connect the datalogger to a computer with a USB Type A to USB Micro cable. The USB connection inside the datalogger case is located on the Adafruit Feather M0 Adalogger board, highlighted in :numref:`Figure %s <fig_datalogger_usb_connection>`.

.. _fig_datalogger_usb_connection:

.. figure:: ./png

    Connect the datalogger to the PC with a USB Type A to USB Micro cable.

Open the ``datalogger-firmware-2026`` folder in Visual Studio Code. Once PlatformIO has finished initialising, select the serial port associated with the datalogger by pressing ``CTRL + SHIFT + P`` and typing ``Set Project Port``.

.. tip::

    If you aren't sure which COM port is associated with the datalogger, open the *Device Manager* (``Windows Key + R``) and run ``devmgmt.msc``.

    Find the ``Ports (COM & LPT)`` section, remove the USB cable to the datalogger and replace it to identify which port is used.

.. _fig_platformio_select_port:

.. figure:: /_static/img/datalogger/programming/2026/platformio_select_port.png
    :width: 100%

    Selecting the project COM port in PlatformIO.

.. _fig_platformio_upload:

.. figure:: /_static/img/datalogger/programming/2026/platformio_upload.png
    :width: 100%

    Building, uploading and opening a serial monitor in PlatformIO.

Display (latest version)
------------------------
The layout of the latest version of the receiver display is shown in :numref:`Figure %s <fig_chil_datalogger_display_2026b>`. It shows information regarding the SD card configuration, Iridium configuration, environmental sensors on the receiver and data from the latest packet to be received.

.. _fig_chil_datalogger_display_2026b:

.. figure:: /_static/img/datalogger/display_v2026b.png

    Components of the CHIL Datalogger display (v2026b).

Display (initial version)
--------------------------
This version of the display was shipped with the v202605 version of the CHIL datalogger. It consists of four main components, the receiver time

* **Receiver time**: The current timestamp used by the receiver.
* **Warnings**: Indicates current status and functionality of key datalogger subsystems.
* **Config settings**: Shows SD card configuration values.
* **Latest packet**: Instrument ID and data from the last packet to be received.

These components are annotated in :numref:`Figure %s <fig_chil_datalogger_display_2026a>` as a guide to interpreting the display while in the field.

.. _fig_chil_datalogger_display_2026a:

.. figure:: /_static/img/datalogger/display_v2026a.png

    Components of the CHIL Datalogger display (v2026a).