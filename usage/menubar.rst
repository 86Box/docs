Menu bar
========

The menu bar located at the top of the 86Box window provides controls for the emulated machine as a whole, its display, and the 86Box user interface.

Action
------

* **Right CTRL is left ALT:** let the right Ctrl key act as a left Alt key, to simulate some special keyboards where the Alt key is located on the right side of the space bar.
* **Hard reset:** force a reset of the emulated machine. Requires confirmation.
* **Ctrl+Alt+Del:** send a *Ctrl+Alt+Del* key combination to the emulated machine. You can alternatively press *Ctrl+F12* to send that combination.
* **Ctrl+Alt+Esc:** send a *Ctrl+Alt+Esc* key combination to the emulated machine.
* **Pause:** pause emulation. Uncheck this option to resume emulation.
* **Exit:** quit 86Box. Requires confirmation.

View
----

* **Resizeable window:** allow the 86Box window to be freely resized. Unchecking this option will return the window to its normal size.
* **Remember size & position:** automatically save the size and position of the 86Box window to the emulated machine's configuration file.
* **Renderer:** select a graphical renderer for the emulated display. *SDL (Hardware)* is recommended, but it may not work on some host systems, where *SDL (Software)* is the best option.
* **Force 4:3 display ratio:** stretch the emulated display to a 4:3 aspect ratio, independently of the emulated machine's screen resolution.
* **Window scale factor:** scale the emulated display to half (0.5x), normal (1x), 50% larger (1.5x) or double (2x) sizes.
* **Enable HiDPI scaling:** automatically scale the emulated display to real size if your host system has a HiDPI screen. This option can be used alongside *Window scale factor* above.
* **Fullscreen:** enter full screen mode. Press *Ctrl+Alt+Page Down* to go back to windowed mode. You can also enter full screen mode by pressing *Ctrl+Alt+Page Up*.
* **Fullscreen stretch mode:** select the picture mode to use when in full screen mode.

   * **Full screen stretch:** stretch the emulated display to completely fill the host display.
   * **4:3:** stretch the emulated display to a 4:3 aspect ratio, then scale it to fit the host display.
   * **Square pixels (keep ratio):** scale the emulated display to fit the host display, without changing the aspect ratio.
   * **Integer scale:** scale the emulated display to the largest integer scale amount to fit the host display. This provides the highest possible picture quality, at the cost of black bars if the host display's resolution is not divisible by the emulated display's resolution.

* **EGA/(S)VGA settings:** contains display settings specific to EGA, VGA and Super VGA video hardware.

   * **Inverted VGA monitor:** emulate a VGA monitor with inverted colors.
   * **VGA screen type:** select the VGA monitor type to emulate. Color, grayscale, amber phosphor, green phosphor and white phosphor monitors can be selected.
   * **Grayscale conversion type:** select the color-to-grayscale conversion profile to use when a grayscale monitor is selected.

* **CGA/PCjr/Tandy/EGA/(S)VGA overscan:** add an overscan border around the display. This border is only added when emulating the specified video hardware types.
* **Change contrast for monochrome display:** optimize the contrast of monochrome CGA monitors for 4-color operation.

Media
-----

This menu lists all removable media drives attached to the emulated machine, and provides the same controls that are accessible by clicking the respective drive's icon on the :doc:`status bar <statusbar>`.

Tools
-----

* **Settings:** open the :doc:`Settings <../settings/index>` window.
* **Update status bar icons:** enable the activity lights on :doc:`status bar <statusbar>` icons. Unchecking this option may improve emulation performance on low-end host systems.
* **Enable Discord integration:** enable Discord Rich Presence. Other Discord users will know that you're running 86Box, as well as the emulated machine's name, model and CPU.

.. note:: Discord integration will not be available if the Discord desktop app is not running, or if the included ``discord_game_sdk.dll`` file is missing from the 86Box directory.

* **Take screenshot:** take a screenshot of the emulated display. Screenshots are saved as PNG images in the ``screenshots`` directory.

Help
----

* **Documentation:** open the very documentation you're reading.
* **About 86Box:** show credits and license information about 86Box.
