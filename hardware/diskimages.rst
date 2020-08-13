Disk images
===========

86Box supports a large variety of disk image formats for the emulated disk drives.

.. |86f| replace:: :doc:`../dev/formats/86f`
.. |hdx| replace:: :doc:`../dev/formats/hdx`

Hard disk images
----------------

Supported formats:

+-----------------+--------------+
|Format           |File extension|
+=================+==============+
|**Raw image**    |Many *        |
+-----------------+--------------+
|Japanese FDI     |.hdi          |
+-----------------+--------------+
||hdx|            |.hdx          |
+-----------------+--------------+
|Virtual Hard Disk|.vhd          |
+-----------------+--------------+

\* Raw images come in many extensions, including: img ima

Hard disk size limits
^^^^^^^^^^^^^^^^^^^^^

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

Floppy disk images
------------------

Supported formats:

+--------------------+--------------+
|Format              |File extension|
+====================+==============+
|**Raw image**       |Many *        |
+--------------------+--------------+
||86f|               |.86f          |
+--------------------+--------------+
|CopyQM              |.cqm          |
+--------------------+--------------+
|DiskDupe            |.ddi          |
+--------------------+--------------+
|EZ-DisKlone Plus    |.fdf          |
+--------------------+--------------+
|Formatted Disk Image|.fdi          |
+--------------------+--------------+
|HxC MFM             |.mfm          |
+--------------------+--------------+
|ImageDisk           |.imd          |
+--------------------+--------------+
|Japanese FDI        |.fdi          |
+--------------------+--------------+
|PCjs JSON           |.json         |
+--------------------+--------------+
|Teledisk            |.td0          |
+--------------------+--------------+

\* Raw images come in many extensions, including: img ima flp vfd

Floppy disk detection
^^^^^^^^^^^^^^^^^^^^^

86Box determines the physical media format (sides, tracks per side, sectors per track, bytes per sector) of a floppy disk image through the following methods:

1. Image file header data - not applicable for **Raw** and **DiskDupe** formats;
2. `DOS BIOS Parameter Block <https://en.wikipedia.org/wiki/BIOS_parameter_block>`_ data within the image;
3. If all else fails, a guess is made based on the image file's size.

The BIOS Parameter Block detection method may behave incorrectly with non-DOS floppy disks. Installation floppies for UNIX and Linux are common examples of non-DOS disks. Disabling :ref:`Check BPB <settings/floppycdrom:Floppy drives>` is strongly recommended for accessing these, as an inaccurate BPB detection may result in read errors, data corruption and other issues.

.. note:: When using a **Raw** image of a non-DOS floppy with Check BPB disabled, make sure the image file is not truncated (smaller than its media size), otherwise incorrect behavior may still occur.

MO / ZIP removable disk images
------------------------------

Supported formats:

+---------------------+--------------+
|Format               |File extension|
+=====================+==============+
|**Raw image**        |Many *        |
+---------------------+--------------+
|Japanese FDI         |.mdi (MO)     |
|                     +--------------+
|                     |.zdi (ZIP)    |
+---------------------+--------------+

\* Raw images come in many extensions, including: img ima

CD-ROM / DVD-ROM optical disc images
------------------------------------

Supported formats:

+---------------------+--------------+
|Format               |File extension|
+=====================+==============+
|Cue sheet            |.cue + .bin   |
+---------------------+--------------+
|ISO                  |.iso          |
+---------------------+--------------+

CD audio
^^^^^^^^

Compact Disc Digital Audio (CDDA) playback through the emulated CD-ROM drive is supported on **Cue sheet** images. Audio output is muted on all drives by default; it can be unmuted by unchecking the *Mute* option for the respective drive on the :ref:`status bar <usage/statusbar:|cdrom| |nbsp| CD-ROM drives>` or :ref:`Media menu <usage/menubar:Media>`.

.. note:: Only raw format (.bin) tracks are supported. Compressed or otherwise encapsulated audio tracks (.wav, .mp3, .ogg, .flac and other formats) are not supported.
