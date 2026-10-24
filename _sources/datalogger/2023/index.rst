Datalogger 2023
===============

The 2023 version of the CHIL datalogger was designed by Mike Prior-Jones, Paul Biggs and Hashem Alnader. It is based around the `Adafruit Feather M0 Adalogger <https://www.adafruit.com/product/2796>`__ which hosts the microcontroller and SD card. Its features are summarised in the table below:

.. list-table::
   :widths: auto

   * - **Microcontroller**:
     - `Adafruit Feather M0 Adalogger <https://www.adafruit.com/product/2796>`__
   * - **Data storage**:
     - microSD card (4 to 32 GB).
   * - **Sensors**:
     - `MS5607 <https://www.te.com/en/product-MS560702BA03-50.html>`__ temperature and air pressure sensor.
   * - **Iridium modem interface**:
     - `RockBLOCK+ <https://www.groundcontrol.com/product/rockblock-plus-waterproof-satellite-iot-device/>`__ Iridium satellite modem.

The firmware is based on the Arduino framework and makes use of various libraries to communicate with the sensors and other peripherals.  

.. important::

   The 2023 dataloggers are designed for use with **only one type of instrument at a time** (Cryoegg 2023 or Cryowurst 2023). It is not possible to use different types of CHIL instruments with one 2023 datalogger. 

This section of the documentation describes hardware used in the 2023 version of the datalogger, how to program the firmware and servicing instructions for maintenance in the field.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   hardware
   firmware
   servicing