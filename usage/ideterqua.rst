Tertiary and quaternary IDE
===========================

The additional tertiary and quaternary IDE controllers, enabled through the :ref:`settings/peripherals:Tertiary / Quaternary IDE Controller` settings, may require manual configuration of guest operating systems, which is outlined in this page. They are also **not bootable**, except on machines equipped with MR BIOS.

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

The tertiary and quaternary controllers are only supported (partially or fully) by some BIOSes. The following table lists all BIOSes emulated by 86Box which are known to support these controllers:

+--------------------------------+-------------+-----------+-------------------------------+
|BIOS                            |Seen in BIOS?|Bootable? *|:ref:`Windows NT support? <nt>`|
+================================+=============+===========+===============================+
|American Megatrends             |No           |No         |Yes                            |
+--------------------------------+-------------+-----------+-------------------------------+
|Phoenix - AwardBIOS v6.00PG \*\*|No           |No         |Yes                            |
+--------------------------------+-------------+-----------+-------------------------------+
|MR BIOS                         |Yes          |Yes        |Yes                            |
+--------------------------------+-------------+-----------+-------------------------------+

| \* Includes support for DOS and other real mode operating systems.
| \*\* Award Modular BIOS v6.00PG and all other versions before it do not have any support.

Windows 95, 98 and Me
----------------

TBD

.. _nt:

Windows NT, 2000, XP and newer
------------------------------

The Windows NT family will detect and enable both additional channels at installation time *only if* supported by the BIOS (see the *Windows NT support?* column on :ref:`the table above <bios>`).

.. note:: If you install the system to a hard disk on one of the additional channels, it will not be bootable if the BIOS doesn't support booting from these channels (see the *Bootable?* column).

Alternatively, the additional channels can be enabled after the system is installed:

* **Windows NT 4.0:** TBD.
* **Windows 2000:** go to the *Add New Hardware* control panel and add a *Generic IDE/ESDI Hard Disk Controller* device for each additional channel. Configuration 000x corresponds to the **tertiary** channel, while Configuration 000x corresponds to the **quaternary** channel.
* **Windows XP:** TBD. (IDE/ESDI not listed - let PnP do the job?)

Linux
-----
          
On kernels 2.6.19 and newer (after the switch to ``libata``), run the ``modprobe pata_legacy probe_all=1`` command as root to enable both additional channels. Consult your distribution's documentation on how to load that module on startup.

On kernels older than 2.6.19 (before the switch to ``libata``), add the following parameters to the kernel command line to enable their respective channels:

* **Tertiary:** ``ide2=0x168,0x36e,10`` (assuming IRQ 10)
* **Quaternary:** ``ide3=0x1e8,0x3ee,11`` (assuming IRQ 11)
