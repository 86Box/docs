Machine-specific notes
======================

This page contains important notes related to specific machine models emulated by 86Box.

----

8088
----

.. _ibmpc:
.. rubric:: IBM PC

* The 1981 and 1982 variants correspond to the `earlier 16KB-64KB and later 64KB-256KB revisions of the motherboard <https://www.minuszerodegrees.net/5150/motherboard/5150_motherboard_revisions.htm>`_, with different BIOS versions and memory size limits.

  * Those limits apply to on-board RAM; more can be added through :ref:`ISA memory expansion <settings/peripherals:ISA Memory Expansion>` cards.

.. rubric:: IBM PCjr

* Some applications may shift the display slightly to one side due to unconventional use of the PCjr video hardware. Unchecking the **Apply overscan deltas** option accessible through the internal video's :ref:`Configure button <settings/display:Video>` can help bring the display back into position.
* Hard disks are not supported, as a PCjr-compatible hard disk controller is not emulated by 86Box.

.. _ibmxt:
.. rubric:: IBM XT

* The 1982 and 1986 variants correspond to the `earlier 64-256KB and later 256-640KB revisions of the motherboard <https://www.minuszerodegrees.net/5160/motherboard/5160_motherboard_revisions.htm>`_, with different BIOS versions and memory size limits.

  * Those limits apply to on-board RAM; more can be added through :ref:`ISA memory expansion <settings/peripherals:ISA Memory Expansion>` cards.

80286
-----

.. _ibmat:
.. rubric:: IBM AT

* On-board RAM is limited to 512 KB; more can be added through :ref:`ISA memory expansion <settings/peripherals:ISA Memory Expansion>` cards.
* The IBM Personal Computer Diagnostics disks are not Y2K-compliant and will produce a *0152 ERROR - SYSTEM BOARD* code if :ref:`time synchronization <settings/machine:Time synchronization>` is enabled. This code can be cleared by disabling time synchronization, then clearing the CMOS by deleting ``ibmat.nvr`` from the machine's ``nvr`` directory.

.. rubric:: IBM XT Model 286

* On-board RAM is limited to 640 KB; more can be added through :ref:`ISA memory expansion <settings/peripherals:ISA Memory Expansion>` cards.

.. rubric:: AMI IBM AT

See: :ref:`ibmat`

.. rubric:: Phoenix IBM AT

See: :ref:`ibmat`

.. rubric:: Quadtel IBM AT

See: :ref:`ibmat`

.. rubric:: GRiD GRiDcase 1520

* The BIOS is locked to specific Conner IDE hard disk models. Any hard disks must be set to the **Conner CP3024**, **CP3044** or **CP3104** :ref:`model profiles <settings/hdd:Model>`.
* The Yamaha V6366 video chip is not emulated by 86Box. An **IBM CGA** set to amber monochrome mode (through the :ref:`Configure button <settings/display:Video>`) is recommended as an approximation.

i386SX
------

.. rubric:: Amstrad MegaPC

* The BIOS does not configure itself on first boot or after clearing CMOS; the machine will not work properly until an automatic configuration is performed by pressing **F9** on the BIOS setup's main *Setup* menu, then saving with **F10** and exiting with **Esc**.

i486
----

.. rubric:: IBM Aptiva 510/710/Vision

* The BIOS setup utility is only available in Japanese. For English, use the otherwise identical **IBM PC 330 (type 6573)**.

.. rubric:: Zida Tomato 4DP

* Floppy drive support is completely disabled by default. It can be enabled through the *Onboard FDD Controller* option of the *Chipset Features Setup* menu on the BIOS setup; the floppy drives themselves must also be configured in the *Standard CMOS Setup* menu.

Socket 7
--------

.. rubric:: MSI MS-5119

* 86Box versions prior to 4.0.1 used BIOS version *A37E*, which has PS/2 mouse issues. The fixed *A37EB* BIOS is not applied automatically to existing setups; it can be applied by deleting ``ms5119.bin`` from the machine's ``nvr`` directory.

.. _p65up5:
.. rubric:: ASUS P/I-P65UP5 (C-P55T2D)

* Modular motherboard, consisting of a **P/I-P65UP5** baseboard and one of the following CPU cards:

   * **C-P55T2D:** Socket 7 with Intel 430HX northbridge;
   * **C-P6ND:** Socket 8 with Intel 440FX northbridge;
   * **C-PKND:** Slot 1 with Intel 440FX northbridge.

* While the northbridge depends on the selected CPU card, the southbridge always remains the Intel PIIX3, as it is located on the baseboard.
* The real CPU cards support dual CPUs. As 86Box does not emulate multiprocessing, only a single CPU will be present.
* Due to a lack of I/O APIC emulation at the moment, 86Box will patch the MultiProcessor Specification tables out of RAM during boot, so that operating systems will not hang or exhibit other erratic behavior due to the missing I/O APIC.

.. _ma23c:
.. rubric:: NEC Mate NX MA23C

* Accessing the BIOS setup utility takes an additional step. Press **F2** during the NEC logo screen and some Japanese text will appear; once a different line of text appears, press the **right arrow** key to enter the setup utility.
* The first setup option below the date and time can be used to change the BIOS language to English.

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

.. rubric:: NEC Mate NX MA30D/23D

See: :ref:`ma23c`

Slot 1/2
--------

.. rubric:: Freeway FW-6400GX

* The maximum amount of RAM is limited to 2032 MB due to a BIOS bug with 2048 MB.
* ACPI is disabled by default. It can be enabled through the *ACPI Aware O/S* option of the *Power Management Setup* menu on the BIOS setup.
* Once enabled, ACPI :ref:`does not work correctly <brokenacpi>` if a non-Intel CPU is selected.

Slot 2
------

.. rubric:: Gigabyte GA-6GXU

* The BIOS display will corrupt itself during the memory test if the maximum of 2048 MB RAM is selected. This is a visual glitch which does not otherwise negatively impact the machine.

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
* Virtual PC's special 8 MB video card, WDM sound card and Guest Additions are not emulated by 86Box.

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
