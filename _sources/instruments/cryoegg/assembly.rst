Assembly
========

Components
----------
.. image:: /_static/img/cryoegg/assembly/cryoegg_parts.png

.. note::

    The list below is not a comprehensive bill of materials (BOM) for Cryoegg and instead is intended to be used during the instrument assembly process, please refer to the `GitHub repository <https://github.com/chilcardiff/cryoegg-2025>`__ for the complete BOM.

.. csv-table:: Cryoegg (2025) assembly components.
    :widths: auto
    :header-rows: 1
    :file: assembly_list.csv

Tools 
-----
There are various tools required to correctly assembly a Cryoegg sensor. The minimum required set of tools are listed below with the part they are used to assembly.

.. csv-table:: Tools for Cryoegg (2025) assembly.
    :widths: auto
    :header-rows: 1

    Tool name,Relevant parts
    M3 socket driver,EC electrodes and PCB standoffs
    Flathead screwdriver,PCB securing screws
    Phillips (crosshead) screwdriver,EC electrodes
    2.5mm hex (Allen) key,Pressure flange screws
    3mm hex (Allen) key,Upper casework screws
    Loctite 242,Antenna and eyelet.

Assembly steps
--------------

1. Pressure sensor
^^^^^^^^^^^^^^^^^^
**Parts required**: (n., o., p.)

.. figure:: /_static/img/cryoegg/assembly/pressure_sensor.png

    Installation steps for the Keller PA-7L(HP)D pressure sensors in the lower Cryoegg shell.

1. Insert the pressure sensor assembly (with QWIIC tail) **[p.]** into the slot at the bottom of the lower Cryoegg shell. If necessary, use a dab of O-ring grease around the circumference of the sensor and the flange **[o.]** to insert the sensor.

.. warning::
    It is not possible to remove the pressure sensor once inserted without risk of damaging it.

2. Push the flange **[o.]** over the top of the pressure sensor with the flat side facing away from the casework. Carefully rotate the flange to align the holes with the those in the casework.
3. Tighten the pressure sensor in place with four M4x8mm screws **[m.]**. Tighten opposite sides of the flange first, rather than working around the screws in a circular manner.
4. The pressure sensor is now installed.

2. EC electrodes
^^^^^^^^^^^^^^^^
**Parts required**: (f., g., h., i.)

.. figure:: /_static/img/cryoegg/assembly/ec_electrodes.png

    Installation steps for the EC electrodes in the lower Cryoegg shell.

1. Identify the self-sealing EC bolts **[f.]**, shakeproof washers **[h.]**, ring terminals and tail **[i.]** and M3 nuts **[g.]**. 
2. Insert the EC bolts so that the screw cap is on the outside of the shell.
3. On the inside of the shell place the shakeproof washers, ring terminals and nuts on the other side of the bolts. Tighten these in place using an screwdriver and adjustable spanner or socket drive.
4. Install the anti-vibration PCB mounts **[l.]** on the bottom of the shell. 

3. PCB installation
^^^^^^^^^^^^^^^^^^^
**Parts required**: (a., b., j., k., l.)

.. figure:: /_static/img/cryoegg/assembly/pcb_installation.png

    Installation steps for the Cryoegg PCBs.

1.
    Connect the lower PCB **[b.]** to the loose sensor tails:
    a. Pressure sensor.
    b. EC sensor.
2.  To prepare the lower PCB supports:
    a. Make three pairs of the 8mm nylon PCB standoffs **[k.]**. 
    b. Snip the exposed thread of the standoffs to 6mm length.
3. Secure the lower PCB in place with the nylon standoffs.
4. Mate the upper PCB **[a.]** with the lower PCB and secure it in place with three M3x6mm screws **[j.]**.

4. Radio module and fixings
^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Parts required**: (d., q., c., e., m.)

.. figure:: /_static/img/cryoegg/assembly/radio_oring.png

    Installation steps radio module and fixings.

1. 
    a. Install the jumpers **[d.]** in the positions shown on ``J4`` and ``J6``. 
    b. Place a dab of Loctite 242 on the antenna connector thread and install the antenna by screwing into place **[q.]**.
2.  Place the O-ring **[c.]** in the groove of the lower shell.
3.  *(Optional)* If using the lifting eye **[e.]**, place a dab of Loctite 242 on the metal thread and screw it into place in the upper casework.
4.  Install the eight M4x16mm socket cap screws **[m.]** around the upper casework.