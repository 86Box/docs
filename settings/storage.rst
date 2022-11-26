.. include:: /include.rst

|storage_controllers| Storage controllers
=========================================

The **Storage controllers** page contains settings related to the emulated machine's disk drive controllers.

HD Controller
-------------

Hard disk drive controller card to emulate. This box only lists cards supported by the machine's expansion buses. MFM, RLL, ESDI and IDE controllers are available. Selecting an IDE controller is not required for machines with onboard IDE.

The *Configure* button opens a new window with settings specific to the selected controller card, such as the BIOS option ROM address.

FD Controller
-------------

Floppy disk drive controller card to emulate. Selecting a controller is not required, unless you wish to use one of the add-on controllers for adding high-density 1.44M floppy support to XT machines.

The BIOS option ROM address used by the selected controller can be configured through the *Settings* button.

Tertiary / Quaternary IDE Controller
------------------------------------

Add a third or fourth (respectively) IDE channel to the emulated machine, through a generic ISA or VLB IDE controller card.

The IRQ used by each controller can be configured through its respective *Settings* button.

.. note:: The tertiary and quaternary controllers are not Plug and Play compliant by default; they may require manual configuration of emulated operating systems, and may not be bootable. See :doc:`../hardware/ideterqua` for more information.

SCSI
----

SCSI host bus adapter cards to emulate. Up to 4 SCSI cards are supported. The selection boxes only list cards supported by the machine's expansion buses.

The *Configure* buttons open a new window with settings specific to the corresponding SCSI card, such as the I/O port and IRQ for ISA cards.

Cassette
--------

Enable IBM cassette tape emulation. The cassette deck can be controlled through the :ref:`status bar <usage/statusbar:|cassette| Cassette deck>` or :ref:`Media menu <usage/menubar:Media>`.

.. note:: While cassette emulation can be enabled on any machine, it is only usable on the IBM PC, PCjr and other machines with an IBM cassette port.
