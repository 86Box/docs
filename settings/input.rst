.. include:: /include.rst

|input_devices| Input devices
=============================

The **Input devices** page contains settings related to the emulated machine's mouse, joysticks and other input devices.

Mouse
-----

Emulate a pointing device. The following types are supported:

* **Bus mouse:** ISA expansion card with a mouse interface. The I/O port and IRQ used by the card are configurable.
* **Serial mouse:** connected to the serial port of your choosing.
* **PS/2 mouse:** connected to the PS/2 port. Only available on machines with a PS/2 mouse port.
* **Wacom tablet:** connected to the serial port of your choosing. Currently cannot be used alongside a mouse.

The *Configure* button opens a new window with settings specific to the selected device type, such as the number of buttons, or the serial port for a serial mouse or tablet.

.. note:: Serial pointing devices require the configured serial port to be enabled on the :ref:`Ports tab <settings/ports:Serial port 1-4>`. 

Joystick
--------

Emulate one or more game port controller(s). The following controller types are supported:

* **None:** no controller connected.
* **2-axis, 2-button joystick(s):** up to two controllers, each with two buttons and an analog stick.
* **2-axis, 4-button joystick:** single controller with four buttons and an analog stick.
* **3-axis, 2-button joystick:** single controller with two buttons and an analog stick and a throttle.
* **3-axis, 4-button joystick:** single controller with four buttons and an analog stick and a throttle.
* **2-axis, 6-button joystick:** single controller with four regular buttons, two additional buttons mapped to the third and fourth axes, and an analog stick.
* **2-axis, 8-button joystick:** single controller with four regular buttons, four additional buttons mapped to the third and fourth axes, and an analog stick.
* **4-axis 4-button joystick:** single controller with four buttons and two analog sticks (or four axes).
* **CH Flightstick Pro:** flight controller with four buttons, three axes and a POV hat.
* **Microsoft SideWinder Pad:** up to four controllers, each with 10 buttons and a directional pad. Not compatible with standard game port joysticks; requires a driver in the emulated machine.
* **Thrustmaster Flight Control System:** flight controller with four buttons, two axes and a POV hat.

.. note:: A generic game port card is emulated if the machine has no game ports (either built-in or as part of a Plug and Play or PCI sound card) to accomodate the selected controller. This generic card uses the default I/O ports 200-207h, which can be changed through ISA Plug and Play. On IBM PCjr and PS/1 machines, the generic card uses port 201h only and has no Plug and Play capability.

Joystick 1-4...
---------------

Configure the mappings for each emulated game port controller. The *Device* box lists all game controllers connected to the host, while the other boxes allow you to map each axis or button of the emulated controller to the real controller.

If you're not sure as to what axis or button numbers map to which sticks and buttons on the real controller, use the *Test* feature of Windows' *Game Controllers* control panel (``joy.cpl``). Keep in mind 86Box's button numbers start with 0, whereas the control panel's numbers start with 1.

.. note:: XInput controllers are accessed through their DInput emulation mode at the moment.
