Input devices
=============

The *Input devices* page contains settings related to the emulated machine's mouse, joysticks and other input devices.

Mouse
-----

Mouse device to emulate. Bus, serial and PS/2 (on supported machines) mice are supported.

The *Configure* button opens a new window with settings specific to the selected mouse type, such as the number of buttons, the serial port for serial mice, or the I/O port and IRQ for bus mice.

Joystick
--------

Game port controller to emulate. The following choices are available:

* **Standard 2-button joystick(s):** up to two controllers, each with two buttons and a single analog stick.
* **Standard 4-button joystick:** single controller with four buttons and a single analog stick.
* **Standard 6-button joystick:** single controller with four regular buttons, two additional buttons mapped to the third and fourth axes, and a single analog stick.
* **Standard 8-button joystick:** single controller with four regular buttons, four additional buttons mapped to the third and fourth axes, and a single analog stick.
* **4-axis 4-button joystick:** single controller with four buttons and four axes (or two analog sticks).
* **CH Flightstick Pro:** flight controller with four buttons, three axes and a POV hat.
* **Microsoft SideWinder Pad:** up to four controllers, each with 10 buttons and a directional pad. Requires a driver to be installed on the guest operating system.
* **Thrustmaster Flight Control System:** flight controller with four buttons, two axes and a POV hat.
* **No joystick:** no controller connected.

Joystick 1-4...
---------------

Configure the mappings for each emulated game port controller. The *Device* box lists all game controllers connected to the host, while the other boxes allow you to map each axis or button of the emulated controller to the real controller.

If you're not sure as to what axis or button numbers map to which sticks and buttons on the real controller, use the *Test* feature of Windows' *Game Controllers* control panel (``joy.cpl``). Keep in mind 86Box's button numbers start with 0, whereas the control panel's numbers start with 1.

.. note:: Only DInput controllers are supported at the moment. XInput controllers are still supported through their DInput emulation mode, with no action required.
