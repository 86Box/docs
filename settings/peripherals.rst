|other_peripherals| Other peripherals
=====================================

The **Other peripherals** page contains settings related to disk drive controllers, memory expansions and other expansion cards.

|general_other_peripherals| General
-----------------------------------

ISA RTC
^^^^^^^

Emulate an ISA real-time clock card, for machines without an integrated real-time clock. Click |clear| to search for cards by name.

The I/O port and/or IRQ used by the selected controller can be configured through the *Configure* button.

ISABugger
^^^^^^^^^

Emulate an **ISABugger** debugging interface card, equipped with two hexadecimal displays and two LED banks, all controlled by the emulated machine. See :doc:`../hardware/isabugger` for documentation on the card's features.

POST card
^^^^^^^^^

Emulate a diagnostic POST card, which displays POST code values issued by the emulated machine's BIOS on the status bar. See :ref:`Status bar: POST card <usage/statusbar:POST card>` for more information.

The POST card will automatically use the correct diagnostic I/O ports for the emulated machine:

.. list-table::
  :header-rows: 1
  :widths: 80 615

  * - Port
    - Machine types

  * - ``0x10 0x11 0x12``
    - IBM PCjr

  * - ``0x60``
    - IBM XT

  * - ``0x80``
    - IBM AT, clones and the XT-based Xi 8088

  * - ``0x84``
    - Early Compaq

  * - ``0xE0 0xE4``
    - Dell (4-character text display after the port ``0x80`` hex display)

  * - ``0x190``
    - IBM PS/1 and PS/2 not based on the Micro Channel Architecture

  * - ``0x378``
    - Olivetti

  * - ``0x680``
    - Micro Channel Architecture

  * - ``0x5080``
    - ASUS ISA-486C

.. note:: Some operating systems and applications use port ``0x80`` (which is shared with the POST card on most machines) for other purposes. If you notice the POST code display is flickering and the emulation speed has decreased drastically, try disabling the POST card.

86Box Unit Tester
^^^^^^^^^^^^^^^^^

Emulate a special device for software in the emulated machine to control 86Box for testing purposes. The *Configure* button provides settings specific to this device.

.. note:: Documentation to be concluded.

Novell NetWare 2.x Key Card
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Emulate the hardware license key card required by Novell NetWare 2.0a among other versions.

The serial number displayed in software can be configured through the *Configure* button.

|isa_memory| ISA Memory Expansion
---------------------------------

Add up to four ISA-based memory expansion cards, for machines which support memory expansion through the ISA bus. Click |clear| to search for cards by name.

The memory start address and size for each card can be configured through its respective *Configure* button.

|isa_rom| ISA ROM Cards
-----------------------

Add up to four ROM expansion cards, which can load a predefined or custom BIOS option ROM directly into the emulated machine. Click |clear| to search for cards by name.

The **Vision Systems LBA Enhancer** ROM can help work around the :ref:`hard disk size limits <hardware/diskimages:Hard disk size limits>` on many older machines. Hard disks up to 8055 MB (16367 cylinders, 16 heads, 63 sectors) in size are supported; they must be manually configured to **8 cylinders, 8 heads and 8 sectors** on the machine's BIOS setup utility for the Enhancer to handle them.

The base address for each card, as well as the ROM file and size for a generic card, can be configured through its respective *Configure* button.
