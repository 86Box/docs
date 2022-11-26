Machine-specific notes
======================

This page contains important notes related to specific machine models emulated by 86Box.

----

8088
----

.. _t1000:
.. rubric:: Toshiba T1000

The function keys can be accessed by holding Right Alt or Right Ctrl:

* ``Right Alt/Ctrl + Num Lock``: Show/hide numeric keypad overlay
* ``Right Alt/Ctrl + Right``: Change internal display font
* ``Right Alt/Ctrl + Home``: Use internal display
* ``Right Alt/Ctrl + End``: Use external display

8086
----

.. _m24:
.. rubric:: Olivetti M21/24/24SP

The special keys on Olivetti keyboards are mapped as such:

* ``Page Up``: CLEAR
* ``Page Down``: BREAK
* ``Print Screen``: SCR PRT
* ``Menu``: HELP
* ``Left Windows``: 00
* ``Insert``: F13
* ``Home``: F14
* ``Del``: F15
* ``End``: F16
* ``Right Alt``: F17
* ``Right Win``: F18

.. rubric:: Olivetti M240

See: :ref:`m24`

.. rubric:: Toshiba T1200

All function keys from the :ref:`T1000 <t1000>` are present, plus:

* ``Right Alt/Ctrl + Page Up``: Turbo mode on
* ``Right Alt/Ctrl + Page Down``: Turbo mode off
* ``Right Alt/Ctrl + Print Screen``: Show/hide pop-up window

80286
-----

.. rubric:: IBM AT

* The IBM Personal Computer Diagnostics disks are not Y2K-compliant and will produce a *0152 ERROR - SYSTEM BOARD* code if :ref:`time synchronization <settings/machine:Time synchronization>` is enabled. This code can be cleared by disabling time synchronization, then clearing the CMOS by deleting ``ibmat.nvr`` from the ``nvr`` directory.

Socket 7
--------

.. _p65up5:
.. rubric:: ASUS P/I-P65UP5 (C-P55T2D)

* Modular motherboard, consisting of a **P/I-P65UP5** baseboard and one of the following CPU cards:

   * **C-P55T2D:** Socket 7 with Intel 430HX northbridge;
   * **C-P6ND:** Socket 8 with Intel 440FX northbridge;
   * **C-PKND:** Slot 1 with Intel 440FX northbridge.

* While the northbridge depends on the selected CPU card, the southbridge always remains the Intel PIIX3, as it is located on the baseboard.
* The real CPU cards support dual CPUs. As 86Box does not emulate multiprocessing, only a single CPU will be present.
* Due to a lack of I/O APIC emulation at the moment, 86Box will patch the MultiProcessor Specification tables out of RAM during boot, so that operating systems will not hang or exhibit other erratic behavior due to the missing I/O APIC.

Socket 8
--------

.. rubric:: ASUS P/I-P65UP5 (C-P6ND)

See: :ref:`p65up5`

Slot 1
------

.. rubric:: ASUS P/I-P65UP5 (C-PKND)

See: :ref:`p65up5`

.. _atc6310bxii:
.. rubric:: A-Trend ATC6310BXII

* Equipped with the obscure SMSC Victory66 southbridge instead of the regular Intel PIIX4E.

   * The Victory66 has faster IDE - up to Ultra ATA/66 as opposed to the PIIX4E's Ultra ATA/33 - and a different USB controller.
   * Drivers for Windows 95, 98, Me and 2000 are available `here <https://essentials.86box.net/drivers/chipset/SMSC%20SLC90E66%20%28Victory66%29%20%28Windows%209x%20and%202000%29.zip>`_. Windows XP, Vista and 7 include drivers out of the box.

Slot 2
------

.. rubric:: Gigabyte GA-6GXU

* The BIOS display will corrupt itself during the memory test if the maximum of 2048 MB RAM is selected. This is a visual glitch which does not otherwise negatively impact the machine.

.. rubric:: Freeway FW-6400GX

* Hybrid motherboard supporting both Slot 1 and Slot 2 CPUs.
* The maximum amount of RAM is limited to 2032 MB due to a BIOS bug with 2048 MB.
* ACPI is disabled by default. It can be enabled through the *ACPI Aware O/S* option of the *Power Management Setup* menu on the BIOS setup.
* Once enabled, ACPI :ref:`does not work correctly <brokenacpi>` if a non-Intel CPU is selected.

Socket 370
----------

.. rubric:: A-Trend ATC7020BXII

See: :ref:`atc6310bxii`

.. rubric:: AEWIN AW-O671R

* Equipped with dual Winbond W83977EF Super I/O chips driving four serial (COM1-COM4) and two parallel (LPT1-LPT2) ports.

   * The I/O ports and IRQs used by all these ports can be configured in the BIOS setup.

* ACPI is disabled by default, unlike other machines with Award v6.00PG BIOS. It can be enabled through the *ACPI function* option of the *Power Management Setup* menu on the BIOS setup.

Miscellaneous
-------------

.. rubric:: Microsoft Virtual PC 2007

* This machine loads the American Megatrends BIOS from Virtual PC 2007 into 86Box's emulation. It does not use the virtualization engine or any other components from Virtual PC.
* Virtual PC's special 8 MB video card, network card, WDM sound card and Guest Additions are not emulated by 86Box.

----

Footnotes
---------

.. _brokenacpi:
.. rubric:: Broken ACPI

Some machines may have faulty or otherwise incomplete `Advanced Configuration and Power Interface <https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface>`_ implementations in their BIOSes, symptoms of which include:

* Windows 2000 and higher will install the "Standard PC" HAL, which does not enable ACPI features such as soft power off and sleep mode;
* Booting an existing Windows installation with the ACPI HAL will result in a STOP 0x000000A5 blue screen;
* Booting Windows Vista or 7 (which require ACPI) will also result in a STOP 0x000000A5 blue screen, or a Windows Boot Manager 0xc0000225 error.

There is no solution to this issue, as none of the currently emulated machines with broken ACPI ever received a BIOS update to fix it.
