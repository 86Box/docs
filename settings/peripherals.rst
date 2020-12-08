Other peripherals
=================

The *Other peripherals* page contains settings related to disk drive controllers, memory expansions and other expansion cards.


ISA RTC
-------

Emulate an ISA real-time clock card, for machines without an integrated real-time clock.

The I/O port and/or IRQ used by the selected controller can be configured through the *Settings* button.

ISA Memory Expansion
--------------------

Add up to four ISA-based memory expansion cards, for machines which support memory expansion through the ISA bus.

The memory start address and size for each expansion card can be configured through its respective *Settings* button.

ISABugger
---------

Emulate an **ISABugger** debugging interface card, equipped with two hexadecimal displays and two LED banks, all controlled by the emulated machine. See :doc:`../hardware/isabugger` for documentation on the card's features.

POST card
---------

Emulate a diagnostic POST card, which displays POST code values issued by the emulated machine's BIOS on the status bar. See :ref:`Status bar: POST card <usage/statusbar:POST card>` for more information.

The POST card will automatically use the correct diagnostic I/O port for the emulated machine:

* Port 10h on the IBM PCjr;
* Port 60h on the IBM XT;
* Port 80h on the IBM AT, clones and the XT-based Xi 8088;
* Port 84h on early Compaq machines;
* Port 0190h on IBM PS/1 and PS/2 machines not based on the Micro Channel Architecture;
* Port 0680h on Micro Channel Architecture machines.

.. note:: Some guest operating systems and applications use port 80h (which is shared with the POST card on most machines) for other purposes. If you notice the POST code display is flickering and the emulation speed has decreased drastically, try disabling the POST card.