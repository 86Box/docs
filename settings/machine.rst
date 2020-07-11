Machine
=======

Machine type / Machine
----------------------

Machine/motherboard to emulate. The *Machine type* box lists all available processor classes, while the *Machine* box lists all available machines of the selected processor class.

CPU type / CPU
--------------

Main processor to emulate. Only processors supported by the selected machine will be listed.

FPU
---

Math co-processor to emulate. This box will not be enabled if a processor with an integrated math co-processor is selected.

Wait states
-----------

Number of memory wait states. This box is only enabled and relevant if a 286- or 386-class CPU is selected.

Memory
------

Amount of RAM to give the emulated machine. The minimum and maximum amounts of RAM will vary depending on the selected machine.

Dynamic Recompiler
------------------

Enable the dynamic recompiler, which provides faster but less accurate CPU emulation. The recompiler is available as an option for 486-class processors, and is mandatory starting with the Pentium.

Time synchronization
--------------------

Time synchronization automatically copies your host machine's date and time settings over to the guest machine's hardware real-time clock. Synchronization is performed every time the guest operating system reads the hardware clock, which often happens once on every boot.

* **Disabled:** do not perform time synchronization.
* **Enabled (local time):** synchronize the time in your host machine's configured timezone. Use this option when running a guest operating system which stores local time in the hardware clock, such as DOS or Windows.
* **Enabled (UTC):** synchronize the time in Coordinated Universal Time (UTC). Use this option when running a guest operating system which stores UTC time in the hardware clock, such as Linux.
