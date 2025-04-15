Menu bar
========

The menu bar located at the top of the 86Box window provides controls for the emulated machine as a whole, its display, and the 86Box user interface.

.. important:: On macOS, the **Exit** (Quit), **Preferences** and **About 86Box** options are found in the **86Box** application menu instead of the locations outlined here.

Action
------

* **Auto-pause on focus loss:** automatically pause emulation while the 86Box window is not focused.
* **Keyboard requires capture:** require the mouse to be captured for keypresses to be forwarded to the emulated machine. Enabling this option allows the use of keyboard combinations (such as Alt+Tab) on the host system while the 86Box window is focused.
* **Right CTRL is left ALT:** let the right Ctrl key act as a left Alt key, to simulate some special keyboards where the Alt key is located on the right side of the space bar.
* **Pause:** pause emulation of the machine. Uncheck this option to resume emulation.
* **Hard Reset:** force a reset of the emulated machine. Requires confirmation, which can be disabled by checking the *Don't show this message again* box.
* **Ctrl+Alt+Del:** send a *Ctrl+Alt+Del* key combination to the emulated machine. You can alternatively press *Ctrl+F12* to send that combination.
* **Ctrl+Alt+Esc:** send a *Ctrl+Alt+Esc* key combination to the emulated machine.
* **Exit:** quit 86Box. Requires confirmation, which can be disabled by checking the *Don't show this message again* box.

View
----

* **Hide toolbar:** hides the :doc:`toolbar <toolbar>` below the menu bar.
* **Hide status bar:** hides the :doc:`status bar <statusbar>` at the bottom of the window.
* **Show non-primary monitors:** shows or hides the secondary display window if a :ref:`secondary video card <settings/display:Video #2>` is configured.
* **Resizeable window:** allow the 86Box window to be freely resized. Unchecking this option will also return the window to its normal size.
* **Remember size & position:** automatically save the size and position of the 86Box window to the emulated machine's configuration file.
* **Renderer:** select a graphical renderer for the emulated display.

   * **Qt (Software)** is recommended in most cases.
   * **Qt (OpenGL)** and **Vulkan** are known to perform better on some host systems. Try these if your system is struggling to maintain 100% emulation speed. *Vulkan* may not be available if the host GPU is not Vulkan-capable.
   * **OpenGL (3.0 Core)** allows for shader effects to be applied to the emulated display, however, it is not compatible with older integrated GPUs.

* **Renderer options:** open a window to configure the *OpenGL (3.0 Core)* renderer. This option will be available if that renderer is selected.

   * **Synchronize with video:** update the emulated display at its current refresh rate.
   * **Use target framerate:** update the emulated display at the selected refresh rate.
   * **VSync:** enable vertical sync. Recommended if tearing artifacts are observed.
   * **Add:** add a ``.glsl`` or ``.glslp`` file to the list of shaders to apply on the emulated display.
   * **Remove:** remove the selected shader from the list.
   * **Configure:** open a window to configure parameters on the selected shader.
   * **Move up/down:** move the selected shader up or down in the processing order.

.. note::
  * Many shaders are available for simulating CRT displays, VHS tapes and other aesthetics; the `RetroArch glsl-shaders repository <https://github.com/libretro/glsl-shaders>`_ is a good place to start.
  * ``.cg`` and ``.cgp`` shaders are not supported, as these formats are long deprecated.

* **Specify dimensions:** open a window where an exact size (in pixels) for the emulated display can be set. If checked, the *Lock to this size* box prevents changes in the emulated display's resolution from overriding the specified size.
* **Force 4:3 display ratio:** stretch the emulated display to a 4:3 aspect ratio, independently of the emulated machine's screen resolution.
* **Window scale factor:** scale the emulated display to half (*0.5x*), normal (*1x*), 50% larger (*1.5x*), double (*2x*) or larger (up to *8x*) sizes.
* **Filter method:** select the filtering method (*Nearest* or *Linear*) to be used when scaling the emulated display.
* **HiDPI scaling:** automatically scale the emulated display to real size if your host system has a HiDPI display. This option can be used alongside *Window scale factor* above.

.. note:: If HiDPI scaling is disabled on a host with a HiDPI display, the emulated display's size may be off by one pixel due to an integer scaling limitation.

