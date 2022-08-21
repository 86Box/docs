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

Creating and using disk images
------------------------------

Disk images are a convenient way to transfer files in and out of your machine without the need to configure networking. Perhaps your OS doesn't support networking or you don't want to deal with the added complexity of configuring networking on legacy operating systems.

The tooling available varies by host operating system, ranging from command-line tools to full GUI.

Floppy: mtools (Linux, macOS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `mtools <https://www.gnu.org/software/mtools/>`_ suite is "a collection of utilities to access MS-DOS disks from GNU and Unix without mounting them." With ``mtools`` you can create floppy disk images and copy files to the image. The resulting image can be mounted in 86Box. ``mtools`` can be installed via homebrew on macOS and is available in the standard package repositories on linux.

.. warning:: Never use a tool or utility to write to a disk image that is currently mounted by 86Box. Doing so can lead to unpredictable results, including filesystem corruption.

Creating floppy images
**********************

The following command will create a 1.4M (1440K, double-sided, 18 sectors per track, 80 cylinders) floppy image named ``floppy.img`` with a label of ``LABEL``:

.. code-block::

  mformat -f 1440 -v LABEL -C -i floppy.img ::

The ``-f`` option specifies the format of the floppy being created. The command can be adjusted for format, label, and image name as needed.

Please see the `mtools documentation <https://www.gnu.org/software/mtools/manual/mtools.html#mformat>`_ for more information on the supported formats.

Copying files to floppy images
******************************

The following command will copy ``file1`` and ``file2`` to the floppy image ``floppy.img``:

.. code-block::

  mcopy -i floppy.img file1 file2 ::

Wildcards are also supported with ``mcopy``.

.. note:: The ``::`` is required to let ``mtools`` know there are no more files to copy or arguments to process.

CD-ROM: macOS
^^^^^^^^^^^^^

macOS can natively mount CD-ROM ISOs, but to create them you'll need to open up the terminal.

The following command creates an ISO file named ``cdrom.iso`` with the volume name ``CDROM``.

.. code-block::

  hdiutil makehybrid -iso -joliet -joliet-volume-name "CDROM" -o /path/to/cdrom.iso /path/to/cd/root

In the above example the directory ``/path/to/cd/root`` becomes the root directory of the ISO image.

If you wanted your current working directory to be the ISO root filesystem you could use the following command:

.. code-block::

  hdiutil makehybrid -iso -joliet -joliet-volume-name "CDROM" -o ../cdrom.iso .

.. note:: Make sure the output filename with ``-o`` has a path outside of the filesystem root.

CD-ROM: Linux
^^^^^^^^^^^^^

Linux provides the ``mkisofs`` tool in order to easily create ISO images. The following command creates the ISO file ``cdrom.iso`` which contains the contents of the directory ``/path/to/cd/root``:

.. code-block::

  mkisofs -o cdrom.iso /path/to/cd/root

.. note::
  This package is available in the standard distribution repositories, generally under the ``mkisofs`` or ``genisoimage`` package names.

Disk Image: macOS
^^^^^^^^^^^^^^^^^

macOS can natively mount raw disk images (floppy or hard disk) of types ``FAT16`` and ``FAT32``. Simply double click the file in Finder to mount the image.

For fixed-size ``vhd`` files the following command may work depending your your macOS version:

.. code-block::

  hdiutil attach -imagekey diskimage-class=CRawDiskImage /path/to/your/vhd

.. note:: As with any image file in macOS, the image can only be mounted if macOS can read the underlying filesystem. macOS can read both ``FAT16`` and ``FAT32``.

Various: Windows
^^^^^^^^^^^^^^^^^

On Windows you can use WinImage to create and manipulate disk images.

Windows will also allow you to directly mount a ``vhd`` file in order to copy files. The ``Disk Management`` utility allows you to attach a ``vhd`` file by selecting ``Action -> Attach VHD`` from the menu.

.. warning:: As above, make sure that two different applications never mount the same image file simultaneously. For example, do not mount a ``vhd`` with Windows that is currently mounted by 86Box.

Windows also provides command-line functionality via the ``diskpart`` command. The documentation can located `here <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart>`_.
