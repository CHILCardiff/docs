Instruments
===========

The CHIL group is reponsible for the development of wireless instruments for studying glacial hydrology and ice dynamics, including:

* :doc:`Cryoegg <cryoegg/index>`: a spherical temperature, pressure and electrical conductivity sensor for englacial and subglacial hydrology studies.
* :doc:`Cryowurst <cryowurst/index>`: a cylindrical temperature, pressure, electrical conductivity and tilt sensor for borehole applications.

This documentation describes the **capabilities** of each instrument, how to **assemble** them, **program** them with the latest firmware and **deploy** them in the field.

.. toctree::
   :maxdepth: 2
   :caption: Instruments:

   cryoegg/index
   cryowurst/index

Overview
--------
Cryoegg and Cryowurst are based on the same electronic design and therefore share a lot of the same basic functionality and sensors. The table below summarises the features of the two instruments:

.. list-table:: Instrument summary
   :widths: auto
   :header-rows: 1

   * - Name
     - Cryoegg
     - Cryowurst
   * - Microcontroller
     - STM32L433
     - STM32L433
   * - Radio
     - Radiocrafts RC1701HP-MBUS4
     - Radiocrafts RC1701HP-MBUS4
   * - Temperature
     - ✔ (TMP117)
     - ✔ (TMP117)
   * - Conductivity
     - ✔ 
     - ✔ 
   * - Pressure
     - ✔ (Keller 7LD)
     - ✔ (Keller 7LD, *optional*)
   * - Orientation
     - ✔ (LSM303AGR)
     - ✔ (LSM303AGR, CTi Tilt-05)
   * - Dimensions
     - 120mm dia. sphere.
     - 80mm dia. x 270mm long cylinder.
   * - Battery capacity
     - 3.9 V, ? Ah
     - 3.9 V, 2.1 to 6.3 Ah

The instruments are designed around an `STM32L433`_ microcontroller and use an `RC1701HP-MBUS4`_ radio modem to provide a one-way wireless communications link from the sensor to receivers on the surface.

.. _STM32L433: https://www.st.com/en/microcontrollers-microprocessors/stm32l433rc.html

.. _RC1701HP-MBUS4: https://radiocrafts.com/products/wirelessmbus/#wireless-mbus-products

Sensors
-------

Conductivity
^^^^^^^^^^^^
The CHIL instruments use an in-house design for the electrical conductivity sensor which makes use of the internal voltage buffer and analogue-to-digital converter of the STM32L433.

The resolution of the sensor is non-linear, and is proportional to the square of the measured conductivity. Interpretation of the conductivity requires careful pre-calibration, described in the Cryoegg :doc:`deployment <cryoegg/deployment>` documentation.

Pressure
^^^^^^^^
Pressure sensors in the Cryoegg and Cryowurst are manufactured by `Keller`_ and are either the `Series 7LD`_ (standard) or `Series 7LHPD`_ (for high pressure applications). They are accurate to 0.15% of the full scale pressure. The Keller sensors communicate with the STM32 microcontroller via a shared |I2C| bus.

.. list-table:: Keller pressure sensors in CHIL instruments
   :widths: auto
   :header-rows: 1
   
   * - Pressure sensor
     - Range (bar)
     - Applications
   * - 7LD
     - 0...3
     - Surface hydrology
   * - 7LD
     - 0...30
     - Englacial and subglacial hydrology
   * - 7LD
     - 0...100
     - Englacial and subglacial hydrology
   * - 7LHPD
     - 0...250
     - Borehole and subglacial hydrology

.. _`Series 7LD`: https://keller-pressure.com/en/products/pressure-transmitters/oem-pressure-transmitters/series-7ld
.. _`Series 7LHPD`: https://keller-pressure.com/en/products/pressure-transmitters/oem-high-pressure-transmitters/series-7lhpd
.. _Keller: https://keller-pressure.com

.. |I2C| replace:: I\ :sup:`2`\ C

Temperature
^^^^^^^^^^^
The CHIL instruments use a Texas Instruments `TMP117`_ digital temperature sensor with an accuracy of ±0.15°C and resolution of 0.0078°C.

The Keller pressure sensors provide an auxiliary temperature sensor used to calibrate the pressure value which is accurate to 2°C with a 0.05°C resolution.

.. _TMP117: https://www.ti.com/product/TMP117

Orientation
^^^^^^^^^^^
An `LSM303AGR`_ e-compass sensor from STMicroelectronics is used in the Cryoegg and Cryowurst to provide an orientation sensing capability by reporting 3-axis accelerometer and magnetometer values.

The Cryowurst also features a CTi `TILT-05`_ inclinometer which incorporates a 3-axis accelerometer and on-board controller which provide pitch and roll measurements with a resolution of 0.1°.

.. _LSM303AGR: https://www.st.com/en/mems-and-sensors/lsm303agr.html
.. _TILT-05: https://ctisensors.com/products/tilt-05-oem-inclinometer/
