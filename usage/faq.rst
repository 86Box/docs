Frequently asked questions
==========================

What is the difference between 86Box and applications like VirtualBox or Virtual PC?
------------------------------------------------------------------------------------

VirtualBox, Virtual PC and similar applications are *hypervisors*. For the most part, they execute code running in the virtual machine as is, and only step in whenever it is required to enforce the separation of a virtual machine from the rest of the system. This also means that the virtual machine sees the same CPU as the host system.

They also mostly implement peripherals that are custom designed to let the guest take full potential of the virtualizer as long as appropriate drivers, which are distributed with the provided additions, are installed. This is great for modern operating systems and software that is not designed for a specific hardware target, but rather an abstraction interface such as DirectX; however, running older applications and games will often lead to a suboptimal experience, as hypervisors don't tend to be designed with this usecase in mind.

On the other hand, 86Box is a *system emulator*. It implements a whole system in software, which includes the CPU, chipset and additional cards, if any. Furthermore, it interprets every single instruction running in the virtual machine, and while that comes with the obvious tradeoff of emulation being more CPU intensive than virtualization, it also makes it possible to simulate authentic behavior of the original hardware, including its speed. This in turn allows running countless games and demos that wouldn't have run in a hypervisor before, as they simply run too fast or fail to make use of various hardware quirks that don't exist in modern processors.

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

Why is 86Box unable to run Xbox-level hardware when emulators for PS3 and Switch exist?
---------------------------------------------------------------------------------------
The difference is in how high level emulation and low level emulation works. High level lets you run much faster speeds at the cost of accuracy and compatibility. See the `Emulation General Wiki <https://emulation.gametechwiki.com/index.php/High/Low_level_emulation>`_ for a detailed explanation.

Back in the late 90s, Ultra HLE came out that emulated an N64 at 100% speed on a system with a Pentium II 300. It would take another decade before computers got fast enough to do it in low level. The tradeoff is that HLE only ran about 20 games because the emulator had to be built specifically to run each game.

Simply put, think of it this way:

* **high level** = good enough to run just "these things"
* **low level** = emulate the *entire* system to run literally anything that original hardware could have run, even including the hardware incompatibilities 

In 86Box it's entirely possible to put a video card with a motherboard that would not boot and that replicates real life. Any console emulator doing PS2 or higher is doing high level emulation. This is why they have lists of compatible games - if they actually full emulated all the hardware, every game would just work because it would not know the difference but they cannot because no computer is fast enough.

My virtual machine does not run at 100% speed, what can I do to fix this?
-------------------------------------------------------------------------

If the emulation speed is consistently way under 100%, then your configuration is too demanding for your host system. Try to pick a slower emulated CPU speed.

However, if you only experience casual drops in emulation speeds, you should not instantly worry, as the guest might simply be doing some heavy I/O operations.

What is the top VM configuration my system will handle?
-------------------------------------------------------

There is no formula that would tell you this with 100% certainty. In general, the higher the host's IPC (instructions per clock) rating, the higher emulated CPU speeds it can handle. However, the emulation speeds also depend on the kind of software that runs in the virtual machine.

A good way to estimate the limit of your host setup is by looking at `single-thread benchmarks <https://www.cpubenchmark.net/singleThread.html>`_. The higher a CPU is on this list, the faster it will run 86Box.

For example:

* **~4000** = Pentium II 300
* **~3400** = Pentium II 233
* **~2600** = Pentium 200
* **~1600** = Pentium 75
* **~700**  = 486DX2 66 (assuming the gpu on such a system can keep up)

Keep in mind that these are only rough estimates. The best way to optimize your virtual machine configuration is simply trial and error.

What are some era-appropriate configurations for 86Box?
-------------------------------------------------------

