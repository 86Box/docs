Frequently asked questions
==========================

What is the difference between 86Box and applications like VirtualBox or Virtual PC?
------------------------------------------------------------------------------------

VirtualBox, Virtual PC and similar applications are *hypervisors*. For the most part, they execute code running in the virtual machine as is, and only step in whenever it is required to enforce the separation of a virtual machine from the rest of the system. This also means that the virtual machine sees the same CPU as the host system.

They also mostly implement peripherals that are custom designed to let the guest take full potential of the virtualizer as long as appropriate drivers, which are distributed with the provided additions, are installed. This is great for modern operating systems and software that does is not designed for a specific hardware target, but rather an abstraction interface such as DirectX; however, running older applications and games will often lead to a suboptimal experience, as hypervisors don't tend to be designed with this usecase in mind.

On the other hand, 86Box is a *system emulator*. It implements a whole system in software, which includes the CPU, chipset and additional cards, if any. Furthermore, it interprets every single instruction running in the virtual machine, and while that comes with the obvious tradeoff of emulation being more CPU intensive than virtualization, it also makes it possible to simulate authentic behavior of the original hardware, including its speed. This in turn allows running countless games and demos that wouldn't have ran in a hypervisor before, as they simply run too fast or fail to make use of various hardware quirks that don't exist in modern processors.

In addition, the large variety of peripherals emulated by 86Box also makes it possible to use existing software, games and drivers that had been specifically designed for such peripherals. However, this obviously means that the emulator is also stuck with the limitations of the original hardware, and therefore it is not possible to offer advanced features such as mouse pointer integration.

What is the difference between 86Box and QEMU?
----------------------------------------------

86Box and QEMU are both emulators, as they can both implement a whole computer system in software. However, QEMU is primarily designed to performantly translate between different instruction sets by implementing a generic CPU, and therefore doesn't try to emulate all the various quirks of the real hardware like 86Box.

Similarly to hypervisors, QEMU also implements certain fictional peripherals that are designed to reduce the emulation overhead. Again, this all is great for modern software that is not designed for a specific hardware target, but not so great for older software.

A common point of confusion is also QEMU's option to pick a specific CPU to be emulated, similarly to 86Box. This however only has the effect of changing the reported CPU identification (``CPUID`` instruction in x86) and does not impact the behavior of the emulation in any way.

What is the difference between 86Box and PCem?
----------------------------------------------

86Box and PCem are both PC system emulators. In fact, 86Box originally started out as a fork of PCem in 2016. However, the codebases of both emulators have since then diverted by a lot. Because of this, features and bugs found in one emulator do not necessarily have to be present in the other.

In general, 86Box focuses more on the accuracy of emulation, especially for older 8088/8086 based systems. This makes it more compatible with older applications, games and demos that make use of clever hardware tricks to make do with the limited computing power of the time.

Meanwhile, PCem often takes various shortcuts to improve performance at the cost of accuracy, which does end up limiting the selection of software it can run.

My virtual machine does not run at 100% speed, what do I do?
------------------------------------------------------------

If the emulation speed is consistently way under 100%, then your configuration is too demanding for your host system. Try to pick a slower emulated CPU speed.

However, if you only experience casual drops in emulation speeds, you should not instantly worry, as the guest might simply be doing some heavy I/O operations.

What is the top VM configuration my system will handle?
-------------------------------------------------------

There is no formula that would tell you this. In general, the higher the host's IPC (instructions per clock) rating, the higher emulated CPU speeds it can handle. However, the emulation speeds also depend on the kind of software that runs in the virtual machine.

Therefore, the best way to optimize your virtual machine configuration is simply trial and error.

Are you going to add emulation of the Pentium 3 and/or newer CPUs?
------------------------------------------------------------------

In short, no. Newer CPUs are way too powerful and even the top-end systems that are currently on the market are not nearly performant enough to be able to emulate them at usable speeds. In fact, we already had to add some low-clocked variants of the Pentium 2 that never actually existed, just so more people could use it!

For further reading, team member RichardG wrote a `blog post <86box.net/2022/03/21/why-not-p3>`_ that goes into the details of what makes the emulation of newer CPUs so controversial.
