Firmware and programming
========================

Firmware
--------
The latest source code for the Cryowurst firmware is stored on GitHub here: https://github.com/CHILCardiff/cryowurst-2026/. At present, we do not provide pre-compiled ``.elf`` files to program the instrument using *STM32CubeProgrammer* or similar binary flashing tools.

You should already have downloaded the latest version of the firmware for Cryowurst when :ref:`setting up your CHIL development environment <devenv>`.

Programming using STM32CubeIDE
------------------------------
The following section describes the equipment required and necessary steps to program the Cryowurst sensor. Programming the sensor allows the user to change the measurement interval, number of deployment packets and radio packet version used.

Equipment
^^^^^^^^^

To program the Cryowurst, you will need the items shown below in addition to an assembled Cryowurst motherboard, power switch and batteries.

a. STMicroelectronics `STLINK-V3 Programmer <STLINK-V3>`_ for STM32 microcontrollers.
b. USB-A to Micro-USB cable.
c. Tag-Connect `TC2030-IDC-NL`_ programming cable.
d. *(Optional)* Tag-Connect `TC2030-CLIP`_ retaining board.

.. _STLINK-V3: https://www.st.com/en/development-tools/stlink-v3set.html
.. _TC2030-IDC-NL: https://www.tag-connect.com/product/tc2030-idc-nl
.. _TC2030-CLIP: https://www.tag-connect.com/product/tc2030-retaining-clip-board-3-pack

Steps
^^^^^

.. _fig_programming_cryowurst:

.. figure:: /_static/img/cryowurst/programming.png  

    Connecting the Cryowurst (2026) to the STLINK-V3 programmer.

1. Connect the Tag-Connect cable to the STLINK-V3 programmer using the exposed connector underneath and **connect the STLINK-V3 to your PC**.
2. Insert the Tag-Connect cable to connector ``J2`` on the Cryowurst motherboard on the **same side as the radio module and microcontroller**.
3. If using the retaining clip, press this onto the Tag-Connect pins on the other side of the board.
4. Connect a battery and power switch (``POWER_EN``). You are now ready to program the Cryowurst.

.. note::

    It can be easier to disconnect the motherboard from the sensorboard while programming the Cryowurst to avoid damaging the header. **If you are diagnosing problems** with the EC, temperature or pressure sensors, then ensure that the sensorboard is connected. 

The following steps assume you have set up your the CHIL development environment. If not, follow the :ref:`setup instructions <devenv>` and then return to this step when completed.

5. Open STM32CubeIDE and ensure that the ``cryowurst-2026`` and ``chillib`` projects are open (check by right-clicking in the Project Explorer window).

.. _fig_main_c_cryowurst:

.. figure:: /_static/img/cryowurst/programming/main_c_programming_setttings.png

    STM32CubeIDE development environment and Cryowrust configuration settings.

6. Find ``Core/Src/main.c`` in the Project Explorer and open the file. Scroll down to the ``int main(void)`` function (Line 118 at time of writing). This section defines the deployment behaviour of the instrument. If you wish to modify the behaviour, update these values in ``main.c``. Each value is described below in the table below:

.. _table_cryowurst_variables:

.. csv-table::
    :widths: auto
    :header-rows: 1

    Varible name,Description,Units,Default value
    ``deployment_sleep_period_s``,The time period in seconds to sleep between each deployment measurement.,seconds,``27``
    ``max_deployment_packets``,The total number of packets to send before entering long term deployment mode (max. value of 255).,N/A,``240``
    ``long_term_sleep_period_s``,The time period in seconds to sleep between each measurement.,seconds,``897``
    ``invert_ec``,*(Advanced)* Changes the polarity of the EC sensor.,N/A,``0``

.. note::
    
    When defining sleep periods, account for the time period the instrument takes to make each measurement by subtracting 3 seconds from the desired value. For example, to have a deployment interval of 30 seconds, set ``deployment_sleep_period_s = 27``. 

7. Open the *Debug Configurations* dialog box from ``Run > Debug Configurations`` in the top menu bar.

.. _fig_debug_conf_cryowurst:

.. figure:: /_static/img/cryowurst/programming/debug_configurations.png

    Debug Configuration settings to program the Cryowurst using STM32CubeIDE.

8. If there is no configuration available under *STM32 C/C++ Application* and ensure that the Debugger settings match those in :numref:`Figure %s <fig_debug_conf_cryowurst>`.
9. When you are ready to program the Cryowurst, press the *Debug* button in the *Debug Configurations* dialog box.

.. _fig_halt_after_debug:

.. figure:: /_static/img/cryowurst/programming/halt_after_debug.png

    Code execution paused in debug mode after successful programing of Cryowurst.

10. 
    If you succesfully program the Cryowurst, you should see output in the Console which matches :numref:`Figure %s <fig_halt_after_debug>`. The programmer has halted execution of the program at the start of the main function. At this point, you can choose to:

    a. Disconnect the programmer and power from the Cryowurst and test it at a later date.
    b. Continue to run the program and check sensor outputs (see Step 11) by pressing the resume icon (pink arrow in :numref:`Figure %s <fig_halt_after_debug>`).
11. Open the Serial Wire Viewer Output window to check the instrument is working. If you have not previously configured the Serial Wire Viewer, follow the instructions :ref:`here <serial_wire_viewer_setup>`.

.. figure:: /_static/img/cryowurst/programming/swv_trace.png

    Output from Cryowurst in the SWV ITM Data Console.

You have now succesfully programmed the Cryowurst for deployment.

.. _serial_wire_viewer_setup:

Configuring Serial Wire Viewer (SWV)
------------------------------------
To configure the serial wire viewer (SWV) to view debugging data from CHIL instruments, follow the instructions below:

1. If not already open, create a new SVW ITM Data Console Window by selecting ``Window > Show View > SWV > SWV ITM Data Console`` from the top menu bar.

.. _fig_swv_data_console:

.. figure:: /_static/img/cryowurst/programming/swv_data_console.png

    Open an SWV ITM Data Console Window.

2. Open the settings by selecting the "tools" (spanner and screwdriver) menu in the top right of the SWV ITM Data Console Window. Copy the settings below from :numref:`Figure %s <fig_swv_settings>`.

.. _fig_swv_settings:

.. figure:: /_static/img/cryowurst/programming/swv_settings.png

    Settings for the SWV ITM Data Console.

3. Press the *Start Trace* button (red circle) to enable logging. When logging is enabled, the button will have a blue highlight around it. Viewing the ITM Data Console window during debugging will show any SWV output from the instrument.

.. _fig_swv_trace:

.. figure:: /_static/img/cryowurst/programming/swv_trace.png

    Output in the SWV ITM Data Console.
