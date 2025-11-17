VM manager
==========

Opening 86Box will start the **virtual machine manager**, which allows for creating, managing, starting and controlling multiple emulated machine configurations.

.. note::
  * This manager is currently a preview, with a limited feature set expanding upon the previous standalone `86Box Manager <https://github.com/86Box/86BoxManager>`_ app. Other managers with more features can still be used.
  * Running 86Box directly no longer creates or starts an emulated machine in the current folder like on previous versions. The ``-P``/``--vmpath`` command line option can be used to start a machine directly instead.
  * The manager can be fully disabled (restoring the behavior of previous 86Box versions when launched without specifying a virtual machine path on the command line) by adding ``vmm_disabled = 1`` to the global configuration file, which is stored at one of the following locations based on the platform:

    * **Windows**: ``C:\Users\[username]\AppData\Local\86Box\86box_global.cfg``
    * **Linux**: ``~/.config/86Box/86box_global.cfg``
    * **macOS**: ``~/Library/Preferences/86Box/86box_global.cfg``

Machine list
------------

The **left-hand side** of the manager window displays a list of all machines found in the :ref:`system directory <preferences>`, along with their current state and icon. Click on a machine to select it.

The following options are available by **right-clicking** a machine:

* **Start:** start the machine.
* **Hard reset:** force a reset of the machine.
* **Force shutdown:** force a shutdown of the machine. If this fails due to a frozen 86Box process, try *Kill*.
* **Ctrl+Alt+Del:** send a *Ctrl+Alt+Del* key combination to the machine.
* **Settings:** open the :doc:`Settings <../settings/index>` window to configure the machine.
* **Change display name:** change the name by which the machine is identified on the manager and 86Box window. Changing this will not rename the machine's folder.
* **Set icon:** change the icon displayed next to the machine on the list.

  * Select an icon from the preset list, or click **Reset** to restore the default icon.

* **Clone:** make a copy of the machine.
* **Kill:** forcibly terminate the machine's 86Box process if one is running.
* **Wipe NVRAM:** clear the machine's CMOS non-volatile memory. On models with Flash ROM, the original BIOS is also reflashed.
* **Delete:** delete the machine, along with **everything** stored within its directory.
* **Open folder:** open the directory where the machine's configuration file is stored.
* **Open printer tray**: open the directory where documents printed by the machine's :ref:`emulated printers <settings/ports:LPT1-4 Device>` are saved.
* **Open screenshots folder**: open the directory where screenshots of the machine are saved.
* **Show config file:** display the contents of the machine's ``86box.cfg`` file for sharing, support requests and bug reports.

Search
^^^^^^

The **search box** at the bottom of the machine list allows for filtering the list by any of the following criteria:

* **Display name** and **folder name**.
* Names of **hardware components** present in the machines, as displayed in the :ref:`details pane <usage/manager:Machine details>`.
* **Image file names** for any media inserted into the machines, including hard disks, floppies and CDs.

Advanced users can :ref:`enable regular expressions <preferences>` to perform more complex searches.

Machine details
---------------

The **right-hand side** of the manager window displays information and controls for the selected machine:

* A **summary** of the machine's :doc:`configuration <../settings/index>`.
* A gallery of **screenshots** saved through :ref:`Take screenshot <usage/menubar:Tools>` or the respective keyboard shortcut.
* A small text area for writing any **notes** about the machine.
* Controls for the machine: **Settings**, **Hard reset**, **Force shutdown**, **Start**/**Pause**, **Ctrl+Alt+Del**.
* The machine's current **status**, with the 86Box process ID if one is running.

Menu bar
--------

The **menu bar** located at the top of the manager window provides controls for the manager as a whole.

File
^^^^

* **New machine:** create a new machine from scratch or from an existing configuration file.
* **Exit:** quit the manager. Requires confirmation if any machines are currently running.

Tools
^^^^^

.. _preferences:

* **Preferences:** open the *Preferences* window, which provides the following options:

  * **System Directory:** view or change the folder where emulated machines are stored.
  * **Language:** select a language for the 86Box user interface.
  * **Remember size & position:** automatically save the manager window's size and position and the machine list's width.
  * **Check for updates on startup:** automatically check for 86Box updates when starting the manager.
  * **Use regular expressions in search box:** enable the use of Perl-syntax regexes to perform more complex searches with the search box.
  * **Color scheme:** select a visual style for the 86Box user interface. *System* uses the operating system's global preference if possible.

.. note::
  * The manager **must be restarted** for any changes to the system directory to take effect.
  * The system directory is **scanned recursively** for machines through their ``86box.cfg`` files.

* **Check for updates:** check for and download any available 86Box version update.

Help
^^^^

* **Documentation:** open the very documentation you're reading.
* **About 86Box:** show credits, license and build information about 86Box.

Status bar
----------

The **status bar** located at the bottom of the manager window displays a **count** of running, paused and total available machines.

Additionally, any information about **available updates** will be displayed in the status bar if :ref:`checking for updates on startup <preferences>` is enabled.
