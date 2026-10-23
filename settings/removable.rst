|other_removable_devices| Other removable devices
=================================================

The **Other removable devices** page contains settings related to the emulated machine's additional removable storage drives.

|mo| |rdisk_tab| |tape| MO / Removable disk / Tape drives
---------------------------------------------------------

Up to four Magneto-Optical, four removable disk drives and four tape drives can be attached to the emulated machine. The following settings apply to the selected drive:

* **Bus:** storage bus to attach the drive to. ATAPI (IDE), SCSI and LPT (Shuttle EPAT interface for removable disk drives, Iomega Ditto interface for tape drives) are supported. For tape drives, FDC (floppy-based tape) is also supported.
* **Channel**/**ID:** where to attach the drive on the selected storage bus. See :ref:`settings/hdd:Adding a new disk` for more information on IDE channels and SCSI IDs.
* **Type**: drive model to identify as. A list of drive models to choose from is provided; click |clear| to search for models by name. Each model supports different types of media, while the *86BOX* models supports all types.

.. note:: The **LPT** bus requires the specified parallel port to be :ref:`enabled <settings/ports:LPT1-4>` and not in use by a :ref:`PLIP network device <settings/network:Adapter>`, :ref:`CD-ROM drive <settings/floppycdrom:|cdrom| CD-ROM drives>` or :ref:`other parallel device <settings/ports:LPT1-4>`.

MO, removable disk and tape images can be inserted and removed through the :ref:`status bar <usage/statusbar:|rdisk| |zip| |jaz| |syquest| |mo| |tape| Removable disk, MO and tape drives>` or :ref:`Media menu <usage/menubar:Media>`.
