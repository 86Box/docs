Keyboard
========

This page outlines keyboard behavior specific to different host operating systems, real keyboards and emulated machines.

Host systems
------------

Windows
^^^^^^^

* Not all multimedia function keys can be passed through to the emulated machine due to a Windows limitation.
* System-wide key remapping through the **Scancode Map** registry key (as performed by applications such as SharpKeys) is fully supported.

macOS
^^^^^

* Apple keyboards with **European or other ISO layouts** may have *the key below Esc* and *the key to the right of Left Shift* switch places in the emulated machine, due to a hardware quirk in many of those keyboards (both internal and external) and a limitation in the way macOS corrects it.
* The **Num =** key is only usable in operating systems which recognize that key on Microsoft PS/2 multimedia keyboards.
* Mac special keys are mapped to their PC equivalents where possible:

.. list-table::
  :header-rows: 1
  :widths: 1 999

  * - Emulated key
    - Host key

  * - Windows
    - Command

  * - Alt
    - Option

  * - Print Screen
    - F13

  * - Scroll Lock
    - F14

  * - Pause
    - F15

  * - Insert
    - Command + Fn + Delete (MacBook and tenkeyless keyboards)

      Command + Forward Delete (full size keyboards)

  * - Num Lock
    - Clear

Linux
^^^^^

* The `xkbcommon <https://xkbcommon.org>`_ library is used to accurately map physical keys to the emulated keyboard on both X11 and Wayland. When compiling 86Box from source, make sure the development files for ``libxkbcommon`` and ``libxkbcommon-x11`` are installed, as this is an optional build component.


Special keys
------------

Some machines provide additional function or otherwise special keys on top of the standard PC layout. Those keys are mapped to ones present on modern keyboards within reason.

Olivetti
^^^^^^^^

The Olivetti M series special keys are mapped as such:

.. list-table::
  :header-rows: 1
  :widths: 1 999

  * - Emulated key
    - Host key

  * - CLEAR
    - Page Up

  * - BREAK
    - Page Down

  * - SCR PRT
    - Print Screen

  * - HELP
    - Menu

  * - 00
    - Left Windows

  * - F13
    - Insert

  * - F14
    - Home

  * - F15
    - Del

  * - F16
    - End

  * - F17
    - Right Alt

  * - F18
    - Right Win


Toshiba
^^^^^^^

The Toshiba T1000 series function keys can be accessed by holding Right Alt or Right Ctrl:

.. list-table::
   :header-rows: 1

   * - Function
     - Right Alt/Ctrl +

   * - Show/hide numeric keypad overlay
     - Num Lock

   * - Change internal display font
     - Right

   * - Use internal display
     - Home

   * - Use external display
     - End

   * - Turbo mode on (T1200)
     - Page Up

   * - Turbo mode off (T1200)
     - Page Down

   * - Show/hide pop-up window (T1200)
     - Print Screen
