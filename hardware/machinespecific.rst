Machine-specific notes
======================

This |page| contains important notes related to specific machine models emulated by 86Box.

----

8088
----

.. _ibmpc:
.. rubric:: IBM PC

* The 1981 and 1982 variants correspond to the `earlier 16KB-64KB and later 64KB-256KB revisions of the motherboard <https://www.minuszerodegrees.net/5150/motherboard/5150_motherboard_revisions.htm>`_, with different BIOS versions and memory size limits.

  * Those limits apply to on-board RAM; more can be added through :ref:`ISA memory expansion <settings/peripherals:|isa_memory| ISA Memory Expansion>` cards.

.. rubric:: IBM PCjr

* Some applications may shift the display slightly to one side due to unconventional use of the PCjr video hardware. Unchecking the **Apply overscan deltas** option accessible through the internal video's :ref:`Configure button <settings/display:Video>` can help bring the display back into position.

.. _ibmxt:
.. rubric:: IBM XT

* The 1982 and 1986 variants correspond to the `earlier 64-256KB and later 256-640KB revisions of the motherboard <https://www.minuszerodegrees.net/5160/motherboard/5160_motherboard_revisions.htm>`_, with different BIOS versions and memory size limits.

  * Those limits apply to on-board RAM; more can be added through :ref:`ISA memory expansion <settings/peripherals:|isa_memory| ISA Memory Expansion>` cards.

80286
-----

.. rubric:: IBM AT

* On-board RAM is limited to 512 KB; more can be added through :ref:`ISA memory expansion <settings/peripherals:|isa_memory| ISA Memory Expansion>` cards.

.. rubric:: IBM XT Model 286

* On-board RAM is limited to 640 KB; more can be added through :ref:`ISA memory expansion <settings/peripherals:|isa_memory| ISA Memory Expansion>` cards.

.. rubric:: GRiD GRiDcase 1520

* The BIOS is locked to specific Conner IDE hard disk models. Any hard disks must be set to the **Conner CP3024**, **CP3044** or **CP3104** :ref:`model profiles <settings/hdd:Model / Audio>`.
* The Yamaha V6366 video chip is not emulated by 86Box. An **IBM CGA** set to amber monochrome mode (through the :ref:`Configure button <settings/display:Video>`) is recommended as an approximation.

i386SX
------

.. rubric:: Amstrad MegaPC

* The BIOS does not configure itself on first boot or after clearing CMOS; the machine will not work properly until an automatic configuration is performed by pressing :kbd:`F9` on the BIOS setup's main *Setup* menu, then saving with :kbd:`F10` and exiting with :kbd:`Esc`.

i486
----

.. rubric:: Intel Classic R/R Plus (Monsoon)

* The messages for entering the BIOS setup and skipping the memory test are not displayed by default. To enter the setup utility, press :kbd:`F1` when the number *135* or an error is displayed. To skip the memory test, press :kbd:`Space`. Both messages can be enabled through the *POST Setup Prompt* and *POST Memory Test Prompt* options in page 1 of the BIOS setup utility respectively.
* The internal IDE hard disk controller is disabled by default. It can be enabled through the *Onboard IDE* option in page 1 of the BIOS setup utility.

.. rubric:: Zida Tomato 4DPS

* On the default Funworld BIOS, floppy drive support must be enabled manually through the *Onboard FDD Controller* option of the *Chipset Features Setup* menu in the BIOS setup; the floppy drives themselves must also be configured in the *Standard CMOS Setup* menu.

Socket 7
--------

.. rubric:: MSI MS-5119

* 86Box versions prior to 4.0.1 used BIOS version *A37E*, which has PS/2 mouse issues. The fixed *A37EB* BIOS is not applied automatically to existing setups; it can be applied by wiping NVRAM :ref:`through the VM manager <usage/manager:Machine list>` or deleting ``ms5119.bin`` from the machine's ``nvr`` directory.

.. _p65up5:
.. rubric:: ASUS P/I-P65UP5 (C-P55T2D)

* Modular motherboard, consisting of a **P/I-P65UP5** baseboard and one of the following CPU cards:

  * **C-P55T2D:** Socket 7 with Intel 430HX northbridge;
  * **C-P6ND:** Socket 8 with Intel 440FX northbridge;
  * **C-PKND:** Slot 1 with Intel 440FX northbridge.

* While the northbridge depends on the selected CPU card, the southbridge always remains the Intel PIIX3, as it is located on the baseboard.
* The real CPU cards support dual CPUs. As 86Box does not emulate multiprocessing, only a single CPU will be present.
* Due to a lack of I/O APIC emulation at the moment, 86Box will patch the MultiProcessor Specification tables out of RAM during boot, so that operating systems will not hang or exhibit other erratic behavior due to the missing I/O APIC.

.. rubric:: AwardBIOS v6.00PG Beta Evaluation Board

