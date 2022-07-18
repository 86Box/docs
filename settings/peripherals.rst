.. include:: /include.rst

|other_peripherals| Other peripherals
=====================================

The **Other peripherals** page contains settings related to disk drive controllers, memory expansions and other expansion cards.


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

.. list-table::
  :header-rows: 1
  :widths: 1 999

  * - Port
    - Machine types

  * - ``0x10``
    - IBM PCjr

  * - ``0x60``
    - IBM XT

  * - ``0x80``
    - IBM AT, clones and the XT-based Xi 8088

  * - ``0x84``
    - Early Compaq

  * - ``0x190``
    - IBM PS/1 and PS/2 not based on the Micro Channel Architecture

  * - ``0x680``
    - Micro Channel Architecture

.. note:: Some operating systems and applications use port ``0x80`` (which is shared with the POST card on most machines) for other purposes. If you notice the POST code display is flickering and the emulation speed has decreased drastically, try disabling the POST card.
