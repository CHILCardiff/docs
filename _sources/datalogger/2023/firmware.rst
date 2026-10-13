Firmware
========

Equipment
~~~~~~~~~~

* Computer with datalogger firmware
* Datalogger PCB (v2023). 

Programming
~~~~~~~~~~~

.. |arduino_upload| image:: /_static/img/arduino_upload.png 
    :height: 2ex

.. |arduino_serial| image:: /_static/img/arduino_serialmon.png
    :height: 2ex

Do this first somewhere with an internet connection, where you can troubleshoot. Then try with everything in airplane mode, to make sure it all works offline.

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