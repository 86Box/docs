.. include:: /include.rst

|machine| Machine
=================

The **Machine** page contains settings related to the emulated machine as a whole, such as the machine type, CPU type and amount of memory.

Machine type / Machine
----------------------

Machine/motherboard model to emulate. The *Machine* box lists all available models for the machine class selected on the *Machine type* box.

The *Configure* button opens a new window with settings specific to the machine, such as BIOS type selection.

.. note:: **86Box 4.0.1:** Settings for the machine's onboard devices have been moved to the *Configure* buttons at the devices' respective locations; for instance, configuring the amount of installed video memory for an onboard video chip is now done through the *Configure* button next to the :ref:`Display page's Video box <settings/display:Video>` when the *Internal* option is selected there.

CPU type / Speed
----------------

Main processor to emulate. The *Speed* box lists all available speed grades for the processor family selected on the *CPU type* box. These boxes only list processor types and speed grades supported by the machine selected above.

FPU
---

Math co-processor to emulate. This box is not available if the processor selected above has an integrated co-processor or lacks support for an external one.

Wait states
-----------

Number of memory wait states to use on a 286- or 386-class processor. This box is not available if any other processor family is selected above.

PIT mode
--------

Programmable Interval Timer emulation mode. **Auto** should cover most use cases, automatically selecting **Fast** mode on 486-class and newer processors or **Slow** mode on older ones. A limited set of timing-sensitive applications require **Slow** mode, which is slower but more accurate.

Memory
------

Amount of RAM to give the emulated machine. The minimum and maximum allowed amounts of RAM will vary depending on the machine selected above.

Dynamic Recompiler
------------------

Enable the dynamic recompiler, which provides faster but less accurate CPU emulation. The recompiler is available as an option for 486-class processors, and is mandatory starting with the Pentium.

Softfloat FPU
-------------

Enable a slower but more accurate math co-processor emulation, for running a limited set of operating systems and applications which demand full 80-bit precision from the floating point unit.

Time synchronization
--------------------

Automatically copy your host system's date and time over to the emulated machine's hardware real-time clock. Synchronization is performed every time the emulated operating system reads the hardware clock to calibrate its own internal clock, which usually happens once on every boot.

* **Disabled:** do not perform time synchronization. The emulated machine's date and time can be set through its operating system or BIOS setup utility. Time only ticks while the emulated machine is running.
* **Enabled (local time):** synchronize the time in your host system's configured timezone. Use this option when emulating an operating system which stores *local time* in the hardware clock, such as DOS or Windows.
* **Enabled (UTC):** synchronize the time in Coordinated Universal Time (UTC). Use this option when emulating an operating system which stores *UTC time* in the hardware clock, such as Linux.
