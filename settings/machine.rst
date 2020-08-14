Machine
=======

The *Machine* page contains settings related to the emulated machine as a whole, such as the machine type, CPU type and amount of memory.

Machine type / Machine
----------------------

Machine/motherboard to emulate. The *Machine type* box lists all available machine classes, while the *Machine* box lists all available machines on the selected class.

The *Configure* button opens a new window with settings specific to the machine's onboard devices, such as the amount of installed video memory for an onboard video chip.

CPU type / CPU
--------------

Main processor to emulate. Only processors supported by the selected machine will be listed.

FPU
---

Math co-processor to emulate. This box will not be enabled if a processor with an integrated math co-processor is selected.

Wait states
-----------

Number of memory wait states to use on a 286- or 386-class processor. This box will not be enabled if any other processor family is selected.

Memory
------

Amount of RAM to give the emulated machine. The minimum and maximum allowed amounts of RAM will vary depending on the selected machine.

Dynamic Recompiler
------------------

Enable the dynamic recompiler, which provides faster but less accurate CPU emulation. The recompiler is available as an option for 486-class processors, and is mandatory starting with the Pentium.

Time synchronization
--------------------

Time synchronization automatically copies your host system's date and time settings over to the emulated machine's hardware real-time clock. Synchronization is performed every time the guest operating system reads the hardware clock to calibrate its own internal clock, which usually happens once on every boot.

* **Disabled:** do not perform time synchronization.
* **Enabled (local time):** synchronize the time in your host system's configured timezone. Use this option when emulating an operating system which stores *local time* in the hardware clock, such as DOS or Windows.
* **Enabled (UTC):** synchronize the time in Coordinated Universal Time (UTC). Use this option when emulating an operating system which stores *UTC time* in the hardware clock, such as Linux.
