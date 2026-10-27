|machine| Machine
=================

The **Machine** page contains settings related to the emulated machine as a whole, such as the machine type, CPU type and amount of memory.

|machine_tab| Machine
---------------------

Machine type / Machine
^^^^^^^^^^^^^^^^^^^^^^

Machine/motherboard model to emulate. The *Machine* box lists all available models for the machine class selected on the *Machine type* box. Click |clear| to search for a machine by name or chipset across all classes.

The *Configure* button opens a new window with settings specific to the machine, such as BIOS type selection.

.. note:: Settings for the machine's on-board devices have been moved to the *Configure* buttons at the devices' respective locations; for instance, configuring the amount of installed video memory for an on-board video chip is now done through the *Configure* button next to the :ref:`Display page's Video box <settings/display:Video>` when the *Internal device* option is selected there.

Memory
^^^^^^

Amount of RAM to give the emulated machine. The minimum and maximum allowed amounts of RAM will vary depending on the machine selected above.

Synchronize with host clock
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Automatically copy your host system's date and time over to the emulated machine's hardware real-time clock. Synchronization is performed every time the emulated operating system reads the hardware clock to calibrate its own internal clock, which usually happens on each boot.

**Time zone:** controls which time is used for the emulated system:

* **Local:** synchronizes the time in your host system's configured time zone. Use this when emulating an operating system which stores *local time* in the hardware clock, such as DOS or Windows.
* **UTC:** synchronizes the time in Coordinated Universal Time (UTC). Use this option when emulating an operating system which stores *UTC time* in the hardware clock, such as Linux or *BSD.

**Date:** controls the synchronization of the year, month, and day, while the hour, minute, and second remain synchronized to the host using the set time zone rule:

* **Match the host:** completely synchronizes the current date set on your host, which allows guest operating systems to follow the real date and reflect it in timestamps. This may especially be crucial when interacting with Internet services through the guest, as a roughly correct clock is expected in many network protocols.
* **Offset the year by:** allows altering the date by offsetting the year by a specified integer number of years; negative values represent years in the past and positive values represent years in the future. If you set a value of -40 while the current year is 2027, the guest will boot up believing the year to be 1987; in the year 2028, the guest will boot up in the year 1988. This option may help to avoid year 2000 or year 2038 issues with some software.
* **Always use the year:** sets a static year that the guest will always boot up in, while preserving the current month and day. If you set this value, for instance, to 1986, the guest will always boot up believing it to be 1986. This may cause timestamps to wrap around at the start of a new year, making newer files appear older than earlier ones. This option may help to avoid year 2000 or year 2038 issues with some software.
* **Do not synchronize the date:** causes 86Box to only synchronize the hour, minute, and second components of the real-time clock. Any date set by the BIOS and/or operating system in the guest will stick. This may be especially useful in running "timebombed" interim builds of operating systems that have a narrow window of time during which they are permitted to be installed and used.

|processor| Processor
---------------------

CPU type / Frequency
^^^^^^^^^^^^^^^^^^^^

Main processor to emulate. The *Speed* box lists all available speed grades for the processor family selected on the *CPU type* box. These boxes only list processor types and speed grades supported by the machine selected above.

FPU
^^^

Math co-processor to emulate. This box is not available if the processor selected above has an integrated co-processor or lacks support for an external one.

Wait states
^^^^^^^^^^^

Number of memory wait states to use on a 286- or 386-class processor. This box is not available if any other processor family is selected above.

Softfloat FPU
^^^^^^^^^^^^^

Enable a slower but more accurate math co-processor emulation, for running a limited set of operating systems and applications which demand full 80-bit precision from the floating point unit.

|performance| Performance
-------------------------

PIT mode
^^^^^^^^

Programmable Interval Timer emulation mode. **Auto** should cover most use cases, automatically selecting **Fast** mode on 486-class and newer processors or **Slow** mode on older ones. A limited set of timing-sensitive applications require **Slow** mode, which is slower but more accurate.

Use the 486 interpreter for 286 and 386 processors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enable a faster but less accurate CPU emulation engine on 286- or 386-class processors. Recommended for low-end host systems which are struggling to emulate faster 386s. This option is not available if any other processor family is selected above.

Dynamic recompiler
^^^^^^^^^^^^^^^^^^

Enable the dynamic recompiler, which provides faster but less accurate CPU emulation. The recompiler is available as an option for 486-class processors, and is mandatory starting with the Pentium.

.. note:: The recompiler can be disabled temporarily (even on processors where it is mandatory) through an option on the :ref:`Action menu <usage/menubar:Action>`, in the unlikely event that an application performs worse with the recompiler enabled. Selecting this temporary option again or restarting 86Box will reenable the recompiler.

Accurate FPU environment on the dynamic recompiler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enable to remove some performance shortcuts in the math co-processor emulation while using the dynamic recompiler, for running a limited set of applications which demand access to floating point unit instruction state. Can be combined with :ref:`Softfloat <settings/machine:Softfloat FPU>` for maximum FPU accuracy at a high performance cost.

Block linking on the dynamic recompiler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enable a dynamic recompiler optimization which is known to improve emulation speed in most cases, but reduce it in a limited set of applications.

Debug registers on 486 and later processors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enable the hardware breakpoint/watchpoint functionality on 486-class or newer processors, for running software debuggers and copy-protected games which require it, at the cost of slower emulation. This functionality is always enabled on 386-class processors.

CPU frame size
^^^^^^^^^^^^^^

Change the emulator's frame timing behavior. This mostly affects the smoothness of the emulated mouse and other input peripherals.

* **Larger frames (less smooth):** same behavior as 86Box 4.2.1 and older. Switching to it may improve performance on low-end host systems, at the expense of reduced input smoothness.
* **Smaller frames (smoother):** the new default behavior introduced in 86Box 5.0, which improves input smoothness.