* **Fullscreen:** enter full screen mode. Press *Ctrl+Alt+Page Down* to go back to windowed mode. You can also enter full screen mode by pressing *Ctrl+Alt+Page Up*.
* **Fullscreen stretch mode:** select the picture mode to use when in full screen mode.

   * **Full screen stretch:** stretch the emulated display to completely fill the host display.
   * **4:3:** stretch the emulated display to a 4:3 aspect ratio, then scale it to fit the host display.
   * **Square pixels (keep ratio):** scale the emulated display to fit the host display, without changing the aspect ratio.
   * **Integer scale:** scale the emulated display to the largest integer scale factor to fit the host display. This provides the highest possible picture quality, at the cost of black bars if the host display's resolution is not divisible by the emulated display's resolution.
   * **4:3 integer scale:** stretch the emulated display to a 4:3 aspect ratio, then scale it to the largest integer scale factor to fit the host display.

* **Apply fullscreen stretch mode when maximized:** apply the picture mode selected above in windowed mode if *Resizeable window* is enabled and the window is maximized. 
* **EGA/(S)VGA settings:** contains display settings specific to EGA, VGA and Super VGA video hardware.

   * **Inverted VGA monitor:** emulate a VGA monitor with inverted colors.
   * **VGA screen type:** select the VGA monitor type to emulate. *Color*, *Grayscale*, *Amber*, *Green* and *White* phosphor monitors can be selected.
   * **Grayscale conversion type:** select the color-to-grayscale conversion profile (*BT.601*, *BT.709* or *Average*) to use when a grayscale monitor is selected.

* **CGA/PCjr/Tandy/EGA/(S)VGA overscan:** add an overscan border around the display. This border is only added when emulating the specified video hardware types.
* **Change contrast for monochrome display:** optimize the contrast of monochrome CGA monitors for 4-color operation.

Media
-----

This menu lists all storage drives and network cards attached to the emulated machine, and provides the same options that are accessible by clicking the respective device's icon on the :doc:`status bar <statusbar>`.

The **Clear image history** option empties the list of recently-loaded images on all storage drives.

Tools
-----

* **Settings:** open the :doc:`Settings <../settings/index>` window to configure the emulated machine.
* **Update status bar icons:** enable the activity lights on :doc:`status bar <statusbar>` icons. Unchecking this option may improve emulation performance on low-end host systems.
* **Enable Discord integration:** enable Discord Rich Presence. 86Box shares the emulated machine's name, model and CPU with other Discord users.

.. note:: Integration requires the Discord desktop app, running on x86 or x64 Windows, ``x86_64`` Linux or Intel macOS. Discord does not provide integration support for other operating systems / architectures or the browser app. Additionally, integration will not be available on Windows if the included ``discord_game_sdk.dll`` file is missing from the 86Box directory.

* **Take screenshot:** take a screenshot of the emulated display. Screenshots are saved as .png images in the ``screenshots`` subdirectory found in the emulated machine's directory, which can be opened with the **Open screenshots folder** option below.
* **Sound:** provides the same options that are accessible by clicking the :ref:`sound icon on the status bar <usage/statusbar:|sound| Sound>`.
* **Preferences:** open the *Preferences* window, which provides the following options:

   * **Language:** select a language for the 86Box user interface.
   * **Mouse sensitivity:** adjust the emulated mouse's tracking sensitivity.
   * **Select media images from program working directory:** if checked, starts any file open/save prompts on the emulated machine's directory. This option is particularly useful for macOS users.
   * **Inhibit multimedia keys on Windows:** if checked, multimedia keys such as **Volume Up/Down** will not be passed through to the emulated machine. This option is only available on Windows.
   * **Ask for confirmation before saving settings / quitting / hard resetting:** enable confirmation messages for certain actions. These options can reenable confirmations after they have been disabled through the *Don't show this message again* box.
   * **Display hotkey message when entering full-screen mode:** enable the *Ctrl+Alt+Page Down* reminder message upon entering full screen mode.

* **MCA devices**: open the *MCA devices* window, which lists the IDs and required `Adapter Definition Files <https://ardent-tool.com/adapters/ADF.html>`_ of all Micro Channel devices installed on the emulated machine. This option will only be available when emulating a Micro Channel Architecture-based machine.
* **Open screenshots folder**: open the host system's file browser on the directory where screenshots of this emulated machine are saved.

Help
----

* **Documentation:** open the very documentation you're reading.
* **About 86Box:** show credits, license and build information about 86Box.
