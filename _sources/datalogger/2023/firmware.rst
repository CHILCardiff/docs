Firmware
========

Programming
~~~~~~~~~~~

.. note:: 
    
    Do this first somewhere with an internet connection, where you can troubleshoot. Then try with everything in airplane mode, to make sure it all works offline.

Equipment
^^^^^^^^^

* Computer with Datalogger2023 firmware for the instrument you are deploying.
* Datalogger PCB (v2023). 

If you wish to test the Iridium modem, you will also need:

* RockBLOCK+ Iridium modem.
* 12V battery.

Configuring the Iridium modem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The behaviour of the Iridium modem is configured when the datalogger frimware is compiled and **cannot be changed without reuploading the firmware to the datalogger**. There are some applications where the user might not want to use the Iridium modem when it is physically installed; for example, transmitting a large number of radio packets with a short time interval to test radio propagation. In such cases, it is recommended to temporarily disable the Iridium modem and then re-enable it when the deployment is ready.

:numref:`Table %s <tab_iridium_datalogger_settings>` describes the Iridium settings for the datalogger and provides recommended default values.

.. _tab_iridium_datalogger_settings:

.. list-table:: Iridium configuration variables in Datalogger (2023) firmware.
    :header-rows: 1
    :widths: auto

    * - Name
      - Description
      - Default value
      - Variable type
    * - ``DIAGNOSTICS``
      - Enable diagnostic messages for general operation of the datalogger.
      - ``true``
      - bool
    * - ``GET_IRIDIUM_TIME``
      - If *true*, attempt to retrieve the time from the Iridium modem. If *false*, use the compiler timestamp.
      - ``true``
      - bool
    * - ``USE_IRIDIUM``
      - If *true*, attempt to transmit the data using the Iridium modem. If *false*, no packets will be transmitted by Iridium.
      - ``false``
      - bool
    * - ``IRIDIUM_DIAGNOSTICS``
      - Enable diagnostic messages from the Iridium modem - useful if there are problems with the Iridium modem.
      - ``false``
      - bool
    * - ``FAKE_IRIDIUM``
      - Advanced option: if *true*, behave as if the Iridium modem is in use but do not actually transmit any packets. If *false*, behaviour defaults to ``USE_IRIDIUM``. 
      - ``false``
      - bool
    * - ``IRIDIUM_CONNECT_ATTEMPTS``
      - THe number of attempts to try connecting to the Iridium network before falling back.
      - ``1``
      - integer
    * - ``IRIDIUM_HOUSEKEEPING_INTERVAL``
      - The time in milliseconds between attempts to retrieve the time from the Iridium modem.
      - 12 hours (43200000)
      - integer

Configuration options for the Iridium modem are set using C ``#define`` macros near the top of the datalogger firmware (``Datalogger2023.ino``) and are repeated below for convenience.

.. code-block:: C++

    #define DIAGNOSTICS true                                   // change this to see diagnostic messages from the main logger code
    #define GET_IRIDIUM_TIME true                              // if this is true and USE_IRIDIUM is false, we get the time from Iridium but don't try and send any messages
    #define USE_IRIDIUM false                                  // if true, we get the time from Iridium and also try and send Iridium packets; if false we don't bother. If false we rely on getting the compilation time to set the RTC.
    #define IRIDIUM_DIAGNOSTICS true                          // change this to see diagnostic messages from the Iridium library
    #define FAKE_IRIDIUM false                                 // set to false to actually send SBD messages
    #define IRIDIUM_CONNECT_ATTEMPTS 1                         // How many attempts to connect to Iridium and get the timestamp before resetting
    #define IRIDIUM_HOUSEKEEPING_INTERVAL 60 * 60 * 12 * 1000  // 60 * 60 * 10 // Create an interval (in ms) after which the IRIDIUM_FAIL flag will be reset

Uploading to the datalogger
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |arduino_upload| image:: /_static/img/arduino_upload.png 
    :height: 2ex

.. |arduino_serial| image:: /_static/img/arduino_serialmon.png
    :height: 2ex

* Connect the datalogger to the toughbook via USB. Open up the datalogger code in Arduino IDE (should be the git branch danzhur2025_iridium_safe from https://github.com/mrpj100/Datalogger2023, unless told otherwise by CHIL!).

.. important:: Things to check in the datalogger code:
    
    #. Iridium settings (see figure :numref:`fig-iridium-settings-old`). Remember to turn diagnostics on for testing, and off for deployment.
    #. Cryowurst IDs: listed from line 41. There is also a wurst count: this should be the number of wursts in the list of IDs.
    #. timing between transmission: change SBD_SEND_DELAY on line 84 to the set the delay between sending satellite messages. This should be 3600s (1 hour) for deployment, but for testing something like 180s (3 minutes) is good. Any shorter risks confusing the poor modem.

* Upload sketch to the datalogger |arduino_upload|.
* If there is a satellite modem attached, check in the Arduino serial monitor |arduino_serial| to see if the Iridium connection is working. 
* Close Arduino IDE (otherwise VSCode will not connect to the datalogger).
* Open up https://github.com/mrpj100/cryowurst-packet-decoder in VSCode. Change any instance of a named COM port to the correct one (look in Device Manager to find which COM port the datalogger is connected to). Run the script.
* Serial output should display data from the logger, and any cryowurst data packets as they arrive.
    
.. _fig-iridium-settings-old:

.. figure:: iridium_settings_testing.png
   :align: center
   :width: 60%

   Relevant Iridium settings in Datalogger2023 for system testing. Diagnostics can be turned off for deployment. 

Debugging
~~~~~~~~~
If the system is not working: 

* Check which git branch you are using.
* Check there is power to the PCB.
* Check you are using a data USB cable (try another cable - some USB cables only provide power)!
* Check the modem is wired in correctly. You may need to remove the connections and replace them in the on-board connector, or re-strip the ends of the cable.

If none of the above work, reach out to CHIL for further assistance.