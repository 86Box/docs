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

The maximum supported disk image size for IDE or SCSI is 131071 MB. Disk overlay software such as the :ref:`settings/storage:Vision Systems LBA Enhancer` or *Ontrack Disk Manager* can work around BIOS limits and allow booting of larger IDE hard drives, with the same caveats as using such software on a real machine.

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

Creating and using disk images
------------------------------

Disk images are a convenient way to transfer files in and out of emulated machines, without the complexity of setting up networking. There are many different command line and GUI tools available for manipulating disk images on each host operating system.

.. warning:: Before editing or mounting any disk images, make sure they are **not in use** by any emulated machine that is currently running.

Editing and mounting on Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**WinImage** or **PowerISO** can be used to create and manipulate disk images on Windows.

VHD images can be natively mounted by double-clicking them on File Explorer, or through the **Disk Management** tool (``diskmgmt.msc``): select *Action* > *Attach VHD* to mount an image. Eject the drive through File Explorer to unmount. The ``diskpart`` `command line utility <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart>`_ also provides VHD mounting/unmounting functionality.

Mounting on macOS
^^^^^^^^^^^^^^^^^

macOS can natively mount raw hard disk and floppy images formatted as **FAT** and its variants. Open the image in Finder to mount it, and eject the disk to unmount.

Editing on Linux and macOS
^^^^^^^^^^^^^^^^^^^^^^^^^^

The `mtools <https://www.gnu.org/software/mtools/>`_ suite is "a collection of utilities to access MS-DOS disks from GNU and Unix without mounting them". It can be used to create floppy disk images and directly copy files to them. The ``mtools`` package is available on many Linux distributions, as well as macOS Homebrew.

Creating floppy images
**********************

The following command will create a 1.44M (1440 KB, double-sided, 18 sectors per track, 80 cylinders) floppy image named ``floppy.img`` with a label of ``LABEL``:

.. code-block::

  mformat -f 1440 -v LABEL -C -i floppy.img ::

The ``-f`` option specifies the format of the floppy being created. The command can be adjusted for format, label, and image name as needed. Refer to the `mtools documentation <https://www.gnu.org/software/mtools/manual/mtools.html#mformat>`_ for a full list of supported formats.

Copying files to floppy images
******************************

The following command will copy ``file1`` and ``file2`` to the floppy image ``floppy.img``:

.. code-block::

  mcopy -i floppy.img file1 file2 ::

Wildcards are also supported with ``mcopy``.

.. note:: The ``::`` is required to let ``mtools`` know there are no more files to copy or arguments to process.

Mounting on Linux
*****************

Linux can natively mount raw disk images (floppy or hard disk) of most types (``FAT`` and ``NTFS`` included).  The easiest path is to use `losetup <https://manpages.debian.org/bookworm/mount/losetup.8.en.html>`_ so that partitions can be properly recognized.  Floppies are not normally partitioned, and you can use `mount <https://manpages.debian.org/bookworm/mount/mount.8.en.html>`_ directly.

All following commands must be run as root:

.. code-block:: sh

   losetup -fP /path/to/86box/hdd
   losetup                         # to verify which loopback device was set up.
                                   # Assuming /dev/loop0 was selected:
   mount /dev/loop0p1 /mnt         # Mount the first partition at /mnt

Disk images should at least be unmounted before running 86Box again, and preferably detached too:

.. code-block::

   umount /mnt
   losetup -d /dev/loop0

Partitionless media can be mounted directly:

.. code-block::

   mount /path/to/86box/fdd /mnt

VHD images may be mounted via `qemu-nbd <https://manpages.debian.org/bookworm/qemu-utils/qemu-nbd.8.en.html>`_:

.. code-block::

   modprobe nbd max_part=16
   qemu-nbd -f vpc -c /dev/nbd0 /path/to/86box/hdd
   mount /dev/nbd0p1 /mnt
     # After doing some work...
   umount /mnt
   qemu-nbd -d /dev/nbd0
