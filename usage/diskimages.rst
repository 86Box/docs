Disk images
===========

86Box supports a large variety of disk image formats for the emulated drives.

Hard disk images
----------------

Supported formats:

+---------------------+--------------+
|Format               |File extension|
+=====================+==============+
|**Raw image**        |Many *        |
+---------------------+--------------+
|Japanese FDI         |.hdi          |
+---------------------+--------------+
|:doc:`../formats/hdx`|.hdx          |
+---------------------+--------------+
|Virtual Hard Disk    |.vhd          |
+---------------------+--------------+

\* Raw images come in many extensions, including: img ima

Floppy disk images
------------------

Supported formats:

+---------------------+--------------+
|Format               |File extension|
+=====================+==============+
|**Raw image**        |Many *        |
+---------------------+--------------+
|:doc:`../formats/86f`|.86f          |
+---------------------+--------------+
|Formatted Disk Image |.fdi          |
+---------------------+--------------+
|CopyQM               |.cqm          |
+---------------------+--------------+
|DiskDupe             |.ddi          |
+---------------------+--------------+
|EZ-DisKlone Plus     |.fdf          |
+---------------------+--------------+
|HxC MFM              |.mfm          |
+---------------------+--------------+
|ImageDisk            |.imd          |
+---------------------+--------------+
|Japanese FDI         |.fdi          |
+---------------------+--------------+
|PCjs JSON            |.json         |
+---------------------+--------------+
|Teledisk             |.td0          |
+---------------------+--------------+

\* Raw images come in many extensions, including: img ima flp vfd

Floppy disk detection
^^^^^^^^^^^^^^^^^^^^^

86Box detects the physical media format (sides, tracks per side, sectors per track, bytes per sector) of a floppy disk image through the following methods:

1. Data stored in the file header, except for Raw and DiskDupe formats where there is none.
2. Data stored in the `DOS BIOS Parameter Block <https://en.wikipedia.org/wiki/BIOS_parameter_block>`_.
3. If all else fails, a guess is made based on the file size.

The BIOS Parameter Block detection may result in incorrect behavior on non-DOS-compatible floppy disks. Installation floppies for UNIX and Linux are common examples of non-DOS-compatible disks. Disabling the :ref:`Check BPB <settings/floppycdrom:Floppy drives>` setting is strongly recommended for accessing these, as the inaccurate BPB detection may result in read errors, data corruption and other issues.

.. note:: When using a raw image of a non-DOS-compatible floppy with the Check BPB setting disabled, make sure the image file has the right size for its media type, otherwise incorrect behavior may still occur.

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

Compact Disc Digital Audio (CDDA) is supported on *Cue sheet* images. CD audio playback is muted on all drives by default; it can be unmuted by unchecking the *Mute* box for the respective CD-ROM drive in the status bar or the Media menu.

.. note:: Only raw format (.bin) tracks are supported. Compressed or otherwise encapsulated audio tracks (.wav, .mp3, .ogg, .flac and other formats) are not supported.
