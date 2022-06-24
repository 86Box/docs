.. include:: /include.rst

|display| Display
=================

The **Display** page contains settings related to the emulated machine's 2D and 3D video cards.

Video
-----

Video card to emulate. This box only lists cards supported by the machine's expansion buses. On machines equipped with an onboard video chip, the *Internal* option enables the onboard video.

The *Configure* button opens a new window with settings specific to the selected video card, such as the amount of video memory.

Voodoo Graphics
---------------

Emulate a **3dfx Voodoo** add-on 3D accelerator, connected to both the PCI bus and the video card selected above.

The *Configure* button provides the following settings:

* **Voodoo type:** type of Voodoo card to emulate.

   * **Voodoo Graphics:** the original Voodoo model, with a single Texture Mapping Unit operating at 50 MHz.
   * **Obsidian SB50 + Amethyst:** a variant of the Voodoo Graphics, with two Texture Mapping Units operating at 50 MHz.
   * **Voodoo 2:** the second Voodoo model, with two Texture Mapping Units operating at 90 MHz, as well as SLI support.

.. note:: The **Voodoo Banshee** and **Voodoo 3** are independent video cards, which are not found here; they must be selected on the :ref:`settings/display:Video` box above. For these cards, the *Configure* button next to the :ref:`settings/display:Video` box provides similar settings to the ones listed here.

* **Framebuffer memory size** / **Texture memory size**: amount of video memory for the Frame Buffer Interface and Texture Mapping Unit(s), respectively.
* **Bilinear filtering:** apply bilinear filtering to smooth out textures displayed on screen.
* **Screen Filter:** apply a filter to make the screen picture resemble the DAC (digital-to-analog converter) output of a real Voodoo card.
* **Render threads:** split the workloads of each Voodoo card into different CPU threads for faster emulation. The recommended amount of render threads depends on your host system's CPU core count, and whether or not Voodoo 2 SLI is enabled:

+----------+--------------------------+
|Host cores|Recommended render threads|
|          +-----------+--------------+
|          |Single card|Voodoo 2 SLI  |
+==========+===========+==============+
|2         |1          |1             |
+----------+-----------+--------------+
|4         |2          |1             |
+----------+-----------+--------------+
|6 or 8    |4          |2             |
+----------+-----------+--------------+
|10 or more|4          |4             |
+----------+-----------+--------------+

* **SLI:** add a second Voodoo 2 card to the system, connected to the first one through a Scan Line Interleave (SLI) interface.
* **Recompiler:** enable the Voodoo recompiler for faster emulation.

8514/A
------

Emulate an **IBM 8514/A** add-on graphics accelerator. Both the original IBM card for the MCA bus and a generic clone card for the ISA bus are available; the correct card is automatically selected based on the machine's supported expansion buses.

.. note:: Pairing the 8514/A with a video card from **S3** may result in compatibility issues, as those cards implement a subset of the 8514/A's features.

XGA
------

(place description here)
