ROM set
=======

86Box relies on a set of ROM dumps gathered from physical hardware to emulate it. This includes the system BIOS, as well as any option ROMs used by expansion cards.

The ROM set is organized into several directories for each device type, each of which contains futher subdirectories for each machine or device model or category.

.. note:: The expected file names of the ROM dumps and their locations within the set are hardcoded in the emulator. If you rename them or add your own dumps with different file names, the emulator will not be able to make use of them.

Search path
-----------

The emulator utilizes a search path mechanism to locate ROMs. By default, the following locations are considered:

1. ``roms`` subdirectory in the VM path
2. ``roms`` subdirectory in the same directory as the emulator executable
3. Platform-specific locations

A custom location can be specified by using the ``-R`` or ``--rompath`` command line argument, which then precedes any other considered locations.

.. rubric:: Windows

The following locations are searched on Windows:

1. ``%LOCALAPPDATA%\86Box\roms``
2. ``%PROGRAMDATA%\86Box\roms``

.. rubric:: Unix

86Box honors the XDG base directory specification on Linux and other Unix-compatible platforms. The following locations are searched:

1. ``$XDG_DATA_HOME/86Box/roms``
2. ``86Box/roms`` subdirectory in each path listed in ``$XDG_DATA_DIRS``
   
This usually resolves to ``~/.local/share/86Box/roms``, ``/usr/local/share/86Box/roms`` and ``/usr/share/86Box/roms`` (in order).

.. rubric:: macOS

The following locations are searched on macOS:

1. ``~/Library/Application Support/net.86box.86Box/roms``
2. ``/Library/Application Support/net.86box.86Box/roms``

.. tip:: The list of all paths searched when loading ROMs is printed to the log and standard output when 86Box starts.