* **1988** - 386DX 25MHz w/ 1MB RAM, ATI VGA Wonder, AdLib, DOS 4.01 + Windows 2.1x/386
* **1990** - 486DX 33MHz w/ 4MB RAM, Video 7 VRAM VGA + XGA, Sound Blaster 1.5 (CT1320C), DOS 4.01 + Windows 3.0
* **1992** - 486DX2 66MHz w/ 8MB RAM, S3 924 / ATI Mach32, Sound Blaster 16 or Gravis Ultrasound, DOS 5.0 + Windows 3.1
* **1994** - Pentium 100MHz w/ 32MB RAM, S3 Vision964 / ATI Mach64, Sound Blaster AWE32, DOS 6.22 + Windows 3.11
* **1996** - PPro 200 (or Pentium 200 non-mmx) w/ 64MB RAM, Matrox Mystique + Voodoo 1, Sound Blaster AWE64 Gold, Windows 95 OSR2
* **1998** - Pentium II 450MHz w/ 128MB RAM, Riva TNT + Voodoo 2 SLI, Aureal Vortex 2 / Sound Blaster Live, Windows 98 FE

Why is my emulated PS/2 mouse slow/laggy under Windows 95/98/98 SE/ME even at 100% speed?
-----------------------------------------------------------------------------------------

These operating systems set the polling rate of the mouse to 40 Hz by default, which is generally considered a really low polling rate.

Either install Microsoft IntelliPoint (3.0 for Windows 95, 4.0/4.1 for Windows 98/98 SE/ME) or use PS2Rate and select 200 Hz polling rate. The former is only recommended if the Wheel options are selected; it does not require any other programs to be enabled as it will select high polling rates by default and will work better with MS-DOS programs and games running inside the MS-DOS Prompt. Note that 4.0 requires Internet Explorer 5.5 to be installed.

Alternatively, you can check the "Update mouse every CPU frame" option in the Actions menu, but this is not accurate to the emulation and may cause noticeable performance drops.

Can I use 86Box to run a Windows XP system?
-------------------------------------------

We strongly discourage the use of 86Box to run Windows XP or newer Windows operating systems.

While the operating system does run, the Windows XP system requirements are steep compared to what 86Box can offer, and what most host systems are capable of running at 100%. Microsoft publishes the *minimum* system requirements of Windows XP to include a 233 MHz Pentium. The recommended requirements of Windows XP bump the requirements up to include a 300 MHz Pentium or better.

Even though these requirements seem modest in the present day, only some of the newest AMD (Ryzen 5000 series or better), Intel (Core 12th generation or better), and Apple (M2 or better) processors are capable of meeting the bare minimum Windows XP requirements under 86Box’s full system emulation. On top of the operating system requirements, most software and games that require Windows XP will demand even more out of the hardware than Windows XP alone, reducing the utility of Windows XP in 86Box to a very narrow set of software.

It is almost always better to run Windows XP in a different virtualizer or emulator. On AMD and Intel based PCs, software such as `VirtualBox <https://www.virtualbox.org/>`_ or `Hyper-V <https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/Install-Hyper-V?tabs=powershell&pivots=windows/>`_ can run Windows XP close to bare-metal performance, as most CPU instructions can run unmodified. On Apple macOS computers, `UTM <https://mac.getutm.app/>`_ is capable of either running Windows XP in full hardware virtualization on Intel Macs, or with highly optimized x86 emulation on M-series Macs. UTM does not chase the fine-detail historic accuracy of 86Box and as such, is able to take "shortcuts" that can allow Windows XP and software on it to run with acceptable performance even under x86 emulation.

Why doesn't 86Box have the XYZ board/card/peripheral?
-----------------------------------------------------
86Box is entirely comprised of volunteers. Any hardware added is done if someone is willing to contribute the code and work required to make it feasible. Some cards/hardware may never be in 86Box. This might be because documentation is non-existant, the hardware might be out of scope of the project, or other reasons. Asking for cards doesn't make it happen. There is a LOT of work that has to be accomplished to add anything. Anyone is welcome to contribute to the code base and make additions though, provided you follow our guidelines.

Are you going to add emulation of the Pentium III and/or newer CPUs?
--------------------------------------------------------------------

In short, no. Newer CPUs are way too powerful and even the top-end systems that are currently on the market are not nearly performant enough to be able to emulate them at usable speeds. In fact, we already had to add some low-clocked variants of the Pentium II that never actually existed, just so more people could use it!

For further reading, team member RichardG867 wrote a `blog post <https://86box.net/2022/03/21/why-not-p3>`_ that goes into the details of what makes the emulation of newer CPUs so controversial.

