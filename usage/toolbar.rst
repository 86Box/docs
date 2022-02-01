.. include:: /include.rst

Toolbar
=======

The toolbar located at the top of the 86Box window (right below the :doc:`menu bar <menubar>`) has two purposes: it provides quick actions for the emulated machine on its left hand side, and displays status information on its right hand side.

|pause| |run| Pause/resume execution
------------------------------------

Pause emulation of the machine. Press again to resume emulation.

.. note:: Emulation is automatically paused when the emulated machine enters ACPI sleep mode.

|hard_reset| Hard reset
-----------------------

Force a reset of the emulated machine. Requires confirmation, which can be disabled by checking the *Don't show this message again* box.

|acpi_shutdown| ACPI shutdown
-----------------------------

Initiate a clean shutdown of the emulated machine. Only available on machines with ACPI soft power off capability.

|send_cad| |send_cae| Press Ctrl+Alt+Del/Ctrl+Alt+Esc
-------------------------------------------------------

Send a *Ctrl+Alt+Del* (left-most icon) or *Ctrl+Alt+Esc* (right-most icon) key combination to the emulated machine. You can alternatively press *Ctrl+F12* to send a *Ctrl+Alt+Del* combination.

|settings| Settings
-------------------

Open the :doc:`Settings <../settings/index>` window to configure the emulated machine.

Status area
-----------

The right hand side of the toolbar displays status information, such as:

* **Emulation speed** in percentage. If this number stays consistently below 100%, your host system is not keeping up with emulating the configured hardware.
* **Mouse state** (captured or released) if a :ref:`mouse <settings/input:Mouse>` is enabled.
* **Pause indicator** if emulation is paused.
