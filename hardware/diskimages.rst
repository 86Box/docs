Disk images
===========

86Box supports a large variety of disk image formats for the emulated storage drives.

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

\* Raw image extensions recognized by 86Box include: .hdd .ima .img

Hard disk size limits
^^^^^^^^^^^^^^^^^^^^^

There are limits to how big of a hard disk an emulated machine can accept. Such limits will vary depending on the machine's BIOS. The table below lists all important limits applicable to the IDE bus:

+----------------+---------+---------+-----+-------+
|Limit           |Disk size|Cylinders|Heads|Sectors|
+================+=========+=========+=====+=======+
|20-bit CHS      |504 MB   |1024     |16   |63     |
+----------------+---------+---------+-----+-------+
|12-bit cylinder |2015 MB  |4095     |16   |63     |
+----------------+---------+---------+-----+-------+
|ECHS translation|4032 MB  |1024     |128  |63     |
+----------------+---------+---------+-----+-------+
|Revised ECHS    |7560 MB  |1024     |240  |63     |
+----------------+---------+---------+-----+-------+
|LBA translation |8032 MB  |1024     |255  |63     |
+----------------+---------+---------+-----+-------+
|16-bit cylinder |32255 MB |65535    |16   |63     |
+----------------+---------+---------+-----+-------+
|28-bit CHS      |130558 MB|65535    |255  |63     |
+----------------+---------+---------+-----+-------+
|86Box           |131071 MB|Not applicable         |
+----------------+---------+-----------------------+

The maximum supported disk image size for IDE or SCSI is 131071 MB. Disk overlay software such as *Ontrack Disk Manager* can work around BIOS limits and allow booting of IDE hard drives within the 131071 MB limit, with the same caveats as using such software on a real machine.

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
|CopyQM              |.cq / .cqm    |
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

\* Raw image extensions recognized by 86Box include: .bin .dsk .flp .hdm .ima .img .vfd .xdf

Floppy disk detection
^^^^^^^^^^^^^^^^^^^^^

86Box determines the physical media format (sides, tracks per side, sectors per track, bytes per sector) of a floppy disk image through the following methods:

1. Image file header data - not applicable for **Raw** and **DiskDupe** formats;
2. `DOS BIOS Parameter Block <https://en.wikipedia.org/wiki/BIOS_parameter_block>`_ data within the image;
3. If all else fails, a guess is made based on the image file's size.

The BIOS Parameter Block detection method may behave incorrectly with non-DOS floppy disks. Installation floppies for UNIX and Linux are common examples of non-DOS disks. Disabling :ref:`Check BPB <settings/floppycdrom:Floppy drives>` is strongly recommended when accessing these, as an inaccurate BPB detection may result in read errors, data corruption and other issues.

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

\* Raw image extensions recognized by 86Box include: .ima .img

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

Compact Disc Digital Audio (CDDA) playback through the emulated CD-ROM drives is supported on **Cue sheet** images. Audio output is enabled on the first CD-ROM drive and muted on subsequent drives by default; individual drives can be muted or unmuted through the :ref:`status bar <usage/statusbar:|cdrom| CD-ROM drives>` or :ref:`Media menu <usage/menubar:Media>`.

.. note:: Only **raw format** (.bin) tracks are supported. Compressed or otherwise encapsulated audio tracks (.wav, .mp3, .ogg, .flac and other formats) are not supported.

Cassette tape images
--------------------

Supported formats:

+---------------------+--------------+
|Format               |File extension|
+=====================+==============+
|**Raw PCM audio**    |Many *        |
+---------------------+--------------+
|PCE cassette         |.cas          |
+---------------------+--------------+
|Wave audio           |.wav          |
+---------------------+--------------+

\* Raw audio extensions recognized by 86Box include: .pcm .raw

PCjr cartridge images
---------------------

Supported formats:

+---------------------+--------------+
|Format               |File extension|
+=====================+==============+
|**Raw image**        |Many *        |
+---------------------+--------------+
|JRipCart             |.jrc          |
+---------------------+--------------+

\* Raw image extensions recognized by 86Box include: .a .b .bin
