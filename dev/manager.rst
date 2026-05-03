Manager interface
=================

The manager interface allows third-party applications to determine the status of 86Box instances and issue commands to them.

JSON protocol
-------------

This is the latest interface protocol, introduced with 86Box 5.0 and used by the built-in :doc:`../usage/manager`.

The manager attaches to the 86Box instance by launching it with the ``VMM_86BOX_SOCKET`` environment variable set to the full path to a named pipe on Windows or a ``SOCK_STREAM`` domain socket on Unix-compatible operating systems. The pipe/socket must already exist.

Messages are sent as ``QString`` objects via ``QDataStream`` version ``Qt_5_7`` (``17``).

JSON messages are formatted as such:

.. flat-table::
  :header-rows: 1
  :widths: 68 55 540

  * - Name
    - Type
    - Description

  * - ``type``
    - String
    - ``"Client"`` for incoming messages from the 86Box instance, or ``"VMManager"`` for outgoing messages from the manager.

  * - ``version``
    - String
    - 86Box version.

  * - ``message``
    - String
    - Message name.

  * - ``params``
    - Object
    - Message parameters, if applicable. Contents are specific to each message.

The following messages are sent by the 86Box instance to the manager:

.. flat-table::
  :header-rows: 1
  :widths: 218 477
  :class: longtable

  * - Name
    - Description

  * - ``WindowBlocked``
    - Sent when the main window is blocked due to a modal dialog box being shown.

  * - ``WindowUnblocked``
    - Sent when the main window is unblocked.

  * - ``RunningStateChanged``
    - Sent when the emulated machine transitions to a new state. The ``status`` (number) parameter can be one of:

      * ``0``: Running
      * ``1``: Paused
      * ``2``: Waiting for user input
      * ``3``: Paused and waiting for user input

  * - ``ConfigurationChanged``
    - Sent when the emulated machine's :doc:`settings <../settings/index>` are changed.

  * - ``WinIdMessage``
    - Sent upon startup to pass the platform-specific window handle through the ``params`` (number) parameter.

  * - ``GlobalConfigurationChanged``
    - Sent when :doc:`preferences <../usage/preferences>` are changed. The manager should respond by sending a ``GlobalConfigurationChanged`` message to all running instances.

The following messages can be sent to the instance by the manager:

.. flat-table::
  :header-rows: 1
  :widths: 218 477
  :class: longtable

  * - Name
    - Description

  * - ``Pause``
    - Pause or unpause the emulated machine.

  * - ``CtrlAltDel``
    - Send a *Ctrl+Alt+Delete* keyboard sequence to the emulated machine.

  * - ``ShowSettings``
    - Open the emulated machine's :doc:`Settings window <../settings/index>`.

  * - ``ResetVM``
    - Force a reset of the emulated machine.

  * - ``RequestShutdown``
    - Send a shutdown request, which displays a confirmation prompt if enabled.

  * - ``ForceShutdown``
    - Force a shutdown.

  * - ``GlobalConfigurationChanged``
    - Update :doc:`preferences <../usage/preferences>`. Should be sent to all running instances after receiving a ``GlobalConfigurationChanged`` message from one instance.


Plain text protocol
-------------------

This earlier protocol, introduced in 86Box 3.3, uses plain text messages instead of structured JSON.

The manager attaches to the 86Box instance by launching it with the ``86BOX_MANAGER_SOCKET`` environment variable set to the full path to a named pipe on Windows or a ``SOCK_STREAM`` domain socket on Unix-compatible operating systems. The pipe/socket must already exist.

Commands sent by the manager must be followed by a newline character (``\n``). The following commands are recognized:

.. flat-table::
  :header-rows: 1
  :widths: 139 556
  :class: longtable

  * - Name
    - Description

  * - ``showsettings``
    - Open the emulated machine's :doc:`Settings window <../settings/index>`.

  * - ``pause``
    - Pause or unpause the emulated machine.

  * - ``cad``
    - Send a *Ctrl+Alt+Delete* keyboard sequence to the emulated machine.

  * - ``reset``
    - Force a reset of the emulated machine.

  * - ``shutdown``
    - Send a shutdown request, which displays a confirmation prompt if enabled.

  * - ``shutdownnoprompt``
    - Force a shutdown.

Furthermore, the emulator writes an ASCII ``1`` to the pipe/socket when the main window is blocked by a modal dialog box, and an ASCII ``0`` when the window is unblocked.


Window message protocol (Windows-only)
--------------------------------------

.. warning:: This protocol is **deprecated** as of 86Box 5.0 and will be removed in a future release. It is documented here for completeness only.

This earlier protocol, used by the legacy 86Box Manager application., uses Windows window messages sent to the emulator window and received on a specified window handle.

The manager attaches to the 86Box instance by launching it with the ``-H``/``--hwnd vm_id,hwnd`` command line option, where ``vm_id`` is an arbitrary 64-bit identifier number and ``hwnd`` is the window handle to receive messages on, both **in hexadecimal** without the ``0x`` prefix.

All window messages sent by the emulator include the main window's handle in ``LPARAM``, including ``WM_SENDHWND`` which is sent on startup and can be used to match the window handle to the identifier provided in the command line.

.. flat-table::
  :header-rows: 1
  :widths: 139 65 73 418
  :class: longtable

  * - Name
    - Value
    - Sent by
    - Description

  * - ``WM_SHOWSETTINGS``
    - ``0x8889``
    - Manager
    - Open the emulated machine's :doc:`Settings window <../settings/index>`.

  * - ``WM_PAUSE``
    - ``0x8890``
    - Manager
    - Pause or unpause the emulated machine.

  * - ``WM_SENDHWND``
    - ``0x8891``
    - 86Box
    - Sent when the emulator window is first displayed. ``WPARAM`` contains the manager-provided machine ID.

  * - ``WM_HARDRESET``
    - ``0x8892``
    - Manager
    - Force a reset of the emulated machine.

  * - ``WM_SHUTDOWN``
    - ``0x8893``
    - Manager
    - Trigger a shutdown. ``WPARAM`` ``0`` sends a shutdown request, which displays a confirmation prompt if enabled, while ``1`` forces a shutdown.

  * - ``WM_CTRLALTDEL``
    - ``0x8894``
    - Manager
    - Send a *Ctrl+Alt+Delete* keyboard sequence to the emulated machine.

  * - ``WM_SENDSTATUS``
    - ``0x8895``
    - 86Box
    - Sent when the emulated machine is paused (``WPARAM`` ``0``) or unpaused (``1``).

  * - ``WM_SENDDLGSTATUS``
    - ``0x8896``
    - 86Box
    - Sent when the emulator is waiting for user input in a modal dialog box (``WPARAM`` ``0``) or when said dialog box has closed (``1``).

  * - ``WM_HAS_SHUTDOWN``
    - ``0x8897``
    - 86Box
    - Sent when the emulated machine shuts down.
