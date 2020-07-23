Other peripherals
=================

The *Other peripherals* page contains settings related to disk drive controllers, memory expansions and other expansion cards.

SCSI Controller
---------------

SCSI host bus adapter card to emulate. Only cards supported by the machine's expansion buses will be listed.

The *Configure* button opens a new window with settings specific to the selected SCSI card, such as the I/O port and IRQ for ISA cards.

HD Controller
-------------

Hard disk drive controller card to emulate. Only cards supported by the machine's expansion buses will be listed.

MFM, RLL, ESDI and IDE controllers are available. Selecting an IDE controller is not necessary for machines with onboard IDE.

The *Configure* button opens a new window with settings specific to the selected controller card, such as the BIOS option ROM address.

FD Controller
-------------

Floppy disk drive controller card to emulate.

Selecting a controller is not usually necessary. The DTK controllers are useful for adding high-density 1.44 MB floppy support to XT machines.

The BIOS option ROM address used by the selected controller can be configured through the *Settings* button.

Tertiary / Quaternary IDE Controller
------------------------------------

Add a third or fourth (respectively) IDE channel to the emulated machine, through a generic ISA or VLB IDE controller card.

The IRQ used by each controller can be configured through its respective *Settings* button.

.. note:: The tertiary and quaternary channels may require manual configuration of guest operating systems, and may not be bootable. See :doc:`../usage/ideterqua` for more information.

ISABugger
---------

Emulate an **ISABugger** debugging card. Documentation on the card's functionality can be found in the `header comment <https://github.com/86Box/86Box/blob/master/src/device/bugger.c#L1>`_ of ``src/device/bugger.c`` in the 86Box source code.

The following information is displayed on the status bar (from left to right) when the ISABugger is enabled:

* Hexadecimal values corresponding to the left and right 7-segment displays, respectively.
* Green LED bank, from the most significant to the least significant bit: **G** if the LED is lit, **g** if it's not lit.
* Red LED bank, from the most significant to the least significant bit: **R** if the LED is lit, **r** if it's not lit.

POST card
---------

Emulate a diagnostic POST card, which displays I/O port 80h POST code values on the status bar. The leftmost hexadecimal value is the most recent POST code reported, while the rightmost value is the second most recent code, like on a real dual-display POST card. A value of ``--`` indicates that no POST code has been reported yet.

Some machines use a different I/O port for POST codes: port 0680h on Micro Channel Architecture-based machines, or port 90h on non-MCA-based IBM PS/2 machines.


.. note:: Some guest operating systems (such as Linux before kernel 3.0) rely heavily on the first DMA extra page register, which is shared with the POST card. If you notice the POST code display is flickering and the emulation speed has decreased drastically, try disabling the POST card.

ISA RTC
-------

Emulate an ISA real-time clock card, for machines without an integrated real-time clock.

The I/O port and/or IRQ used by the selected controller can be configured through the *Settings* button.

ISA Memory Expansion
--------------------

Add up to four ISA-based memory expansion cards, for machines which support memory expansion through the ISA bus.

The memory start address and size for each expansion card can be configured through its respective *Settings* button.
