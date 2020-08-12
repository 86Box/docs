Advanced builds
===============

The `86Box Jenkins <https://ci.86box.net/>`_ provides all kinds of pre-release testing builds for advanced users. These are linked to the `86Box git repository on GitHub <https://github.com/86Box/86Box>`_; a new build is produced with the latest source code every time the repository is updated.

.. important:: Testing builds are development snapshots which may contain bugs, incomplete features or other issues. These should only be used if you know what you're doing.

Standard
--------

Standard builds (**86Box**) are compiled with default options. Release versions of 86Box are based on these.

Debug
-----

Debug builds (**86Box-Debug**) are :ref:`standard builds <dev/builds:Standard>` compiled with debug symbols and no optimizations, to allow for debugging with ``gdb`` and other tools if you don't have a full 86Box development setup. These run slower than standard builds due to the removal of optimizations and addition of debugging features.

Development
-----------

Development builds (**86Box-Dev**) are compiled with ``DEV_BUILD=y``, enabling additional features which are currently under development. These new features might not work, either partially or entirely, and the development team reserves the right to change or remove them at any time.

Optimized
---------

Optimized builds (**86Box-Optimized**) are :ref:`standard builds <dev/builds:Standard>` which have been optimized for use with a specific CPU family on the host machine. These provide slight performance improvements, especially on older or low-end hosts; however, the aggressive optimizations employed **may result in bugs** not present on standard builds.

There are many different optimized binaries available for each build; you must download the **correct one for your host CPU**, otherwise, 86Box will run poorly or even crash. The table below lists most CPUs currently supported by optimized builds, along with the respective binaries you should use with them, as well as their codenames (as shown on an identification tool such as `CPU-Z <http://www.cpuid.com/softwares/cpu-z.html>`_):

.. raw:: html

  <table class="docutils align-default">
  <tr><th align="left">Binary</th><th align="left">CPUs</th><th align="left">Codenames</th></tr>
  <tr><th colspan="3" align="left">Intel</th></tr>
  <tr><td>Core2</td><td>Core 2 Duo/Quad<br/>Pentium Dual-Core</td><td>Conroe, Allendale, Merom,<br/>Kentsfield, Wolfdale, Yorkfield</td></tr>
  <tr><td>Nehalem</td><td>1st generation Core</td><td>Bloomfield, Lynnfield, Gulftown,<br/>Arrandale, Clarkdale, Clarksfield</td></tr>
  <tr><td>SandyBridge</td><td>2nd/3rd generation Core</td><td>Sandy Bridge, Ivy Bridge</td></tr>
  <tr><td>Haswell</td><td>4th/5th generation Core</td><td>Haswell, Broadwell</td></tr>
  <tr><td>Skylake</td><td>6th/7th/8th/9th/10th generation Core</td><td>Skylake, Kaby Lake, Coffee Lake,<br/>Whiskey Lake, Amber Lake, Comet Lake</td></tr>
  <tr><td>IceLake</td><td>10th/11th generation Core</td><td>Ice Lake, Tiger Lake, Rocket Lake</td></tr>
  <tr><td>Bonnell</td><td>Atom (2008-2012)</td><td>Silverthorne, Diamondville, Lincroft,<br/>Pineview, Cedar Trail, Cover Trail</td></tr>
  <tr><td rowspan="2">Silvermont</td><td>Atom (2013+)</td><td>Bay Trail, Cherry Trail, Braswell</td></tr>
  <tr><td>N/J-series Celeron/Pentium</td><td>Bay Trail, Braswell, Apollo Lake,<br/>Gemini Lake, Skyhawk Lake</td></tr>
  <tr><th colspan="3" align="left">AMD</th></tr>
  <tr><td>K8 *</abbr></td><td colspan="2">All (2005-2007)</td></tr>
  <tr><td>K10</td><td colspan="2">All (2008-2010)</td></tr>
  <tr><td>Bobcat</td><td>Athlon (2011+)<br/>FX<br/>A/C/E-Series APU</td><td>Ontario, Zacate, Hondo, Llano, Trinity,<br/>Richland, Kabini, Kaveri, Beema, Mullins,<br/>Carrizo, Bristol Ridge, Stoney Ridge</td></tr>
  <tr><td rowspan="2">Zen</td><td>Ryzen 1000/2000 CPU<br/>Ryzen 2000/3000 APU **</td><td>Summit Ridge, Raven Ridge, Dali,</br>Pinnacle Ridge, Picasso</td></tr>
  <tr><td>Ryzen Threadripper 1000/2000</td><td>Whitehaven, Colfax</td></tr>
  <tr><td rowspan="2">Zen2</td><td>Ryzen 3000/4000 CPU<br/>Ryzen 4000 APU **</td><td>Matisse, Renoir, Vermeer</td></tr>
  <tr><td>Ryzen Threadripper 3000</td><td>Castle Peak</td></tr>
 
  </table>

| \* Older K8 CPUs without SSE3 are not supported.
| \*\* Ryzen APU = models equipped with integrated graphics, including G-series on desktop and U/H-series on mobile. These are always one generation behind; the model numbers are misleading.
