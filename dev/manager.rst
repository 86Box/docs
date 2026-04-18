Manager interface
=================

The manager interface allows third party applications to determine the status of 86Box instances and to issue commands to them.

JSON-based protocol
-------------------

This is the latest protocol introduced with 86Box 5.0 and used by the built-in virtual machine manager.

The manager attaches to the 86Box instance by setting the ``VMM_86BOX_SOCKET`` environment variable to the full name of a named pipe on Windows or a Unix domain socket on Unix-compatible operating systems. The pipe or socket must already exist when launching 86Box.

The messages have following format:

.. flat-table:: Message schema
  :header-rows: 1
  :widths: 68 55 540

  * - Name
    - Type
    - Description

  * - ``type``
    - String
    - Determines the message sender:

      * ``Client``: Sent by the 86Box instance.
      * ``VMManager``: Sent by the manager.

  * - ``version``
    - String
    - 86Box version

  * - ``message``
    - String
    - Message name

  * - ``params``
    - Object
    - Message parameters, contents are specific to each message

The following messages are sent to the manager by the 86Box instance:

.. flat-table:: Client messages
  :header-rows: 1
  :widths: 218 477

  * - Name
    - Description

  * - ``WindowBlocked``
    - Sent when the main window is blocked due to a modal dialog box being shown.

  * - ``WindowUnblocked``
    - Sent when the main window is unblocked.

  * - ``RunningStateChanged``
    - Sent when the virtual machine transitions to a different state.

      **Parameters:**

      * ``status`` (number)

        * ``0``: Running
        * ``1``: Paused
        * ``2``: Waiting for user input
        * ``3``: Paused and waiting for user input

  * - ``ConfigurationChanged``
    - Sent when the virtual machine configuration changes.

  * - ``WinIdMessage``
    - Sent upon startup to pass the platform-specific window handle.

      **Parameters:**

      * ``params`` (number): Window handle

  * - ``GlobalConfigurationChanged``
    - Sent when the global configuration changes. The manager should relay this message to all running instances.

The following messages are sent to the instance by the manager:

.. flat-table:: Server messages
  :header-rows: 1
  :widths: 218 477

  * - Name
    - Description

  * - ``Pause``
    - Pauses or unpauses the virtual machine.

  * - ``CtrlAltDel``
    - Sends the Ctrl+Alt+Delete keyboard sequence to the virtual machine.

  * - ``ShowSettings``
    - Opens the Settings dialog.

  * - ``ResetVM``
    - Triggers a hard reset

  * - ``RequestShutdown``
    - Sends a shutdown request, showing a confirmation prompt if enabled.

  * - ``ForceShutdown``
    - Forces a shutdown.

  * - ``GlobalConfigurationChanged``
    - Sent when the global configuration changes.


Plaintext-based protocol
------------------------

This is an earlier protocol introduced with 86Box 3.3, which uses plaintext messages instead of structured JSON.

The manager attaches to the 86Box instance by setting the ``86BOX_MANAGER_SOCKET`` environment variable to the full name of a named pipe on Windows or a Unix domain socket on Unix-compatible operating systems. The pipe or socket must already exist when launching 86Box.

Commands sent by the manager must be followed by a new line character (``\n``). The following commands are recognized:

.. flat-table:: Commands
  :header-rows: 1
  :widths: 139 556

  * - Name
    - Description

  * - ``showsettings``
    - Opens the Settings dialog.

  * - ``pause``
    - Pauses or unpauses the virtual machine.

  * - ``cad``
    - Sends the Ctrl+Alt+Delete keyboard sequence to the virtual machine.

  * - ``reset``
    - Triggers a hard reset.

  * - ``shutdown``
    - Sends a shutdown request, showing a confirmation prompt if enabled.

  * - ``shutdownnoprompt``
    - Forces a shutdown.

Furthermore, the emulator writes a ``1`` to the socket when the main window is blocked due to a modal dialog box being shown, and a ``0`` when the window is unblocked.


Window message protocol (Windows-only)
--------------------------------------

.. warning:: This protocol is **deprecated** since 86Box 5.0 and will be removed in a future release of 86Box. It is only being documented here for completeness sake.

This is the original protocol used by 86Box Manager, which uses Windows window messages for communication between the manager and the 86Box instance.

The manager attaches to the instance by passing an arbitrary ``uint64_t`` identifier and its own window handle, both formatted as hexadecimal numbers and separated by a comma via the ``-H`` / ``--hwnd`` command line argument, i.e. ``-H <vm_id>,<hwnd>``.

All window messages sent by the emulator include the emulator's main window handle in ``LPARAM``. Use the ``WM_SENDHWND`` window message sent upon 86Box startup to match this to the identifier provided in the command line.

.. flat-table:: Windows messages
  :header-rows: 1
  :widths: 139 70 78 408

  * - Name
    - Value
    - Sent by
    - Description

  * - ``WM_SHOWSETTINGS``
    - ``0x8889``
    - Manager
    - Opens the Settings dialog.

  * - ``WM_PAUSE``
    - ``0x8890``
    - Manager
    - Pauses or unpauses the virtual machine.

  * - ``WM_SENDHWND``
    - ``0x8891``
    - 86Box
    - Sent when the main window is first shown. ``WPARAM`` contains the virtual machine ID provided by the manager

  * - ``WM_HARDRESET``
    - ``0x8892``
    - Manager
    - Triggers a hard reset

  * - ``WM_SHUTDOWN``
    - ``0x8893``
    - Manager
    - Triggers a shutdown.

      * ``WPARAM`` = 0: Shows the confirmation prompt
      * ``WPARAM`` = 1: Forces the shutdown

  * - ``WM_CTRLALTDEL``
    - ``0x8894``
    - Manager
    - Sends the Ctrl+Alt+Delete keyboard sequence to the virtual machine.

  * - ``WM_SENDSTATUS``
    - ``0x8895``
    - 86Box
    - Sent when the virtual machine transitions to paused state or back.

      * ``WPARAM`` = 0: Execution has been paused
      * ``WPARAM`` = 1: Execution has been resumed

  * - ``WM_SENDDLGSTATUS``
    - ``0x8896``
    - 86Box
    - Sent when the emulator is waiting for user input in a modal dialog box.

      * ``WPARAM`` = 0: Dialog box has opened
      * ``WPARAM`` = 1: Dialog box has closed

  * - ``WM_HAS_SHUTDOWN``
    - ``0x8897``
    - 86Box
    - Sent when the virtual machine shuts down.
