Floppy and CD-ROM drives
========================

The *Floppy and CD-ROM drives* page contains settings related to the emulated machine's base removable devices.

Floppy drives
-------------

Up to four floppy disk drives can be attached to the emulated system, although not all BIOSes provide support for more than two drives. The following options apply to the selected drive:

* **Type:** Type of floppy drive to emulate. Some drive types have special properties:

   * **5.25" 1.2M PS/2** and **3.5" 1.44M PS/2:** IBM PS/2 drives, which have inverted polarity on the Density Select pin.
   * **5.25" 1.2M 300/360 RPM** and **3.5" 1.44M 300/360 RPM**: "3-mode" drives, which are capable of reading 360K 5.25" or PC-98 3.5" disks. BIOS support for 3-mode floppy drives is required.
   * **3.5" 1.44M PC-98:** NEC PC-98 drives, which are 3-mode and have inverted polarity on the Density Select pin.

* **Turbo timings:** Run the drive mechanism as fast as possible. This decreases access time and makes some incorrectly-dumped floppies readable, but may cause issues some operating systems and applications.
* **Check BPB:** When disabled, 86Box will skip checking the `DOS BIOS Parameter Block <https://en.wikipedia.org/wiki/BIOS_parameter_block>`_ when determining the physical media format for a floppy image on this drive. See :ref:`usage/diskimages:Floppy disk detection` for more details.

.. note:: Disabling "Check BPB" may be required in order to access UNIX/Linux installation floppies or other raw stream disks, as outlined on the page linked above.

Floppy disk images can be inserted and removed through the status bar or the *Media* menu.

CD-ROM drives
-------------

Up to four CD-ROM / DVD-ROM optical disc drives can be attached to the emulated system. The following options apply to the selected drive:

* **Bus:** bus to attach the drive to. ATAPI (IDE) and SCSI are supported.
* **Channel**/**ID:** where to attach the drive on the selected bus. See :ref:`settings/hdd:Adding a new disk` for more information on IDE channels.
* **Speed:** maximum transfer speed for the drive. Up to 72x is supported.

CD-ROM / DVD-ROM disc images can be inserted and removed through the status bar or the *Media* menu.
