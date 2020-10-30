Other peripherals
=================

The *Other peripherals* page contains settings related to disk drive controllers, memory expansions and other expansion cards.

SCSI Controller
---------------

SCSI host bus adapter card to emulate. Only cards supported by the machine's expansion buses will be listed.

The *Configure* button opens a new window with settings specific to the selected SCSI card, such as the I/O port and IRQ for ISA cards.

HD Controller
-------------

Hard disk drive controller card to emulate. Only cards supported by the machine's expansion buses will be listed. MFM, RLL, ESDI and IDE controllers are available. Selecting an IDE controller is not required for machines with onboard IDE.

The *Configure* button opens a new window with settings specific to the selected controller card, such as the BIOS option ROM address.

FD Controller
-------------

Floppy disk drive controller card to emulate. Selecting a controller is not required, unless you wish to use the DTK controllers for adding high-density 1.44M floppy support to XT machines.

The BIOS option ROM address used by the selected controller can be configured through the *Settings* button.

Tertiary / Quaternary IDE Controller
------------------------------------

Add a third or fourth (respectively) IDE channel to the emulated machine, through a generic ISA or VLB IDE controller card.

The IRQ used by each controller can be configured through its respective *Settings* button.

.. note:: The tertiary and quaternary controllers are not Plug and Play compliant; they may require manual configuration of emulated operating systems, and may not be bootable. See :doc:`../hardware/ideterqua` for more information.

ISABugger
---------

Emulate an **ISABugger** debugging interface card, equipped with two hexadecimal displays and two LED banks, all controlled by the emulated machine. See :doc:`../hardware/isabugger` for documentation on the card's features.

POST card
---------

Emulate a diagnostic POST card, which displays POST code values issued by the emulated machine's BIOS on the status bar. See :ref:`Status bar: POST card <usage/statusbar:POST card>` for more information.

The POST card will automatically use the correct diagnostic I/O port for the emulated machine:

* Port 60h on the IBM XT;
* Port 80h on the IBM AT, clones and the XT-based Xi 8088;
* Port 84h on early Compaq machines;
* Port 0190h on IBM PS/1 and PS/2 machines not based on the Micro Channel Architecture;
* Port 0680h on Micro Channel Architecture machines.

.. note:: Some guest operating systems (such as Linux before kernel 3.0) and applications use port 80h - which is shared with the POST card - for other purposes. If you notice the POST code display is flickering and the emulation speed has decreased drastically, try disabling the POST card.


ISA RTC
-------

Emulate an ISA real-time clock card, for machines without an integrated real-time clock.

The I/O port and/or IRQ used by the selected controller can be configured through the *Settings* button.

ISA Memory Expansion
--------------------

Add up to four ISA-based memory expansion cards, for machines which support memory expansion through the ISA bus.

The memory start address and size for each expansion card can be configured through its respective *Settings* button.
