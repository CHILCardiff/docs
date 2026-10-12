Firmware and programming
========================

Firmware
--------
The latest source code for the Cryoegg firmware is stored on GitHub here: https://github.com/CHILCardiff/cryoegg-2026/. At present, we do not provide pre-compiled ``.elf`` files to program the instrument using *STM32CubeProgrammer* or similar binary flashing tools.

You should already have downloaded the latest version of the firmware for Cryoegg when :ref:`setting up your CHIL development environment <devenv>`.

Programming using STM32CubeIDE
------------------------------
The following section describes the equipment required and necessary steps to program the Cryoegg sensor. Programming the sensor allows the user to change the measurement interval, number of deployment packets and radio packet version used.

Equipment
^^^^^^^^^

To program the Cryoegg, you will need the items shown below in addition to an assembled Cryoegg motherboard, power switch and batteries.

a. STMicroelectronics `Nucleo-L476RG`_ development board.
b. USB-A to Micro-USB or Mini-USB cable (check board type).
c. 6-way 2.54mm header cable.

.. _Nucleo-L476RG: https://www.st.com/en/evaluation-tools/nucleo-l476rg.html

Steps
^^^^^

.. _fig_ceprogramming_cryoegg:

.. figure:: /_static/img/cryoegg/programming.png  

    Connecting the Cryoegg (2026) to the STLINK-V3 programmer.

1. Connect the Nucleo development board to to your PC using the USB cable.
2. Connect the 6-way 2.54mm header cable to the Nucleo development board :numref:`Figure %s.1 <fig_ceprogramming_cryoegg>`.
3. Connect the 6-way 2.54mm header cable to the Cryoegg :numref:`Figure %s.2 <fig_ceprogramming_cryoegg>`.

.. important:: 

    Ensure that **P1** on the Nulceo development board is connected to **P1** (``Vdd``) on the Cryoegg. You can use the colours of the cable to check this.

4. Connect a power switch (``POWER_EN``, :numref:`Figure %s.3 <fig_ceprogramming_cryoegg>`). You are now ready to program the Cryoegg.

The following steps assume you have set up your the CHIL development environment. If not, follow the :ref:`setup instructions <devenv>` and then return to this step when completed.

5. Open STM32CubeIDE and ensure that the ``cryoegg-2025`` and ``chillib`` projects are open (check by right-clicking in the Project Explorer window).

.. _fig_ce_main_c_cryoegg:

.. figure:: /_static/img/cryoegg/programming/main_c_programming_settings.png

    STM32CubeIDE development environment and Cryoegg configuration settings.

6. Find ``Core/Src/main.c`` in the Project Explorer and open the file. Scroll down to the ``int main(void)`` function (Line 116 at time of writing). This section defines the deployment behaviour of the instrument. If you wish to modify the behaviour, update these values in ``main.c``. Each value is described below in the table below:

.. _table_cryoegg_variables:

.. csv-table::
    :widths: auto
    :header-rows: 1

    Varible name,Description,Units,Default value
    ``deployment_sleep_period_s``,The time period in seconds to sleep between each deployment measurement.,seconds,``27``
    ``max_deployment_packets``,The total number of packets to send before entering long term deployment mode (max. value of 255).,N/A,``240``
    ``long_term_sleep_period_s``,The time period in seconds to sleep between each measurement.,seconds,``1797``

.. note::
    
    When defining sleep periods, account for the time period the instrument takes to make each measurement by subtracting 3 seconds from the desired value. For example, to have a deployment interval of 30 seconds, set ``deployment_sleep_period_s = 27``. 

7. Open the *Debug Configurations* dialog box from ``Run > Debug Configurations`` in the top menu bar.

.. _fig_cedebug_conf_cryoegg:

.. figure:: /_static/img/cryoegg/programming/debug_configurations.png

    Debug Configuration settings to program the Cryoegg using STM32CubeIDE.

8. If there is no configuration available under *STM32 C/C++ Application* and ensure that the Debugger settings match those in :numref:`Figure %s <fig_cedebug_conf_cryoegg>`.
9. When you are ready to program the Cryoegg, press the *Debug* button in the *Debug Configurations* dialog box.

.. _fig_cehalt_after_debug:

.. figure:: /_static/img/cryoegg/programming/halt_after_debug.png

    Code execution paused in debug mode after successful programing of Cryoegg.

10. 
    If you succesfully program the Cryoegg, you should see output in the Console which matches :numref:`Figure %s <fig_cehalt_after_debug>`. The programmer has halted execution of the program at the start of the main function. At this point, you can choose to:

    a. Disconnect the programmer and power from the Cryoegg and test it at a later date.
    b. Continue to run the program and check sensor outputs (see Step 11) by pressing the resume icon (pink arrow in :numref:`Figure %s <fig_cehalt_after_debug>`).
11. Open the Serial Wire Viewer Output window to check the instrument is working. If you have not previously configured the Serial Wire Viewer, follow the instructions :ref:`here <serial_wire_viewer_setup>`.

.. figure:: /_static/img/cryoegg/programming/swv_trace.png

    Output from Cryoegg in the SWV ITM Data Console.

You have now succesfully programmed the Cryoegg for deployment. We recommend powering off the instrument and restarting it without the programming cable inserted before deployment.

.. tip::

    See :ref:`here <tip_deployment_packets>` for how to manually reset or adjust the value of ``deployment_packets``.

The next sections describe the CHIL dataloggers which can be used to validate that the instruments are performing correctly before deployment.