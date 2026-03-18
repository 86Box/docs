.. include:: /include.rst

Toolbar
=======

The toolbar located at the top of the 86Box window (right below the :doc:`menu bar <menubar>`) has two purposes: it provides quick actions for the emulated machine on its left hand side, and displays status information on its right hand side.


|pause| |run| Pause/resume execution
------------------------------------

Pause emulation of the machine. Press again to resume emulation. You can alternatively press :kbd:`Ctrl`\ +\ :kbd:`Alt`\ +\ :kbd:`F1` (:doc:`customizable <../settings/bindings>`) to pause or resume emulation.

.. note:: Emulation is automatically paused when the emulated machine enters **ACPI sleep mode**.

|fast_forward| Fast forward
---------------------------

Run the emulated machine at the highest speed your host system can handle. Press again to return to normal speed. You can alternatively press :kbd:`Ctrl`\ +\ :kbd:`Alt`\ +\ :kbd:`F` (:doc:`customizable <../settings/bindings>`) to control this option.

.. note:: When fast forwarding, all emulated audio is automatically **muted** to prevent distortion.

|hard_reset| Hard reset
-----------------------

Force a reset of the emulated machine. Requires confirmation, which can be disabled by checking the *Don't show this message again* box. You can alternatively press :kbd:`Ctrl`\ +\ :kbd:`Alt`\ +\ :kbd:`F12` (:doc:`customizable <../settings/bindings>`) to hard reset.

|acpi_shutdown| ACPI shutdown
-----------------------------

Send a power button press to the emulated machine. Only available on machines with ACPI soft power off support.

|send_cad| |send_cae| Press Ctrl+Alt+Del/Ctrl+Alt+Esc
-----------------------------------------------------

Send a *Ctrl+Alt+Del* (left-most icon) or *Ctrl+Alt+Esc* (right-most icon) key combination to the emulated machine. You can alternatively press :kbd:`Ctrl`\ +\ :kbd:`F12` to send a *Ctrl+Alt+Del* combination, or :kbd:`Ctrl`\ +\ :kbd:`F10` to send *Ctrl+Alt+Esc*; both key combinations are :doc:`customizable <../settings/bindings>`.

|settings| Settings
-------------------

Open the :doc:`Settings <../settings/index>` window to configure the emulated machine.

|take_screenshot| |copy_screenshot| Take/copy screenshot
--------------------------------------------------------

Take a screenshot of the emulated display. The left-most icon saves the screenshot as a .png image in the ``screenshots`` subdirectory found in the emulated machine's directory, which can be opened with the **Open screenshots folder** option in the :ref:`Tools menu <usage/menubar:Tools>`, while the right-most icon copies the image to the host system's clipboard instead. You can alternatively press :kbd:`Ctrl`\ +\ :kbd:`F11` to take a screenshot to file; the key combinations for all screenshot commands are :doc:`customizable <../settings/bindings>`.

Status area
-----------

The right hand side of the toolbar displays status information, such as:

* **Emulation speed** in percentage. If this number stays consistently below 100%, your host system is not keeping up with emulating the configured hardware.
* **Mouse state** (captured or released) if a :ref:`mouse <settings/input:Mouse>` is enabled.
* **Pause indicator** if emulation is paused.
