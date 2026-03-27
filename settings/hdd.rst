.. include:: /include.rst

|hard_disk| Hard disks
======================

The **Hard disks** page contains settings related to the emulated machine's fixed disks.

Hard disk list
--------------

All hard disks attached to the emulated machine are listed, with the following information:

* **Bus:** storage bus the disk is attached to, as well as the disk's bus channel or ID. These can be changed through the *Bus* and *Channel*/*ID* boxes below the list.
* **File:** path to the disk image file.
* **Geometry:** disk size in cylinders, heads, sectors and MiB, respectively.
* **Model:** :ref:`emulated model profile <settings/hdd:Model / Audio>` for the disk.

Model / Audio
-------------

The *Model* box below the hard disk list determines the **disk model** to emulate. Model profiles adjust the disk's identification data, as well as its performance according to rotation speed, physical layout and cache size. Generic profiles adjust performance to match an average period-correct disk, while the **RAM Disk** profile runs the disk as fast as the host can manage.

Additionally, the *Audio* box allows for emulating the mechanical sounds of a real hard disk drive. A list of drive models to choose from is provided, according to the selected model's spindle speed; the *None* option disables these sounds.

Adding a new disk
-----------------

The *New...* button opens a new window allowing you to create an existing hard disk image file.

* **File name:** where to save the disk image file. See :ref:`hardware/diskimages:Hard disk images` for a list of supported image formats.
* **Cylinders/Heads/Sectors:** CHS parameters for the disk image. These boxes control the *Size (MB)* box below.
* **Size (MB):** the disk image's size in MB. This box controls the *Cylinders*, *Heads* and *Sectors* boxes above. There are limits to how big a hard disk image can be; see :ref:`hardware/diskimages:Hard disk size limits` for more information.
* **Bus:** storage bus to attach the disk to.
* **Channel**/**ID:** where to attach the disk on the selected storage bus. Channels/IDs that are already in use cannot be selected.

  * On IDE disks, the first number corresponds to the IDE channel, and the second number corresponds to the Master/Slave position:

    +-----+----------+------+
    |Value|Channel   |Device|
    +=====+==========+======+
    |0:0  |Primary   |Master|
    +-----+----------+------+
    |0:1  |Primary   |Slave |
    +-----+----------+------+
    |1:0  |Secondary |Master|
    +-----+----------+------+
    |1:1  |Secondary |Slave |
    +-----+----------+------+
    |2:0  |Tertiary  |Master|
    +-----+----------+------+
    |2:1  |Tertiary  |Slave |
    +-----+----------+------+
    |3:0  |Quaternary|Master|
    +-----+----------+------+
    |3:1  |Quaternary|Slave |
    +-----+----------+------+
   
  * On SCSI disks, the first number corresponds to the controller's index, starting from 0 and following the order of: on-board SCSI controllers if present, then :ref:`sound cards <settings/sound:Sound card #1-#4>` with SCSI if present, then :ref:`configured SCSI controllers <settings/storage:|scsi_controllers| SCSI controllers>`; the second number is the SCSI ID within that controller:

    +-----+------------+-------+
    |Value|Controller  |SCSI ID|
    +=====+============+=======+
    |0:00 |Controller 1|0      |
    +-----+            +-------+
    ||vel||            ||vel|  |
    +-----+            +-------+
    |0:15 |            |15     |
    +-----+------------+-------+
    |1:00 |Controller 2|0      |
    +-----+            +-------+
    ||vel||            ||vel|  |
    +-----+            +-------+
    |1:15 |            |15     |
    +-----+------------+-------+
    |2:00 |Controller 3|0      |
    +-----+            +-------+
    ||vel||            ||vel|  |
    +-----+            +-------+
    |2:15 |            |15     |
    +-----+------------+-------+
    |3:00 |Controller 4|0      |
    +-----+            +-------+
    ||vel||            ||vel|  |
    +-----+            +-------+
    |3:15 |            |15     |
    +-----+------------+-------+

  * On MFM/RLL, XTA and ESDI disks, the second number is 0 for the first drive on the controller, and 1 for the second drive.

.. note:: If the disk is attached to a channel or controller that doesn't exist, such as the tertiary IDE channel with no tertiary IDE controller present, it will be effectively disabled.

* **Model:** :ref:`model profile <settings/hdd:Model / Audio>` to use for the disk.
* **Image Format:** file format to use for the disk image.
* **Block Size:** size of each dynamic data block in a dynamic or differencing VHD image. The default 2 MB is ideal in most cases.

Press the *OK* button to create the disk image file, or *Cancel* to close the window without adding the disk.

Adding an existing disk
-----------------------

The *Existing...* button opens a similar window to the *New...* button, except that it lets you select an existing disk image file. The CHS parameters are guessed from the image's file size, or the file header if the image is of a format which contains a header.

After selecting the image file and checking if the parameters are correct, select the *Bus* and *Channel*/*ID* for the hard disk and press *OK* to add it. Press *Cancel* to close the window without adding the disk.

Using physical disks
^^^^^^^^^^^^^^^^^^^^

Real disks connected to the host system can be attached to the emulated machine, as long as they meet the :ref:`131071 MB size limit and any other limits set by the emulated hardware <hardware/diskimages:Hard disk size limits>`. Use the *Existing...* button and set *File name* to:

* **Windows:** ``\\.\PhysicalDriveX`` where ``X`` is the disk number displayed in the Disk Management (``diskmgmt.msc``) tool.
* **Linux:** the path to the disk's block device, such as ``/dev/sdb`` for example.

The *Cylinders*, *Heads*, *Sectors* and *Size (MB)* parameters are set automatically when *OK* is pressed.

.. note::
  * You must have the correct permissions to access the raw physical disk. This entails running 86Box as administrator on Windows and adjusting block device permissions on Linux.
  * Any partitions on the disk must be unmounted to prevent data corruption. On Windows, use Disk Management to unmount the disk by right-clicking it and selecting *Offline* (not available on removable drives) or by removing all drive letters assigned to it.

Removing a disk
---------------

Select a disk on the list and press *Remove* to remove it.
