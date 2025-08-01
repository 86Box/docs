.. include:: /include.rst

Status bar
==========

The status bar located at the bottom of the 86Box window provides icons related to devices attached to the emulated machine. Move your mouse cursor over an icon to see what device it represents. **Most icons can be clicked on** to access options related to their respective devices, which are listed below, and image files can be dropped on the icons for removable media devices such as floppy and CD-ROM drives. Additionally, green or red indicator lights will appear on an icon when its device is in use, denoting reads and writes respectively, unless :ref:`Update status bar icons <usage/menubar:Tools>` is disabled.

|cassette| Cassette deck
------------------------

A cassette tape icon will appear if :ref:`IBM cassette emulation <settings/storage:Cassette>` is enabled.

* **New image:** create a new cassette tape image file.
* **Existing image:** insert a :ref:`cassette tape image file <hardware/diskimages:Cassette tape images>` into the deck. Dragging and dropping an image file on the icon will also load it.
* **Existing image (Write-protected):** insert a cassette tape image file into the deck as a read-only tape.
* A history of the last few images that were loaded into the deck. Click on an entry to load it back.
* **Record:** start recording data to the cassette tape. Not available if the tape is read-only.
* **Play:** start playing the cassette tape.
* **Rewind to the beginning:** rewind the cassette tape to its beginning.
* **Fast forward to the end:** fast forward the cassette tape to its end.
* **Eject:** remove the currently-inserted cassette tape from the deck.

|cartridge| PCjr cartridges
---------------------------

Two cartridge icons will appear if the **IBM PCjr** is being emulated. Each icon corresponds to a cartridge slot on the PCjr's front panel.

* **Image:** insert a :ref:`cartridge image file <hardware/diskimages:PCjr cartridge images>` into this slot. Inserting a cartridge will reset the PCjr. Dragging and dropping an image file on the icon will also load it.
* A history of the last few images that were loaded into this slot. Click on an entry to load it back.
* **Eject:** remove the currently-inserted cartridge from this slot.

|floppy_35| |floppy_525| Floppy drives
--------------------------------------

A 3.5" or 5.25" floppy icon will appear for each configured :ref:`floppy drive <settings/floppycdrom:Floppy drives>`.

* **New image:** create a new disk image file. Opens the *New Image* window, which lets you select the image size and where to save the file.
* **Existing image:** insert a :ref:`disk image file <hardware/diskimages:Floppy disk images>` into this drive. Dragging and dropping an image file on the icon will also load it.
* **Existing image (Write-protected):** insert a disk image file into this drive as a read-only disk.
* A history of the last few images that were loaded into this drive. Click on an entry to load it back.
* **Export to 86F:** convert the currently-inserted disk image file to 86Box's :doc:`../dev/formats/86f` surface image format. You will be asked where to save the converted file.
* **Eject:** remove the currently-inserted disk from this drive.

|cdrom| CD-ROM drives
---------------------

A CD icon will appear for each configured :ref:`CD-ROM drive <settings/floppycdrom:CD-ROM drives>`.

* **Mute:** mute any :ref:`hardware/diskimages:CD audio` played through this drive's analog output. CD audio is unmuted by default on the first configured CD-ROM drive.
* **Image:** insert a :ref:`CD-ROM or DVD-ROM disc image file <hardware/diskimages:CD-ROM / DVD-ROM optical disc images>` into this drive. Dragging and dropping an image file on the icon will also load it.
* **Folder:** insert a virtual CD-ROM or DVD-ROM with the contents of a host folder into this drive. Dragging and dropping a folder on the icon will also load it.
* A history of the last few images, folders or host drives that were loaded into this drive. Click on an entry to load it back.
* A list of host CD-ROM or DVD-ROM drives available for passthrough. Click on an entry to attach it to the emulated drive.
* **Eject:** remove any disc inserted into this drive, or detach a host drive.

|zip| |mo| Removable disk and MO drives
---------------------------------------

A removable disk or MO icon will appear for each configured :doc:`additional removable storage drive <../settings/removable>`.

* **New image:** create a new disk image file. Opens the *New Image* window, which lets you select the image size and where to save the file.
* **Existing image:** insert a :ref:`disk image file <hardware/diskimages:MO / removable disk images>` into this drive. Dragging and dropping an image file on the icon will also load it.
* **Existing image (Write-protected):** insert a disk image file into this drive as a read-only disk.
* A history of the last few images that were loaded into this drive. Click on an entry to load it back.
* **Eject:** remove the currently-inserted disk from this drive.

|hard_disk| Hard disks
----------------------

A hard disk icon will appear for each configured :doc:`hard disk bus <../settings/hdd>`. For example, if you have both IDE and SCSI hard disks configured, two hard disk icons will appear: one representing all IDE disks, and another one representing all SCSI disks. No options are available.

|network| Network
-----------------

A network icon will appear for each configured :doc:`network card <../settings/network>`.

* **Connected:** connect this card to its network. Network cards with link state detection support will report a disconnected cable if this option is unchecked.

|sound| Sound
-------------

This icon is always present, providing options to control all audio produced by the emulated machine's PC speaker, :doc:`sound cards <../settings/sound>` and other sound hardware.

* **Mute:** mute all audio. You can alternatively press *Ctrl+Alt+M* (:ref:`customizable <settings/input:Key bindings>`) to mute or unmute audio.
* **Sound gain:** open a gain control, which allows for increasing the loudness of all audio.

.. note:: Sound options do not apply to MIDI music sent to a software synthesizer through the :ref:`System MIDI <settings/sound:MIDI Out Device>` device, as these synthesizers are external to 86Box.

Additional information area
---------------------------

This area, located to the right of the icons described above, contains additional information which may be provided by components such as the :ref:`settings/peripherals:ISABugger` and :ref:`settings/peripherals:POST card`.

Monitor sleep mode
^^^^^^^^^^^^^^^^^^

The *Monitor in sleep mode* message will be displayed if the emulated monitor has been put into DPMS sleep mode by the operating system. Pressing a key or moving the mouse is often enough to wake the monitor up.

MT-32 display
^^^^^^^^^^^^^

Any text messages sent to the LCD screen of an :ref:`emulated Roland MT-32/CM-32L synthesizer <settings/sound:MIDI Out Device>` are displayed here.

ISABugger
^^^^^^^^^

The ISABugger's hexadecimal displays and LED banks are displayed here. See :doc:`../hardware/isabugger` for more information.

POST card
^^^^^^^^^

The leftmost hexadecimal value is the most recent POST code reported, while the rightmost value is the second most recent code, like on a real dual-display POST card. A value of ``--`` indicates that no POST code has been reported yet.

.. note:: The additional information area can only be used by one component at a time. The MT-32 display has the highest priority, followed by the monitor sleep mode message, then the ISABugger and POST card with the same priority (taking over whenever they're written to).

|num_lock_off| |caps_lock_off| |scroll_lock_off| Keyboard indicators
--------------------------------------------------------------------

Indicator lights for |num_lock_off_small| Num Lock, |caps_lock_off_small| Caps Lock and |scroll_lock_off_small| Scroll Lock on the emulated keyboard are displayed on the right side of the status bar.

A |kana_lock_off_small| Kana Lock indicator is also displayed when emulating a machine with a Japanese AX keyboard.
