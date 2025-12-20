.. include:: /include.rst

Toolbar
=======

The toolbar located at the top of the 86Box window (right below the :doc:`menu bar <menubar>`) has two purposes: it provides quick actions for the emulated machine on its left hand side, and displays status information on its right hand side.

|interpreter| |recompiler| Force interpretation / Allow recompilation
---------------------------------------------------------------------

Temporarily disable the :ref:`dynamic recompiler <settings/machine:Dynamic Recompiler>`. Press again to reenable the recompiler. You can alternatively press :kbd:`Ctrl`\ +\ :kbd:`Alt`\ +\ :kbd:`I` (:ref:`customizable <settings/input:Key bindings>`) to control this option.


|pause| |run| Pause/resume execution
------------------------------------

Pause emulation of the machine. Press again to resume emulation. You can alternatively press :kbd:`Ctrl`\ +\ :kbd:`Alt`\ +\ :kbd:`F1` (:ref:`customizable <settings/input:Key bindings>`) to pause or resume emulation.

.. note:: Emulation is automatically paused when the emulated machine enters ACPI sleep mode.

|hard_reset| Hard reset
-----------------------

Force a reset of the emulated machine. Requires confirmation, which can be disabled by checking the *Don't show this message again* box. You can alternatively press :kbd:`Ctrl`\ +\ :kbd:`Alt`\ +\ :kbd:`F12` (:ref:`customizable <settings/input:Key bindings>`) to hard reset.

|acpi_shutdown| ACPI shutdown
-----------------------------

Send a power button press to the emulated machine. Only available on machines with ACPI soft power off support.

|send_cad| |send_cae| Press Ctrl+Alt+Del/Ctrl+Alt+Esc
-----------------------------------------------------

Send a *Ctrl+Alt+Del* (left-most icon) or *Ctrl+Alt+Esc* (right-most icon) key combination to the emulated machine. You can alternatively press :kbd:`Ctrl`\ +\ :kbd:`F12` to send a *Ctrl+Alt+Del* combination, or :kbd:`Ctrl`\ +\ :kbd:`F10` to send *Ctrl+Alt+Esc*; both key combinations are :ref:`customizable <settings/input:Key bindings>`.

|settings| Settings
-------------------

Open the :doc:`Settings <../settings/index>` window to configure the emulated machine.

Status area
-----------

The right hand side of the toolbar displays status information, such as:

* **Emulation speed** in percentage. If this number stays consistently below 100%, your host system is not keeping up with emulating the configured hardware.
* **Mouse state** (captured or released) if a :ref:`mouse <settings/input:Mouse>` is enabled.
* **Pause indicator** if emulation is paused.
