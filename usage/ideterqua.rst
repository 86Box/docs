Tertiary and quaternary IDE
===========================

The additional tertiary and quaternary IDE controllers, enabled through the :ref:`settings/peripherals:Tertiary / Quaternary IDE Controller` settings, are not supported by all BIOSes and may require manual configuration of guest operating systems. The specific details are outlined on this page.

The following system resources are used by these additional controllers:

.. _table:

+----------+-------------+---------------+---+
|Channel   |Main I/O port|Status I/O port|IRQ|
+==========+=============+===============+===+
|Tertiary  |0168h        |036Eh          |10 |
+----------+-------------+---------------+---+
|Quaternary|01E8h        |03EEh          |11 |
+----------+-------------+---------------+---+

.. note:: While the IRQ for each channel can be changed through its respective *Settings* button on :ref:`settings/peripherals:Tertiary / Quaternary IDE Controller`, many operating systems do not allow legacy (ISA or VLB) IDE controllers to use custom IRQs.

BIOS support
------------

The tertiary and quaternary channels are both not visible and not bootable in any BIOS, with the exception of **MR BIOS version 3**, which provides full support for them, including bootability and INT 13h services.

DOS and real mode
-----------------

DOS and other real mode operating systems rely on the BIOS-provided INT 13h services to access hard disks. These are only provided for the tertiary and quaternary channels by **MR BIOS version 3**, as mentioned above.

Windows 95, 98 and Me
---------------------

The Windows 9x family will only detect and enable both additional channels during installation :ref:`if the BIOS supports them <usage/ideterqua:BIOS support>`. Each additional channel can be enabled after installation through the following procedure:

1. Go to the *Add New Hardware* control panel.
2. Add a *Standard IDE/ESDI Hard Disk Controller* from the *Hard disk controllers* category.
3. Don't restart the system when asked to.
4. Go to the *Device Manager* tab of the *System* control panel.
5. Select the newly-added *Standard IDE/ESDI Hard Disk Controller* device from the *Hard disk controllers* category and click *Properties*.
6. Go to the *Resources* tab.
7. Select *Basic configuration 4* in the *Settings based on* box.
8. Change the resource settings to match the :ref:`table above <table>`. The first *Input/Output Range* range corresponds to the **main** I/O port, the second one corresponds to the **status** I/O port, and *Interrupt Request* corresponds to the IRQ.

   * The status I/O port range is off by 6 units. Select 0368 for the tertiary channel or 03E8 for the quaternary channel.
   * The image below shows an example configuration for the tertiary channel.

9. If both the tertiary and quaternary channels are enabled, repeat the steps above to add the other channel.

.. image:: images/ideterqua_win98.png
   :align: center

.. _nt:

Windows NT, 2000, and XP
------------------------

The Windows NT 4 and 5 families will automatically detect and enable both additional channels during installation, regardless of BIOS support. This auto-detection does not, however, work on machines with **Award BIOS**, except for the version which identifies itself as *Phoenix - AwardBIOS v6.00PG*, where it does work.

.. note:: If you install the system to a hard disk on one of the additional channels, it will not be bootable if the BIOS doesn't support booting from these channels.

On Windows 2000 only, the additional channels can be enabled after the system is installed through *Add New Hardware* similarly to Windows 95/98/Me above, although the I/O ports and IRQ cannot be changed. *Basic configuration 0003* corresponds to the **tertiary** channel, while *Basic configuration 0002* corresponds to the **quaternary** channel.

Windows Vista and 7
-------------------

The Windows NT 6 family does not support non-Plug-and-Play IDE controllers.

Linux
-----
          
On kernels 2.6.19 and newer (after the switch to ``libata``), run the ``modprobe pata_legacy probe_all=1`` command as root to enable both additional channels. Consult your distribution's documentation on how to load that module on startup.

On kernels older than 2.6.19 (before the switch to ``libata``), add the following parameters to the kernel command line to enable their respective channels:

* **Tertiary:** ``ide2=0x168,0x36e,10`` (assuming IRQ 10)
* **Quaternary:** ``ide3=0x1e8,0x3ee,11`` (assuming IRQ 11)
