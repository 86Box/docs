.. include:: /include.rst

|input_devices| Input devices
=============================

The **Input devices** page contains settings related to the emulated machine's mouse, joysticks and other input devices.

Keyboard
--------

Select the keyboard type to emulate. This box only lists keyboards supported by the machine.

The *Configure* button opens a new window with settings specific to the selected keyboard type, such as the number of keys.

Mouse
-----

Emulate a pointing device. The following types are supported:

* **Bus mouse:** ISA expansion card with a mouse interface. The I/O port and IRQ used by the card are configurable.
* **Serial mouse:** connected to the serial port of your choosing.
* **Serial tablet:** also connected to a serial port, but providing absolute (seamless) input on supported operating systems and/or applications.
* **PS/2 mouse:** connected to the PS/2 port. Only available on machines with a PS/2 mouse port.

The *Configure* button opens a new window with settings specific to the selected device type, such as the number of buttons, or the serial port for a serial mouse or tablet.

.. note:: 
  * **Serial pointing devices** require the configured serial port to be enabled on the :ref:`Ports page <settings/ports:Serial port 1-4>`.
  * The **middle mouse button** cannot be used to release mouse capture when emulating a pointing device with 3 or more buttons.

Joystick
--------

Emulate one or more game port controller(s). The following types are supported:

* Generic **joysticks**, **gamepads**, **flight yokes** and a **steering wheel**, all with a variable number of buttons and analog axes (two axes make one analog stick).
* **CH Flightstick Pro:** flight controller with four buttons, three or four axes and a POV hat.
* **Microsoft SideWinder Pad:** up to four gamepads, each with 10 buttons and a directional pad. Not compatible with standard game port joysticks; requires a driver in the emulated operating system.
* **Thrustmaster Flight Control System:** flight controller with four buttons, two or three axes and a POV hat.

.. note:: A **generic game port card** is emulated if the machine has no game ports (either built-in or as part of a sound card) to accomodate the selected controller. This generic card uses the default I/O ports 200-207h, configurable through ISA Plug and Play, except on IBM PCjr and PS/1 machines where it uses port 201h only with no Plug and Play capability.

Joystick 1-4...
---------------

Configure the mappings for each emulated game port controller. The *Device* box lists all game controllers connected to the host, while the other boxes allow you to map each axis or button of the emulated controller to the real controller.

If you're not sure as to what axis or button numbers map to which sticks and buttons on the real controller, use the *Test* feature of Windows' *Game Controllers* control panel (``joy.cpl``) or another controller testing utility for your platform.

.. note:: **XInput controllers** are accessed through their DInput emulation mode at the moment.

Key bindings
------------

View and change keyboard shortcuts for common emulator actions. The *Clear binding* button removes the shortcut associated with the selected action, and the *Bind* button allows for entering a new shortcut.

.. note:: The **F8 + F12 key combination** used for releasing mouse capture in previous 86Box versions can no longer be configured as a shortcut.
