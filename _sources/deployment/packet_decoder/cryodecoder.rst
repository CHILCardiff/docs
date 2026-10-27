.. _cryodecoder_packet_decoder:

Cryodecoder (2026)
==================

.. hint::

    Cyrodecoder is described its `documentation <https://chilcardiff.github.io/cryodecoder/>`__, which gives usage examples for serial and file decoding, as well as a complete API for use in your own software.

Cryodecoder is a Python package which implements the decoding logic for the revised CHIL instrument packet format. It is also backwards compatible with the 2023 versions of CHIL packets. As well as an application programming interface (API), it provides a command line interface (CLI) to run the decoder in real-time and decode packets transmitted over a USB (serial) link, or to decode files from CHIL dataloggers and convert them to comma-separated files.

USB (serial) decoding
---------------------

Connect to the datalogger
^^^^^^^^^^^^^^^^^^^^^^^^^
Connect your PC to a CHIL datalogger using a USB to USB Micro cable (see :numref:`Figure %s <fig_adalogger_receiver>`).

.. _fig_adalogger_receiver:

.. figure:: /_static/img/cryodecoder/adalogger_in_receiver.png

    Adafruit Feather M0 Adalogger USB connection and SD card on CHIL Datalogger PCB.

On a Windows PC, load the Device Manager (``Windows Key + R`` then enter ``devmgmt.msc``) and identify the *Ports (COM & LPT)* section (:numref:`Figure %s <fig_device_manager>`). If no other serial devices are connected to your PC, then the datalogger port will be the only one shown in the list. You can check that the COM port address is correct by removing the USB cable and verifying that the entry disappears from the device manager list. Reconnect the USB cable when finished.

.. _fig_device_manager: 

.. figure:: /_static/img/cryodecoder/device_manager.png

    Windows Device Manager to identify COM port address (*COM5* in this example).

Starting cryodecoder
^^^^^^^^^^^^^^^^^^^^
.. important:: 
    These instructions assume you have followed the `setup instructions <setup>`__ If you installed cryodecoder to a `virtual environment <https://docs.python.org/3/library/venv.html>`__ then make sure it is activated before continuing.

To launch cryodecoder, open a new terminal (command prompt) window. If necessary, locate and activate the virtual environment where you have installed cryodecoder. If you followed the :ref:`setup instructions <devenv>` then this will be in ``C:\chil\.env``. 

Cryodecoder saves data to the a folder named ``data`` within the current working directory in the command prompt window. To navigate to a location where you wish to save data, use the ``cd`` command:

.. code-block:: shell

    cd /path/to/my/data

When started, cryodecoder will make a new folder with the current PC timestamp within the ``data`` folder. This means that you can use the same ``data`` folder for multiple sessions using cryodecoder.

To start the cryodecoder software, enter the following command in the terminal window, replacing ``COM5`` with the name of the COM port you identified earlier. This runs cryodecoder in ``serial`` mode and sets ``COM5`` as the port we wish to connect to.

.. hint::
    If you are using one of the Radiocrafts `development kit boards <https://radiocrafts.com/products/development-kits/buy-a-development-kit-from-radiocrafts/>`__, it is possible to decode MBus packets without using a CHIL datalogger by selecting the `-m mbus` option when starting cryodecoder. 

.. code-block:: shell

    cryodecoder -p COM5 serial

Also shown in :numref:`Figure %s <fig_serial_cli_launch>` is the output from cryodecoder help message which explains the various options that can be provide to the receiver. 

.. _fig_serial_cli_launch:

.. figure:: /_static/img/cryodecoder/serial/serial_cli_launch.png

    cryodecoder help menu and command to launch in *serial* mode.

Using the display
^^^^^^^^^^^^^^^^^

If you have connected successfully to the datalogger, you will periodically see messages from the receiver which provide updates on the status of the various on-board sensors (:numref:`Figure %s <fig_serial_cli_receiver_sensors>`). Additionally, information is also provided on whether there are still packets in the buffer which remain to be transmitted over the satellite connection or saved to the SD card. A countdown is also provided until the next time at which the receiver time will be updated using the satellite connection. 

.. _fig_serial_cli_receiver_sensors:

.. figure:: /_static/img/cryodecoder/serial/cli_receiver_sensors.png

    Example output from cryodecoder displaying the datalogger environmental sensor values.