* This custom motherboard was used by Award Software to evaluate what are assumed to be early betas of AwardBIOS v6.00PG around 1997-1998.
* The BIOS identifies as AwardBIOS v4.51PG for the `EFA P5TX-AT <https://theretroweb.com/motherboards/s/efa-p5tx-at>`_ or `E5TX-AT <https://theretroweb.com/motherboards/s/efa-e5tx-at>`_; however, the target hardware deviates from those boards, and the setup utility is an early version of the Phoenix-style one seen in some v6.00PG implementations.
* Being early internal betas, the BIOS versions have known bugs and quirks:

  * The integrated IDE controller is disabled by default in the BIOS setup. To enable it, go to the *Integrated Peripherals* sub-menu under the *Advanced* menu and set the *On-Chip Primary PCI IDE* and *On-Chip Secondary PCI IDE* options to *Enabled*. Note that the *Onboard IDE Controller* option in the same menu corresponds to the Super I/O chip's unused IDE controller and should remain *Disabled* to prevent a conflict with the chipset IDE.
  * The November 1997 beta's setup utility often crashes when scrolling down in long menus, while the January 1998 beta (the default option) is more stable.
  * The setup utility's IDE drive types are slightly non-standard: type *47* corresponds to automatic detection, while both *49* and *50* correspond to custom drive parameters. CD-ROM and other non-hard-disk drives must be set to *47*.
  * Windows 95, 98 and Me may report a conflict between IDE drivers, which does not affect normal operation.

.. _ma23c:
.. rubric:: NEC Mate NX MA23C

* Accessing the BIOS setup utility takes an additional step. Press :kbd:`F2` during the NEC logo screen and a Japanese message will appear; once a different message appears, press :kbd:`🠊` (right arrow) to enter the setup utility.
* The first setup option below the date and time can be used to change the BIOS language to English.

.. rubric:: Siemens Simatic OP47

* Equipped with SMC FDC37C932FR and Intel 82091AA Super I/O chips driving four serial (COM1-COM4) and one parallel (LPT1) ports.

Super Socket 7
--------------

.. _cobalt3k-pacifica:
.. rubric:: Cobalt RaQ 3/4

* **Not PC compatible:** the BIOS can only boot the Cobalt operating system or a customized Linux installation from an IDE hard disk or a network server, and it can only be interacted with through the :ref:`LCD console <hardware/keyboard:Cobalt>` or a serial console. Keyboards and video cards are not supported.
* The BIOS defaults to network boot for restoring the operating system. Official restore discs are live CDs designed to be booted on a regular PC with a **direct network connection** to the Cobalt.

  * Using another 86Box machine with an *Intel PRO/100* network card connected through the :ref:`Local Switch feature <hardware/network:Local Switch>` is recommended.
  * Some restore discs will not change the default boot order to hard disk when done. Change it through the BIOS menu before or after restoring: hard reset the machine, hold down :kbd:`Space` (Select) when the Cobalt logo starts to appear, release it when *Select option* appears, use the arrow keys to select *Configure boot*, press :kbd:`Enter`, select *From disk*, press :kbd:`Enter`, select *Boot from disk* or *Boot from net*, press :kbd:`Enter`.
  * Some restore discs will disable the serial console when done. To enable it again: hard reset the machine, hold down :kbd:`Esc` (password reset pinhole) when the Cobalt logo starts to appear, release it when *console ON* appears.

* Recommended machine settings for the Cobalt operating system:

  * :ref:`BIOS <settings/machine:Machine type / Machine>` 2.3.39 (the default option), as later versions have restore-related bugs.
  * :ref:`Network cards 1 and 2 <settings/network:|network| Adapter 1-4>` set to *Internal device*.
  * :ref:`COM1 <settings/ports:COM1-4>` set to *Virtual Console* for detailed boot logs. :ref:`LPT1 <settings/ports:LPT1-4>` set to *None* as it is internally taken up by the LCD console and therefore cannot be used.
  * Two identical :doc:`IDE hard disks <../settings/hdd>` on channels 0:0 and 1:0, as some restore discs set up a RAID 1 across two disks and will fail to restore without both. On-board SCSI is available but not supported by software.

.. _cobalt3k-carmel:
.. rubric:: Cobalt Qube 3

See: :ref:`cobalt3k-pacifica`

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

* The maximum amount of RAM is limited to 1792 MB due to a BIOS bug with 2048 MB.
* ACPI is disabled by default. It can be enabled through the *ACPI Aware O/S* option of the *Power Management Setup* menu in the BIOS setup.
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

* ACPI is disabled by default, unlike other machines with AwardBIOS v6.00PG. It can be enabled through the *ACPI function* option of the *Power Management Setup* menu in the BIOS setup.

.. rubric:: ASUS CUBX

* Equipped with an on-board CMD PCI-0648 IDE controller on the :ref:`tertiary and quaternary channels <settings/hdd:Adding a new disk>`, on top of the PIIX4E southbridge controller on the primary and secondary channels.

.. rubric:: Samsung CAIRO-5 (MSI MS-6309)

* The BIOS is in Korean by default. Press :kbd:`F2` during the Samsung logo screen to enter the setup utility, where the first option can be used to change the BIOS language to English.
* :ref:`Broken ACPI <brokenacpi>` causes some operating systems such as Windows 2000 and Linux to reboot during startup. :ref:`Disabling ACPI at operating system level <acpioff>` is required, as the BIOS lacks an option for it.

Miscellaneous
-------------

.. rubric:: Microsoft Virtual PC 2007

* This machine loads the AMIBIOS 8 ROM from Virtual PC 2007 on 86Box. It does not use the virtualization engine or any other components from Virtual PC.
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

There is no solution to this issue outside of disabling ACPI, as none of the affected machines ever received a BIOS update to fix it. ACPI can be disabled through the BIOS setup on many machines, or at operating system level if that is not an option:

  .. _acpioff:

* **Windows 2000 or XP:** during installation, press :kbd:`F7` when the *Press F6 if you need to install a third party SCSI or RAID driver...* message appears; this disables ACPI even though no indication is displayed on screen.
* **Linux:** add ``acpi=off`` to the kernel command line.
