.. include:: /include.rst

|storage_controllers| Storage controllers
=========================================

The **Storage controllers** page contains settings related to the emulated machine's disk drive controllers.

.. note:: The **Vision Systems LBA Enhancer** previously available here is now an ISA ROM card, which can be enabled through the :ref:`Other peripherals page <settings/peripherals:ISA ROM Cards>`.

FD Controller
-------------

Floppy disk drive controller card to emulate. Selecting a controller is not required, unless you wish to use one of the add-on controllers for adding high-density 1.44M floppy support to XT machines.

The BIOS option ROM address used by the selected controller can be configured through the *Configure* button.

CD-ROM Controller
-----------------

Standalone CD-ROM controller card to emulate. These cards provide vendor-specific CD-ROM interfaces beyond :ref:`ATAPI (IDE) <settings/storage:Hard disk>` or :ref:`settings/storage:SCSI`.

The I/O port used by the selected controller can be configured through the *Configure* button.

Hard disk
---------

MFM, RLL, ESDI or IDE hard disk drive controller cards to emulate. Up to 4 controller cards are supported. The selection boxes only list cards supported by the machine's expansion buses. On machines equipped with an on-board disk controller, the *Internal* option for controller #1 enables the on-board controller; this is not required for machines with on-board IDE.

The *Configure* buttons open a new window with settings specific to the corresponding controller card, such as the I/O port and IRQ for ISA cards.

.. note:: The **tertiary and quaternary IDE controllers** are now selectable here, replacing the previous separate options for each. These controllers are not Plug and Play compliant by default, potentially requiring manual configuration of the emulated operating system, and may not be bootable; see :doc:`../hardware/ideterqua` for more information.

SCSI
----

SCSI host bus adapter cards to emulate. Up to 4 SCSI cards are supported. The selection boxes only list cards supported by the machine's expansion buses.

The *Configure* buttons open a new window with settings specific to the corresponding SCSI card, such as the I/O port and IRQ for ISA cards.

Cassette
--------

Enable IBM cassette tape emulation. Only available on machines with a cassette port. The cassette deck can be controlled through the :ref:`status bar <usage/statusbar:|cassette| Cassette deck>` or :ref:`Media menu <usage/menubar:Media>`.
