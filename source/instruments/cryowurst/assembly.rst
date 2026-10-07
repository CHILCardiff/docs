Assembly
========

Components
----------
.. image:: /_static/img/cryowurst/assembly/cryowurst_parts.png

.. csv-table:: Common Cryowurst (2026) assembly components.
    :widths: auto
    :header-rows: 1
    :file: assembly_list.csv

.. note::

   **TODO**: Add separate components image for pressure sensor variant.

Tools
-----
There are various tools required to correctly assembly a Cryoegg sensor. The minimum required set of tools are listed below with the part they are used to assembly.

.. csv-table:: Tools for Cryowurst (2026) assembly.
    :widths: auto
    :header-rows: 1

    Tool name,Relevant parts
    M3 socket driver,EC electrodes and PCB standoffs
    Flathead screwdriver,PCB securing screws
    Phillips (crosshead) screwdriver,EC electrodes
    3mm hex (Allen) key,Upper casework screws
    Adjustable spanner,EC electrodes
    Tweezers,Tilt sensor bracket fixings

Assembly steps
--------------

1. Pressure sensor installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2. EC electrodes
^^^^^^^^^^^^^^^^
**Parts required**: (i., j., k., l. b.)

1. Insert the two M6 EC electrode bolts **[i]** so that the head is on the outside (tapered side) of the sensor cap casework.
2. Secure each bolt in place with an M6 nut **[j]** using a screwdriver and adjustable spanner to apply sufficient torque to engage the o-ring in the self sealing screw.
3. Place a nylon spacer **[k]** followed by a steel washer **[l]** on the exposed section of the bolt.
4. Place the sensorboard PCB **[b]** on top of the steel washers and secure it with two more M6 nuts **[j]**.

2. External tilt sensor (*optional*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Parts required**: (c., d., e., f., g., h.)

1. Place the smaller screw **[g]** through the TILT-05 PCB **[c]** and one of the supporting brackets **[d]** so that it matches the alignment shown in (**REF**). Secure in place with **[h]**.
2. Push the connector, cable and free side of **[c]** through the central slot in the motherboard PCB **[a]** so that the supporting bracket is on the same side as the battery holders.
3. Use the second smaller screw **[g]** and nut **[h]** to secure the second bracket **[d]** on the opposite side of the sensor PCB. Make sure the connector cable exists from underneath the bracket.
4. Use the larger screw **[e]** and nut **[f]** to secure **[c]** in place.
5. Insert the connector into J10 (``TILT SENSOR``) on the motherboard PCB.

3. Radio module
^^^^^^^^^^^^^^^
**Parts required**: ()

1. Install the 2.54mm headers **[m]** on jumpers ``J4`` and ``J6`` as shown in (**REF**).
2. Place a small dab of Loctite [REF] on the thread of the antenna connector and then secure the antenna in place.

4. Install motherboard
^^^^^^^^^^^^^^^^^^^^^^

1. Insert the motherboard **[a]** vertically on to the 10-pin connector on the sensorboard **[b]**.
2. Place the 1 to 3 of the Tadiran batteries **[q]** in the battery holders.
3. Place the 9 securing M4 bolts **[p]** into the slots on the sensor cap and secure it in place to main casework.