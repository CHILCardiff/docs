Hardware
========

Equipment
---------

* Datalogger PCB 2023 version with 3V3 modboard (See :numref:`Figure %s <fig_datalogger_pcb_2023>` and :numref:`Figure %s <fig-pcb-wiring-old>`).
* M4 screws to attach PB to baseplate.
* `RockBLOCK+`_ satellite modem.
* Thumbscrews for attaching modem.
* Digital multimeter.
* Loctite 222 (pink).

.. _RockBLOCK+: https://www.groundcontrol.com/product/rockblock-plus-waterproof-satellite-iot-device/

Datalogger PCB
^^^^^^^^^^^^^^
:numref:`Figure %s <fig_datalogger_pcb_2023>` shows annotated components of the 2023 datalogger PCB.

.. _fig_datalogger_pcb_2023:

.. figure:: /_static/img/datalogger/2023/pcb_annotated.png

   Annotated components of the 2023 datalogger PCB.

1.  
    **Adafruit Feather M0 Adalogger** microcontroller.

    a.  Micro USB connector used for firmware programming.
    b.  MicroSD card holder for data storage.
    c.  Reset button used to restart the datalogger.

2.  **12V power** connector.
3.  **Iridium modem** connector. See :ref:`below <fig_rockblock_wiring>` for wiring instructions.
4.  **Reset header**. Alternative way of restarting the datalogger by short-circuiting **both** pins (i.e. with a flathead screwdriver).
5.  **Radio modem** for channel 1.

    a. Tx and Rx headers used to program the radio modem.

6.  **Radio modem** for channel 2.

    a. Tx and Rx headers used to program the radio modem.


Assembly
--------

Before going into the field, it's a good idea to set up and test the system in advance, somewhere where you have access to the internet and potentially a workshop for last-minute tweaks. Assemble the datalogger PCB, modem and pelicase before mounting it on the datalogger tripod.

Testing electrical system 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Connect batteries to the Peli case, and power on by switching the battery breakers on
* Check (using multimeter across the power (red) and ground (black) wires) that voltage is between 12 and 15V. Check that red is in fact positive and black negative!
* Connect the solar panels, expose them to light, and check that the battery voltage increases (slightly).

Installing the PCB
^^^^^^^^^^^^^^^^^^^^

.. note::

    It is recommended to install the PCB **before** assembling the mechanical structure of the datalogger as it is hard to reach the components inside when elevated above the ground.

Refer to :numref:`fig-pcb-wiring-old` 

* Note the older PCBs may have a modboard attached. This should be connected with jumpers to JP3.
* Connect 12V power and ground to the terminal blocks as shown.
* Screw PCB into baseplate undeneath satellite modem mount (:numref:`fig-pelicase-assembled-old`).

.. _fig-pcb-wiring-old:

.. figure:: datalogger_pcb_power_ground.png
   :align: center
   :width: 60%

   Connecting PCB power and ground.

.. _fig_rockblock_wiring:

Connecting antenna cables
^^^^^^^^^^^^^^^^^^^^^^^^^

Use two N-type (pin) to SMA (pin) cables to connect the external antenna connectors (**[3.]** in :numref:`Figure %s <fig-pelicase-assembled-old>`) to the datalogger PCB using the connectors next to the radio modem.

.. important::

    Check and label which radio channel each external connector is assigned to before installing RockBLOCK+ modem.

Installing RockBLOCK+ modem
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    The Tx and Rx connector colours below are **correct** for the CHIL datalogger but are swapped from the descriptions used on the GroundControl `documentation <https://docs.groundcontrol.com/iot/rockblock/specification/connectors-wiring#rockblock-plus>`__.

* Cut and strip RockBLOCK modem cable to suitable length (around 150mm). 
* Mount the RockBLOCK to the bracket using the two thumbscrews. It only mounts with two screws despite having four mounting points. Use pink Loctite to secure them so that they don't rattle out.

Wire the RockBLOCK to the PCB as shown in :numref:`Figure %s <_fig-datalogger_rockblock>`. Wire colours are as follows:

.. raw:: html

   <p>
   <span style="color: #008000;"><strong>Green</strong></span> = Alert<br>
   <span style="color: #666666;"><strong>White</strong></span> = Available<br>
   <span style="color: #d63384;"><strong>Pink</strong></span> = On/Off<br>
   <span style="color: #b88600;"><strong>Yellow</strong></span> = Tx<br>
   <span style="color: #0066cc;"><strong>Blue</strong></span> = Rx<br>
   <strong>Black</strong> = Ground<br>
   <span style="color: #d00000;"><strong>Red</strong></span> = V+
   </p>


.. _fig-datalogger_rockblock:

.. figure:: datalogger_pcb_rockblock.png
   :align: center
   :width: 40%

   RockBLOCK cable wired into datalogger PCB

Datalogger pelicase
^^^^^^^^^^^^^^^^^^^

The datalogger pelicase is used in the tripod version of the CHIL datalogger. Once the PCB is installed and modem are installed, the inside of the datalogger pelicase should look like :numref:`Figure %s <fig-pelicase-assembled-old>`. Before connecting batteries or solar panel, ensure that the jumper switches (labelled in the bottom center) are set to **OFF** for the mechanical assembly.

.. _fig-pelicase-assembled-old:

.. figure:: /_static/img/datalogger/2023/datalogger_2023_annotated.png
   :width: 100%

   Inside of the 2023 datalogger pelicase after assembly. Note the PCB **[1.]** is underneath the RockBLOCK modem! 

**Datalogger Pelicase components**:

1.  Datalogger PCB (2023).
2.  RockBLOCK+ Iridium modem.
3.  External antenna connectors.
4.  External battery connectors.
5.  External solar panel connector.
6.  SunKeeper-6 solar regulator.
7.  Power switches for batteries and solar panels.