.. include:: /include.rst

|floppy_and_cdrom_drives| Floppy & CD-ROM drives
================================================

The **Floppy & CD-ROM drives** page contains settings related to the emulated machine's base removable storage drives.

Floppy drives
-------------

Up to four floppy disk drives can be attached to the emulated system, although not all machines provide BIOS support for more than two drives. The following settings apply to the selected drive:

* **Type:** floppy drive to emulate. Some types have special properties and should only be used in very specific applications:

   * **5.25" 1.2M PS/2** and **3.5" 1.44M PS/2:** IBM PS/2 drives, which invert the polarity of the Density Select pin.
   * **5.25" 1.2M 300/360 RPM** and **3.5" 1.44M 300/360 RPM**: "3-mode" drives, which are capable of reading 360K 5.25" or NEC PC-98 3.5" disks if the emulated machine's BIOS supports 3-mode operation.
   * **3.5" 1.44M PC-98:** NEC PC-98 drive, which is 3-mode and inverts the polarity of the Density Select pin.

* **Turbo timings:** run the drive mechanism as fast as possible. This decreases access times and makes some incorrectly-dumped floppies readable, but may cause issues with some operating systems and applications.
* **Check BPB:** if unchecked, 86Box will ignore the `DOS BIOS Parameter Block <https://en.wikipedia.org/wiki/BIOS_parameter_block>`_ when determining the physical media format for a floppy image on this drive. See :ref:`hardware/diskimages:Floppy disk detection` for more details.

.. note:: Disabling "Check BPB" may be required in order to access UNIX/Linux installation floppies or other non-DOS disks, as outlined on :ref:`hardware/diskimages:Floppy disk detection`.

Floppy disk images can be inserted and removed through the :ref:`status bar <usage/statusbar:|floppy_35| |floppy_525| Floppy drives>` or :ref:`Media menu <usage/menubar:Media>`.

CD-ROM drives
-------------

Up to four CD-ROM / DVD-ROM optical disc drives can be attached to the emulated system. The following settings apply to the selected drive:

* **Bus:** storage bus to attach the drive to. ATAPI (IDE) and SCSI are supported.
* **Channel**/**ID:** where to attach the drive on the selected storage bus. See :ref:`settings/hdd:Adding a new disk` for more information.
* **Speed:** maximum transfer speed for the drive. Up to 72x is supported.
* **Type:** CD-ROM drive model to identify as. A list of drive models to choose from is provided. Some emulated machines have manufacturer restore discs locked to a specific drive model.

CD-ROM / DVD-ROM disc images can be inserted and removed through the :ref:`status bar <usage/statusbar:|cdrom| CD-ROM drives>` or :ref:`Media menu <usage/menubar:Media>`.
