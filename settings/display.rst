.. include:: /include.rst

|display| Display
=================

The **Display** page contains settings related to the emulated machine's 2D and 3D video cards.

Video
-----

Video card to emulate. This box only lists cards supported by the machine's expansion buses. On machines equipped with an on-board video chip, the *Internal device* option enables the on-board video.

The *Configure* button opens a new window with settings specific to the selected video card, such as the amount of video memory.

Video #2
--------

Optional secondary video card to emulate. Only the **MDA**, **Hercules**, **Hercules Plus** and a limited set of **PCI VGA** cards are currently supported as secondary options. The secondary card's video output is displayed on a separate window.

As with the primary card above, the *Configure* button can be used to configure the selected card.

Voodoo Graphics
---------------

Emulate a **3dfx Voodoo** add-on 3D accelerator, connected to both the PCI bus and the video card selected above.

.. note:: The **Voodoo Banshee** and **Voodoo 3** are independent video cards, which are not found here; they must be selected on the :ref:`settings/display:Video` box above, and this Voodoo Graphics option **cannot be selected** alongside them. For these cards, the *Configure* button next to the :ref:`settings/display:Video` box provides similar settings to the ones listed below.

The *Configure* button provides the following settings:

* **Voodoo type:** type of Voodoo card to emulate.

   * **Voodoo Graphics:** the original Voodoo model, with a single Texture Mapping Unit operating at 50 MHz.
   * **Obsidian SB50 + Amethyst:** a variant of the Voodoo Graphics, with two Texture Mapping Units operating at 50 MHz.
   * **Voodoo 2:** the second Voodoo model, with two Texture Mapping Units operating at 90 MHz, as well as SLI support.

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
* **Dynamic Recompiler:** enable the Voodoo recompiler for faster emulation.

IBM 8514/A / XGA / PS/55 Display Adapter Graphics
-------------------------------------------------

Emulate an **IBM 8514/A**, **XGA** or **PS/55 Display Adapter** add-on graphics accelerator. The 8514/A is available for both MCA and ISA buses (emulating a generic clone card on the latter), while the other two are available for the MCA bus only.

The *Configure* buttons next to each card open a new window with settings specific to that card, such as the amount of video memory for the 8514/A and model type for the XGA.

.. note:: Pairing the 8514/A and XGA with each other or with video cards from **ATI** or **S3** may result in compatibility issues, as each card implements a set of 8514/A features.
