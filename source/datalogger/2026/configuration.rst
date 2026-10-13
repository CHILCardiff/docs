SD card configuration
=====================
The 2026 version of the datalogger firmware introduces an text-based configuration file stored on the SD card so that the datalogger no longer needs to be reprogrammed during servicing to update configuration values. The parameters are categorised into the following groups:

* **System**: General datalogger configuration.
* **Iridium**: Iridium timekeeping and data transmission.
* **Safelist**: Safelist configuration.
* **Housekeeping**: Receiver housekeeping and logging.

.. important::

    When making changes to the configuration file ``config.ini`` on the SD card, it is recommended to **power down** the receiver prior to removing the SD card and only **power up** the receiver after replacing it to avoid interrupting any data write operations to the card.

    You **must** reset or power-cycle the receiver after making changes to the ``config.ini`` file for them to have any effect.

System parameters
-----------------
System parameters allow for behaviour such as the display refresh rate, sensor update rate and receiver ID to be defined.

.. _tab_general_params:

.. list-table:: General datalogger parameters.
    :widths: auto
    :header-rows: 1

    * - Field
      - Description
      - Default value
      - Format
    * - ``receiver_id``
      - The receiver ID is used to identify the receiver and distinguish between multiple receivers in the satellite communication layer. Try to follow the convention that a fixed tripod receiver ID begins with 'T' (``0x54``), while a portable datalogger receiver ID begins with 'P' (``0x50``).
      - 00000000
      - Hex string representing 4 bytes.
    * - ``display_update_rate_slow``
      - Display update rate in seconds for the 'SLOW' toggle switch setting
      - 60
      - Integer value of seconds.
    * - ``display_update_rate_fast``
      - Display update rate in seconds for the 'FAST' toggle switch setting 
      - 5
      - Integer value of seconds.
    * - ``sensor_update_rate``
      - Sensor update rate in seconds after which environmental sensors such as the BMA400, MS5607, SHT30 etc. will be updated.
      - 10
      - Integer value of seconds.

Iridium parameters
------------------
The Iridium parameters determine whether the Iridium modem is used as a timebase for the receiver, whether data packets are transmitted via satellite and if so, how frequently. There are three operating modes for the Iridium modem which are set using the ``mode`` parameter and described below:

* **Mode 1**: Transmit all packets on reception, as individual satellite messages.
* **Mode 2**: Every (iridium_time_interval) seconds, transmit the most recent package for each UID received. The UIDs must be in the safelist for this to work the `enable_safelist` is effectively ignored.
* **Mode 3**: (*not currently implemented*): Collate RSSI for identical packets received on mutliple channels and only transmit the message contents once. 

.. _tab_iridium_params:

.. list-table:: Iridium datalogger parameters.
    :widths: auto
    :header-rows: 1

    * - Field
      - Description
      - Default value
      - Format
    * - ``mode``
      - The Iridium mode determines in the pattern of satellite transmissions made by the receiver.
      - 1
      - Integer (1, 2 or 3)
    * - ``iridium_time``
      - If set to 'true', the datalogger time will be set to the UTC timestamp received from the Iridium network. This will be overwritten if the 'gps_time' variable is also set to true and a time value can be obtained.
      - ``true`` 
      - 'true' or 'false', case insensitive.
    * - ``iridium_transmit``
      - If iridium_transmit=true, then the Iridium modem will be used. If iridium_transmit=false, then no messages will be sent via satellite.
      - '`true``
      - 'true' or 'false', case insensitive.
    * - ``connection_attempts`` 
      - The number of times the datalogger will attempt to get the time or start the modem before continuing.
      - 3
      - Integer (positve, non-zero). 
    * - ``iridium_time_interval``
      - If iridium_time=true, the iridium_time_interval parameter specifies the interval at which the datalogger timestamp will be updated from the satellite modem. Defaults to 12 hours.
      - 43200
      - Integer number of seconds.
    * - ``iridium_transmit_interval``
      - If the datalogger is operating in mode=2 then send an Iridium update every (iridium_transmit_inteval) seconds if there is new data available. Defaults to 1 hour.
      - 3600
      - Integer number of seconds.

Safelist parameters
-------------------
The safelist parameters are used when **not** operating in the *transmit all* (``mode=1``) modality. The safelist is a user-defined text file stored on the SD card and lists a collection of instrument IDs which are 'safe' to transmit via the Iridium satellite link. The purpose of this functionality is to allow for the introduction of new instruments to a fieldsite without overwhelming the Iridium link with deployment packets. When the new instruments have been succesfully deployed, their IDs can be added to the safelist and (**after resetting the receiver**) will begin transmitting.

.. _tab_safelist_params:

.. list-table:: Safelist datalogger parameters.
    :widths: auto
    :header-rows: 1

    * - Field
      - Description
      - Default value
      - Format
    * - ``enable_safelist``
      - If enable_safelist is false, all MBUS receiver IDs will be accepted for  processing as a CHIL packet. If enable_safelist=true, then only the receiver IDs provided in the  safelist file will be processed.
      - false 
      - 'true' or 'false', case insensitive.
    * - ``safelist_file``
      -  safelist_file specifies the path on the SD card to the safelist file. The path should be less than 32 characters.
      - safelist.txt
      - Text string, file path.

Housekeeping parameters
-----------------------

.. warning::

    The housekeeping behaviour is not yet implemented, these settings will not have any effect on the behaviour of the datalogger.

.. _tab_housekeeping_params:

.. list-table:: Housekeeping datalogger parameters.
    :widths: auto
    :header-rows: 1

    * - Field
      - Description
      - Default value
      - Format
    * - ``enable_housekeeping_sd``
      - If enable_housekeeping_sd=false, no housekeeping messages will be stored by the receiver. If enable_housekeeping_sd=true, housekeeping messages will be written to the SD card at the interval defined by the housekeeping_interval in seconds.
      - false
      - 'true' or 'false', case insensitive.
    * - ``enable_housekeeping_iridium``
      - If enable_housekeeping_iridiumm=false, no housekeeping messages will be sent from the receiver. If enable_housekeeping_iridium=true and iridium_transmit=true, housekeeping messages will be transmitted at the interval defined by the housekeeping_interval in seconds
      - false
      - 'true' or 'false', case insensitive.
    * - ``housekeeping_interval``
      - The interval to save and transmit housekeeping messages. Defaults to 6 hours.
      - 21600
      - Integer number of seconds.