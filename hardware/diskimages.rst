Disk images
===========

86Box supports a large variety of disk image formats for the emulated storage drives.

.. raw:: html
  
  <style>
    /* There's no getting around Sphinx automatically sizing columns without some CSS.
       It's that kind of recurring issue a lot of people had but nobody ever addressed. */
    table.docutils.colwidths-given > tbody > tr > td:not(:last-child),
    table.docutils:not(.colwidths-given) > tbody > tr > td {
      white-space: nowrap;
    }
    table.docutils.colwidths-given > colgroup > col:not(:last-child),
    table.docutils:not(.colwidths-given) > colgroup > col {
      width: 0 !important;
    }
  </style>

Hard disk images
----------------

Supported formats:

.. list-table::
  :header-rows: 1
  :widths: 1 1 999

  * - Format
    - File extension
    - Notes

  * - Raw image
    - Many
    - Extensions include: .hdd .ima .img

  * - Japanese FDI
    - .hdi
    -

  * - :doc:`../dev/formats/hdx`
    - .hdx
    -

  * - Virtual Hard Disk
    - .vhd
    - Fixed, Dynamic and Differencing VHDs are supported through the `MiniVHD <https://github.com/shermp/MiniVHD>`_ library.

Hard disk size limits
^^^^^^^^^^^^^^^^^^^^^

There are limits to how big of a hard disk an emulated machine can accept. Such limits will vary depending on the machine's BIOS. The table below lists all important limits applicable to the IDE bus:

.. list-table::
  :header-rows: 1

  * - Limit
    - Disk size
    - Cylinders
    - Heads
    - Sectors

  * - 20-bit CHS
    - 504 MB
    - 1024
    - 16
    - 63

  * - 12-bit cylinder
    - 2015 MB
    - 4095
    - 16
    - 63

  * - ECHS translation
    - 4032 MB
    - 1024
    - 128
    - 63

  * - Revised ECHS
    - 7560 MB
    - 1024
    - 240
    - 63

  * - LBA translation
    - 8064 MB
    - 1024
    - 256
    - 63

  * - 16-bit cylinder
    - 32255 MB
    - 65535
    - 16
    - 63

  * - 28-bit LBA
    - 131071 MB
    - 65536
    - 16
    - 256

The maximum supported disk image size for IDE or SCSI is 131071 MB. Disk overlay software such as *Ontrack Disk Manager* can work around BIOS limits and allow booting of IDE hard drives within the 131071 MB limit, with the same caveats as using such software on a real machine.

Floppy disk images
------------------

Supported formats:

.. list-table::
  :header-rows: 1
  :widths: 1 1 999

  * - Format
    - File extension
    - Notes

  * - Raw image
    - Many
    - Extensions include: .bin .dsk .flp .hdm .ima .img .vfd .xdf

  * - :doc:`../dev/formats/86f`
    - .86f
    - Once loaded, any image can be converted to 86F through the :ref:`status bar <usage/statusbar:|floppy_35| |floppy_525| Floppy drives>` or :ref:`Media menu <usage/menubar:Media>`.

  * - CopyQM
    - .cq / .cqm
    -

  * - DiskDupe
    - .ddi
    -

  * - EZ-DisKlone plus
    - .fdf
    -

  * - Formatted Disk Image
    - .fdi
    - Read only.

  * - HxC MFM
    - .mfm
    - Read only.

  * - ImageDisk
    - .imd
    -

  * - Japanese FDI
    - .fdi
    -

  * - PCjs JSON
    - .json
    - Read only. PCjs 1.0 format only; 2.0 not supported yet.

  * - Teledisk
    - .td0
    - Read only.

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

.. list-table::
  :header-rows: 1
  :widths: 1 1 999

  * - Format
    - File extension
    - Notes

  * - Raw image
    - Many
    - Extensions include: .ima .img

  * - Japanese FDI
    - .mdi / .zdi
    - .mdi for MO, .zdi for ZIP.

CD-ROM / DVD-ROM optical disc images
------------------------------------

Supported formats:

.. list-table::
  :header-rows: 1
  :widths: 1 1 999

  * - Format
    - File extension
    - Notes

  * - Cue sheet
    - .cue + .bin
    - :ref:`Audio tracks are supported. <hardware/diskimages:CD audio>`

  * - ISO
    - .iso
    -

CD audio
^^^^^^^^

Compact Disc Digital Audio (CDDA) playback through the emulated CD-ROM drives is supported on **Cue sheet** images. Audio output is enabled on the first CD-ROM drive and muted on subsequent drives by default; individual drives can be muted or unmuted through the :ref:`status bar <usage/statusbar:|cdrom| CD-ROM drives>` or :ref:`Media menu <usage/menubar:Media>`.

.. note:: Only **raw format** (.bin) tracks are supported. Compressed or otherwise encapsulated audio tracks (.wav, .mp3, .ogg, .flac and other formats) are not supported.

Cassette tape images
--------------------

Supported formats:

.. list-table::
  :header-rows: 1
  :widths: 1 1 999

  * - Format
    - File extension
    - Notes

  * - Raw PCM audio
    - Many
    - Extensions include: .pcm .raw

      Audio format must be unsigned 8-bit mono.

  * - PCE cassette
    - .cas
    -

  * - Wave audio
    - .wav
    - Audio format must be unsigned 8-bit mono.

PCjr cartridge images
---------------------

Supported formats:

.. list-table::
  :header-rows: 1
  :widths: 1 1 999

  * - Format
    - File extension
    - Notes

  * - Raw image
    - Many
    - Extensions include: .a .b .bin

  * - JRipCart
    - .jrc
    -
