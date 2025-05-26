Advanced builds
===============

The `86Box Jenkins <https://ci.86box.net/job/86Box/>`_ provides all kinds of pre-release testing builds for advanced users. These are linked to the `86Box git repository on GitHub <https://github.com/86Box/86Box>`_; a new build is produced with the latest source code every time the repository is updated.

.. important:: Testing builds are development snapshots which may contain bugs, unfinished features or other issues. These should only be used if you know what you're doing.

Variants
--------

86Box builds are available in a number of variants. The Jenkins page will automatically detect the recommended variant for the system you're viewing it on, but if you're downloading builds for a different system (or you have disabled JavaScript), use the guide below to select a variant:

* The **Old Recompiler** is recommended. The **New Recompiler** is in beta; you may experience bugs and performance loss with it.

  * The Old Recompiler is not available for the ARM architecture. You must select the New Recompiler for running 86Box on ARM Linux systems.

* On **Windows**, **x64** is the only option, as native ARM builds are currently not provided.

* On **Linux**, select **x64** or **ARM** according to your system's architecture.

* On **macOS**, **Universal** supports both Intel and Apple Silicon Macs.

  * The New Recompiler is always used on Apple Silicon due to its ARM architecture, even if the Old Recompiler is selected.

Discontinued variants
^^^^^^^^^^^^^^^^^^^^^

These variants are no longer built by Jenkins and can only be :doc:`compiled from source <buildguide>`.

* 32-bit variants (**x86** and **ARM32**) as of September 3rd 2024.

  * These variants were eliminated to better focus development on relevant 64-bit architectures, since systems old enough to be 32-bit-only lack the performance for a satisfactory emulation experience.

* Debug variants (**86Box-Debug**) as of April 2nd 2023.

  * These variants were compiled with debug symbols and reduced optimizations to help with running the emulator under ``gdb`` or other debuggers. They were eliminated as the setup process for debugging grew closer to just compiling from source instead.

* Dev variants (**86Box-Dev** and **86Box-DevODR**) as of November 18th 2021.

  * These variants contained incomplete and experimental features subject to change at any time, with the -Dev variant also containing the New Recompiler beta.

* Optimized variants (**86Box-Optimized**) as of March 18th 2021.

  * These variants' aggressive microarchitecture-specific optimizations provided very little performance improvement (within margin of error on modern CPUs) while introducing bugs and other incorrect behavior.
