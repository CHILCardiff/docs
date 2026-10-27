Packet decoders
===============

In the context of CHIL instrumentation, the term "packet decoder" is used interchangeably to refer to the functionality of:

* Decoding packets **sent over a USB connection** from a CHIL datalogger so they can be interpreted in real=time.
* **Parsing files** stored on CHIL dataloggers to convert the data into a usable format.

The 2023 dataloggers were designed so that they only operate with one type of instrument (i.e. Cryoegg *or* Cryowurst) at a time. This resulted in two sets of packet decoder programs being required, one for each instrument type.

While these programs are capable of decoding the packets sent over a USB connection in real=time, they are not designed to interpret the files that are saved on the dataloggers. Cryodecoder was introduced in 2026 to provide a piece of software capable of parsing packets in an instrument agnostic manner, in addition to decoding of the files stored on the dataloggers. The table below compares functionality between the different pieces of software:

.. list-table:: Functionality of the different CHIL packet decoders
    :widths: auto
    :header-rows: 1

    * - Packet decoder
      - Supported instruments
      - USB (serial) decoding
      - USB logging
      - File decoding
      - Cloudloop (satellite) decoding
    * - :ref:`Cryodecoder <cryodecoder_packet_decoder>`
      - Cryoegg (2023), Cryowurst (2023), Cryoegg (2026), Cryowurst (2026)
      - **Yes**
      - **Yes**
      - **Yes**
      - **Yes** 
    * - :ref:`Cryoegg Packet Decoder <cryoegg_packet_decoder>`
      - Cryoegg (2023)
      - **Yes**
      - **Yes**
      - No
      - No
    * - :ref:`Cryowurst Packet Decoder <cryowurst_packet_decoder>`
      - Cryowurst (2023)
      - **Yes**
      - **Yes**
      - No
      - No     

Cryodecoder is backwards compatible with old dataloggers and should be used preferentially, however there are occasions where the legacy 2023 versions may be required. 

.. toctree::
    :hidden:
    
    Cryodecoder (2026) <packet_decoder/cryodecoder>
    Cryoegg decoder (2023) <packet_decoder/cryoegg_2023>
    Cryowurst decoder (2023) <packet_decoder/cryowurst_2023>