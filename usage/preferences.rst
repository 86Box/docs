Preferences
===========

The **Preferences** window allows you to configure options related to 86Box as a whole, which are saved system-wide and apply to all emulated machines as well as the :doc:`manager <manager>`.

.. note:: Any changes made to the preferences in 86Box versions older than 5.0 (saved per-machine) have been reset.

|emulator| Emulator
-------------------

Language
^^^^^^^^

Select a language for the 86Box user interface. Click |clear| to search for languages by their English name. The *Default* button resets back to the system language.

Select media images from program working directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start the first file open/save prompt on the emulated machine's directory. This option is particularly useful for macOS users.

Auto-pause on focus loss / dialog boxes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Automatically pause emulation while the 86Box window is not focused, and/or when the window is covered by a file selector or other dialog boxes.

Ask for confirmation before saving settings / quitting / hard resetting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enable confirmation messages for the specified actions. These options can reenable confirmations after they have been disabled through the *Don't show this message again* box.

Precache CHD files into memory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Load the full uncompressed contents of CHD format :ref:`hardware/diskimages:CD-ROM / DVD-ROM optical disc images` into host RAM ahead of time. May improve emulation performance when using CHD images, especially compressed ones, at the cost of longer disc mounting times and higher 86Box memory usage.

Color scheme
^^^^^^^^^^^^

Select a visual style for the 86Box user interface. *System* uses the operating system's global preference if possible.

|input_devices| Input
---------------------

Mouse sensitivity
^^^^^^^^^^^^^^^^^

Adjust the emulated mouse's tracking sensitivity. The *Default* button resets back to the default sensitivity.

Inhibit multimedia keys
^^^^^^^^^^^^^^^^^^^^^^^

Disable the passthrough of multimedia keys such as :kbd:`Volume Up` and :kbd:`Play/Pause` to the emulated machine.

|key_bindings| Key bindings
---------------------------

View and change keyboard shortcuts for common emulator actions. Most listed actions are also available on the :doc:`menu bar <../usage/menubar>` or the :doc:`toolbar <../usage/toolbar>`; see the respective pages for more information.

The *Clear binding* button removes the shortcut associated with the selected action, and the *Bind* button allows for entering a new shortcut.

.. note:: The :kbd:`F8`\ +\ :kbd:`F12` key combination used for releasing mouse capture in previous 86Box versions can no longer be configured as a shortcut.

|86Box| VM Manager
------------------

System Directory
^^^^^^^^^^^^^^^^

View or change the folder where emulated machines are stored. The *Default* button resets to the default folder.

.. note:: 
  * The manager **must be restarted** for any changes to the system directory to take effect.
  * The system directory is **scanned recursively** for machines through their ``86box.cfg`` files.

Remember size & position
^^^^^^^^^^^^^^^^^^^^^^^^

Automatically save the manager window's size and position and the machine list's width.

Check for updates on startup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Automatically check for 86Box updates when starting the manager.

Use regular expressions in search box
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enable the use of Perl-syntax regexes to perform more complex searches with the manager's search box.

Discord
^^^^^^^

Check *Show running machines in my Discord status* to enable Discord integration, which shares the information specified in *Details shown* with other Discord users.

.. note:: Discord integration requires the Discord desktop app and the 86Box manager to be running. The host OS and Windows DLL limitations from previous 86Box versions no longer apply.
