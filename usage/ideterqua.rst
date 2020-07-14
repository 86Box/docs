Tertiary and quaternary IDE
===========================

The additional tertiary and quaternary IDE controllers, enabled through the :ref:`settings/peripherals:Tertiary / Quaternary IDE Controller` settings, are not supported by all BIOSes and may require manual configuration of guest operating systems. The specific details are outlined on this page.

The following system resources are used by these additional controllers:

+----------+-------------+---------------+---+
|Channel   |Main I/O port|Status I/O port|IRQ|
+==========+=============+===============+===+
|Tertiary  |0168h        |036Eh          |10 |
+----------+-------------+---------------+---+
|Quaternary|01E8h        |03EEh          |11 |
+----------+-------------+---------------+---+

.. note:: While the IRQ for each channel can be changed through its respective *Settings* button on :ref:`settings/peripherals:Tertiary / Quaternary IDE Controller`, most operating systems do not allow legacy (ISA or VLB) IDE controllers to use custom IRQs.

.. _bios:

BIOS support
------------

The tertiary and quaternary channels are both not visible and not bootable in any BIOS with the exception of **MR BIOS**, which provides full support for them, including bootability and real mode / DOS (INT 13h) access.

Windows 95, 98 and Me
---------------------

TBD

.. _nt:

Windows NT, 2000, and XP
------------------------

The Windows NT 4 and 5 family will automatically detect and enable both additional channels during installation. This auto-detection does not work on machines with **Award BIOS**, except for the version that identifies itself as *Phoenix - AwardBIOS v6.00PG*, which does work.

.. note:: If you install the system to a hard disk on one of the additional channels, it will not be bootable if the BIOS doesn't support booting from these channels.

On Windows 2000 only, the additional channels can be enabled after the system is installed by going to the *Add New Hardware* control panel and adding a *Standard IDE/ESDI Hard Disk Controller* device for each additional channel. Configuration 0002 corresponds to the **tertiary** channel, while Configuration 0003 corresponds to the **quaternary** channel.

Windows Vista and 7
-------------------

The Windows NT 6 family does not support non-Plug-and-Play IDE controllers.

Linux
-----
          
On kernels 2.6.19 and newer (after the switch to ``libata``), run the ``modprobe pata_legacy probe_all=1`` command as root to enable both additional channels. Consult your distribution's documentation on how to load that module on startup.

On kernels older than 2.6.19 (before the switch to ``libata``), add the following parameters to the kernel command line to enable their respective channels:

* **Tertiary:** ``ide2=0x168,0x36e,10`` (assuming IRQ 10)
* **Quaternary:** ``ide3=0x1e8,0x3ee,11`` (assuming IRQ 11)
