Datalogger
==========

Portable
--------

Tripod
------

Datalogger servicing protocol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#.  Take photo of site
#.  Log time of arrival (UTC)
#.  Power off logger
#.  Remove micro SD card
#.  Copy to PC 
#.  If sufficient space, leave on card and add servicing note to README (date, time UTC, any notable conditions, who did servicing).
#.  Return SD card to logger

#.  Installing LVD:

    a.  Disconnect wires from power and ground on the PCB
    b.  Connect LVD load wire (blue) to power on PCB, with black ferrule on the end.
    c.  Connect red power wire from pelicase (the one which was originally connected to the PCB power) to LVD power wire (red), using blue butt splice, and crimp.
    d.  Connect black ground wire from pelicase (the one which was originally connected to PCB ground) to LVD ground (black), using a yellow butt splice. Don't crimp yet!
    e.  Using another black wire, connect between the yellow butt splice and PCB ground, using a black ferrule (there will be two black wires coming out of one side of the butt splice). Crimp. See instrumentation_pics.docx for wiring diagram

#.  Power on logger and connect to Adalogger board with microUSB
#.  Connect serial monitor to relevant COM port at 19200 baud
#.  Reset Adalogger (small tactile switch on PCB)
#.  Wait for datalogger status readout. Record pressure, temperature and solar panel voltage (raw and V).
#.  Remove USB 
#.  Take photo of inside of casework
#.  Close lid
#.  Reposition solar panels if not facing south
#.  Take photo of installation


.. figure:: /_static/img/deployment/datalogger_servicing_protocol.png

    Example servicing protocol for the CHIL datalogger.