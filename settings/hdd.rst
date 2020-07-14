Hard disks
==========

The *Hard disks* page contains settings related to the emulated machine's fixed disks.

Hard disk list
--------------

All hard disks attached to the emulated system are listed, with the following information:

* **Bus:** bus the disk is attached to, as well as the disk's bus channel/ID. These can be changed through the *Bus* and *Channel*/*ID* boxes below the list.
* **File:** path to the disk image file.
* **C/H/S:** the disk's amount of cylinders, heads and sectors, respectively.
* **MB:** disk size in megabytes.

Adding a new disk
-----------------

The *New...* button opens a new window allowing you to create an existing hard disk image file.

* **File name:** where to save the disk image file.

   * See :ref:`usage/imageformats:Supported disk image formats` for a list of supported disk image formats.

* **Cylinders/Heads/Sectors:** CHS parameters for the disk image. These boxes control the *Size (MB)* box below.
* **Size (MB):** the disk image's size in MB. This box controls the *Cylinders*, *Heads* and *Sectors* boxes above.

   * See :ref:`limits` for information on disk size limits.

* **Bus:** bus to attach the disk to.
* **Channel**/**ID:** where to attach the disk on the selected bus.

   * The *Channel* value for the IDE bus has two numbers, which correspond to an IDE channel and device, respectively:

     +---------+-----------+------+
     |*Channel*|IDE channel|Device|
     +=========+===========+======+
     |0:0      |Primary    |Master|
     +---------+-----------+------+
     |0:1      |Primary    |Slave |
     +---------+-----------+------+
     |1:0      |Secondary  |Master|
     +---------+-----------+------+
     |1:1      |Secondary  |Slave |
     +---------+-----------+------+
     |2:0      |Tertiary   |Master|
     +---------+-----------+------+
     |2:1      |Tertiary   |Slave |
     +---------+-----------+------+
     |3:0      |Quaternary |Master|
     +---------+-----------+------+
     |3:1      |Quaternary |Slave |
     +---------+-----------+------+

Press the *OK* button to create the disk image file, or *Cancel* to close the window.

Adding an existing disk
-----------------------

The *Existing...* button opens a similar window to the *New...* button, except that it lets you select an existing disk image file. The CHS parameters are guessed from the image's file size, or the file header if the image is of a format which contains a header.

After selecting the image file and checking if the parameters are correct, select the *Bus* and *Channel*/*ID* for the hard disk and press *OK* to add it. Press *Cancel* to close the window.

Removing a disk
---------------

Select a disk on the list and press *Remove* to remove it.

.. _limits:

Size limits
-----------

There are limits to how big of a hard disk an emulated machine can accept. Such limits will vary depending on the machine's age. Here are a few important ones:

+---------------+---------+---------+-----+-------+
|Limit          |Disk size|Cylinders|Heads|Sectors|
+===============+=========+=========+=====+=======+
|20-bit CHS     |504 MB   |1024     |16   |63     |
+---------------+---------+---------+-----+-------+
|Extended CHS   |8032 MB  |1024     |256  |63     |
+---------------+---------+---------+-----+-------+
|65535 cylinders|32255 MB |65535    |16   |63     |
+---------------+---------+---------+-----+-------+
|48-bit LBA     |131071 MB|Not applicable         |
+---------------+---------+-----------------------+

These limits can be worked around (with caveats) by using software such as *Ontrack Disk Manager*, except for the 131071 MB one which is a hard limit of 86Box's hard disk emulation.