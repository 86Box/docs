Extended HDI (HDX)
==================

A derivative of the *Japanese FDI* disk image format, with a more compact header and support for images larger than 4 GB.

Specification
-------------

All offsets are in hexadecimal. The ``[Translation]`` values are for future use.

.. code-block:: none
 
 00000000: Signature (59 54 44 44 20 A8 78 D7 / "YTDD " A8 78 D7)
 00000008: Full size of the data in bytes (64-bit)
 00000010: Sector size in bytes (32-bit)
 00000014: Sectors per cylinder (32-bit)
 00000018: Heads per cylinder (32-bit)
 0000001C: Cylinders (32-bit)
 00000020: [Translation] Sectors per cylinder (32-bit)
 00000024: [Translation] Heads per cylinder (32-bit)
 00000028: Raw data (size set in offset 00000008)
