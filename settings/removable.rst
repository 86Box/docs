.. include:: /include.rst

|other_removable_devices| Other removable devices
=================================================

The **Other removable devices** page contains settings related to the emulated machine's additional removable storage drives.

MO / ZIP drives
---------------

Up to four Magneto-Optical and four Iomega ZIP disk drives can be attached to the emulated system. The following settings apply to the selected drive:

* **Bus:** storage bus to attach the drive to. ATAPI (IDE) and SCSI are supported.
* **Channel**/**ID:** where to attach the drive on the selected storage bus. See :ref:`settings/hdd:Adding a new disk` for more information.
* **Type** (MO only): drive model to identify as. A list of drive models to choose from is provided. Each model supports different types of MO media, while the *86BOX* model supports all types.
* **ZIP 250** (ZIP only): enable the drive to read and write 250 MB ZIP disks.

MO / ZIP disk images can be inserted and removed through the :ref:`status bar <usage/statusbar:|zip| |mo| ZIP and MO drives>` or :ref:`Media menu <usage/menubar:Media>`.
