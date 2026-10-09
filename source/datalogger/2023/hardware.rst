Hardware
========

Equipment
~~~~~~~~~

* CHIL datalogger PCB (old version, with modboard and jumpers)
* screws to attach PB to baseplate
* RockBLOCK+ satellite modem
* thumbscrews for attaching modem
* multimeter
* pink loctite

Assembly

Before going into the field, it's a good idea to set up and test the system in advance, somewhere where you have access to the internet and potentially a workshop for last-minute tweaks.

Testing electrical system 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Connect batteries to the Peli case, and power on by switching the battery breakers on
* Check (using multimeter across the power (red) and ground (black) wires) that voltage is between 12 and 15V. Check that red is in fact positive and black negative!
* Connect the solar panels, expose them to light, and check that the battery voltage increases (slightly).

Installing the PCB
~~~~~~~~~~~~~~~~~~~~

Refer to :numref:`fig-pcb-wiring-old` 

* Note the older PCBs may have a modboard attached. This should be connected with jumpers to JP3.
* connect 12V power and ground to the terminal blocks as shown
* Screw PCB into baseplate undeneath satellite modem mount (:numref:`fig-pelicase-assembled-old`)

.. _fig-pcb-wiring-old:

.. figure:: datalogger_pcb_power_ground.png
   :align: center
   :width: 60%

   Connecting PCB power and ground

.. _fig-pelicase-assembled-old:

.. figure:: datalogger_pic_yukon_2024.jpg
   :align: center
   :width: 60%

   Inside of pelicase after assembly. Note the PCB is underneath the RockBLOCK modem! 

Installing RockBLOCK modem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Cut and strip RockBLOCK modem cable to suitable length (around 150mm). 
* Mount the RockBLOCK to the bracket using the two thumbscrews. It only mounts with two screws despite having four mounting points. Use pink Loctite to secure them so that they don't rattle out.

Wire the RockBLOCK to the PCB as shown in figure x. Wire colours are as follows:

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