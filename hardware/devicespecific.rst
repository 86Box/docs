Device-specific notes
======================

This |page| contains important notes related to various devices emulated by 86Box.

----

|display| Display
-----------------

.. rubric:: ATI Mach64GX

* After creating an emulated machine or :ref:`wiping NVRAM <usage/manager:Machine list>`, the card must be configured using the ``INSTALL.EXE`` DOS utility included with Windows driver packages, otherwise the drivers for many operating systems will exhibit issues.

.. rubric:: Cirrus Logic GD5420

* The driver included with Windows NT 3.1 does not properly support the extra video modes that are unlocked when the card is configured with 1 MB of video memory.

|network| Network
-----------------

.. rubric:: Xircom Pocket Ethernet III

* The driver included with Windows 98 may fail to load with an error message due to a parallel port detection bug. Fix it by selecting an I/O address instead of a port name: on the *Network* control panel, select the *Xircom Pocket Ethernet III*, click *Properties*, go to the *Advanced* tab and change *LPT Port or I/O Address* to ``378`` for LPT1, ``278`` for LPT2 or ``3BC`` for LPT3.

|sound| Sound
-------------

.. rubric:: HP Multimedia Pro 16V-A

* The **ASUS PVI-486SP3** machine hangs during POST at the *Initialize Plug and Play Cards* stage when this card is installed. This is a bug in that machine's BIOS, which gets stuck in an infinite loop on the zero-length I/O ranges reported by the card's disabled IDE CD-ROM device; a real board with this card is expected to behave the same way. Other machines with Plug and Play BIOSes are not known to be affected.
