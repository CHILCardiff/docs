Hardware
========

Equipment
~~~~~~~~~

* CHIL datalogger PCB (2026 version)
* plastic adhesive spacers to mount PCB
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

.. _fig-pelicase-nopcb:

.. figure:: pelicase_nopcb_2026.jpg
   :align: center
   :width: 60%

   Inside of pelicase before assembly

.. _fig-pelicase-assembled:

.. figure:: pelicase_assembled_2026.jpg
   :align: center
   :width: 60%

   Inside of pelicase after assembly

Installing PCB
~~~~~~~~~~~~~~~~

Refer to :numref:`fig-pelicase-nopcb` and :numref:`fig-pelicase-assembled`:

* Connect power input (12V and Ground) to chocbloc in upper right corner of PCB 
* Connect RF inputs to PCB (2 x SMA connectors, make sure they're tight)
* Fix PCB to the metal base of the pelicase using spacers

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


.. _fig-datalogger_rockblock_2026:

.. figure:: datalogger_pcb_rockblock.png
   :align: center
   :width: 40%

   RockBLOCK cable wired into datalogger PCB