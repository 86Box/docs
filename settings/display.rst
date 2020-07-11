Display
=======

The *Display* page contains settings related to the emulated machine's 2D and 3D video cards.

Video
-----

Video card to emulate. Only video cards supported by the machine's expansion buses will be listed. The *Internal* option corresponds to the onboard video chip on machines equipped with one.

The *Configure* button opens a new window with settings specific to the selected video card, such as the amount of installed video memory.

Voodoo Graphics
---------------

Emulate a **3Dfx Voodoo** or **Voodoo 2** 3D accelerator, connected to the PCI bus and to the video card selected above.

The *Configure* button provides the following settings:

Voodoo type
^^^^^^^^^^^

Type of Voodoo card to emulate.

* **Voodoo Graphics:** the original Voodoo model, with a single Texture Mapping Unit operating at 50 MHz.
* **Obsidian SB50 + Amethyst:** a variant of the Voodoo Graphics, equipped with a second Texture Mapping Unit like the Voodoo 2.
* **Voodoo 2:** the second Voodoo model, with two Texture Mapping Units operating at 90 MHz, as well as SLI support.

Framebuffer memory size / Texture memory size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Amount of video memory to give the Frame Buffer Interface and Texture Mapping Unit(s), respectively.

Bilinear filtering
^^^^^^^^^^^^^^^^^^

Apply bilinear filtering to smooth out textures displayed on screen.

Screen Filter
^^^^^^^^^^^^^

Apply a filter to make the picture resemble the digital-to-analog converter output of a real Voodoo card.

Render threads
^^^^^^^^^^^^^^

Allows the Voodoo workload to be split into multiple threads. 2 render threads are recommended for host systems with more than 2 CPU cores.

SLI
^^^

Add a second Voodoo 2 card to the system, connected to the first one through Scan Line Interleave (SLI).

Recompiler
^^^^^^^^^^

Enable the Voodoo recompiler for faster emulation.

.. note:: A host CPU with SSE2 support is required for the recompiler. SSE2 is present in most CPUs made since 2005.