When a packet is received from a CHIL instrument, multiple sources of information are sent to the command line (:numref:`Figure %s <fig_serial_received_packet>`). Some of this originates from the serial debugging output from the datalogger, which is interspersed with the logging output from cryodecoder indicating that a packet has been received. 

.. _fig_serial_received_packet:

.. figure:: /_static/img/cryodecoder/serial/received_packet_annotated.png

    cryodecoder command line output when received a packet from Cryowurst.

Additional output may also appear from the receiver while it is performing operations using the Iridium modem, such as transmitting a packet over the sallite connection (:numref:`Figure %s <fig_serial_transmitting_packet>`).

.. _fig_serial_transmitting_packet:

.. figure:: /_static/img/cryodecoder/serial/cli_transmitting_packet.png

    cryodecoder command line output showing debugging information related to the Iridium modem.

Output files
------------
While the logger is running, it writes to three files in the timestamped directory it created within the ``data`` folder. The files serve different purposes and contain the content described below:

* ``logger_YYYYmmdd_HHMMSS.log``: logger and messages from the receiver and cryodecoder.
* ``raw_YYYYmmdd_HHMMSS.log``: raw data transmitted over the serial link as a hexadecimal stream.
* ``data_YYYYmmdd_HHMMSS.csv``: parsed packet data into a CSV format for quick analysis.

Log file
^^^^^^^^
The ``logger_\*.log`` file contains output from the datalogger that is prefixed with *#* (the log or comment symbol). Each line is prefixed with a logging level and timestamp which corresponds to the time on the host PC adjusted to UTC.

.. code-block:: 
    
    [INFO] 2026-10-14 12:01:05,971:  ---------------- Receiver sensors ----------------
    [INFO] 2026-10-14 12:01:06,005:  Time: 2026-10-14 11:01:05, Display update: 10 s
    [INFO] 2026-10-14 12:01:06,011:  --------------------------------------------------
    [INFO] 2026-10-14 12:01:06,018:  SHT30   Temp.: N/A, Relative Humidity: N/A

The ``logger_\*.log`` file provides a record of the receiver messages during the cryodecoder session and can be useful for debugging issues with Iridium connectivity or a quick reference to received packets.

Raw file
^^^^^^^^
The ``raw_\*.log`` file contains a hexadecimal stream of the raw data transmitted by the serial connection during the cryodecoder session. This is different from the ``*.log`` file that is stored on the SD card in that is also captures the logging messages sent by the receiver in addition to data packets.

.. note::
    Work is in progress on a utility function in the cryodecoder API to convert ``raw_\*.log`` files to the same format as the ``*.log`` files stored on the SD card. 

CSV file
^^^^^^^^
The ``data_\*.csv`` file contains decoded packet data and raw hexadecimal strings for packets sent over the serial connection. It is described in detail in the next section.

File decoding
-------------

The cryodecoder library can also be used to parse `.log` files from CHIL dataloggers into a `*.csv` format for easier data manipulation. This page describes the steps required to do achieve this.

.. important:: 
    These instructions assume you have followed the `setup instructions <setup>`__ If you installed cryodecoder to a `virtual environment <https://docs.python.org/3/library/venv.html>`__ then make sure it is activated before continuing.

    To activate the virtual environment on a Windows PC, navigate to the folder and use the shell command below. Replace ``.env`` with the name of the folder containing your virtual environment.

    .. code-block::

        .\.env\Scripts\activate
        
1.  After activating the virtual environment with cryodecoder installed, navigate to the path containing your data.

2.  
    Run cryodecoder in *file* mode to decode the raw ``.log`` file to ``.csv``.

    .. code-block:: shell

        cryodecoder file -i childata.log -i childata.csv

    The ``-i`` and ``-o`` flags are used to pass the input filename and output filename respectively.

3.  Once the file has finished decoding, it will show a message with the total number of packets (blocks) decoded. A summary of the top-level blocks decoded will also be displayed.

.. figure:: /_static/img/cryodecoder/file_decoder.png

    Example commands to decode ``*.log`` files from CHIL dataloggers.

See the CSV file `documentation <https://chilcardiff.github.io/cryodecoder/csv/logfile.html>`__ for more information on the format of the decoded CSV file. If you wish to interrogate the raw data in more detail, we recommend using the Python API which is described `here <https://chilcardiff.github.io/cryodecoder/reference/>`.
