Tertiary and Quaternary IDE
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

.. important:: While the IRQ for each channel can be changed through its respective *Settings* button on :ref:`settings/peripherals:Tertiary / Quaternary IDE Controller`, most operating systems do not allow IDE controllers to use custom IRQs.

Windows NT (including 2000, XP and newer)
-----------------------------------------

The Windows NT family will detect and enable both additional channels at installation time.

Additionally, they can be enabled after the fact through the *Add New Hardware* control panel, by adding a *Generic IDE/ESDI Hard Disk Controller* device for each channel. Configuration 000x corresponds to the **tertiary** channel, while Configuration 000x corresponds to the **quaternary** channel.

Linux
-----
          
On kernels 2.6.19 and newer (after the switch to ``libata``), run the ``modprobe pata_legacy probe_all=1`` command as root to enable both additional channels. Consult your distribution's documentation on how to load that module on startup.

On kernels older than 2.6.19 (before the switch to ``libata``), add the following parameters to the kernel command line to enable their respective channels:

* **Tertiary:** ``ide2=0x168,0x36e,10`` (assuming IRQ 10)
* **Quaternary:** ``ide3=0x1e8,0x3ee,11`` (assuming IRQ 11)
