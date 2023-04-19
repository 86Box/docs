.. include:: /include.rst

|ports| Ports (COM & LPT)
=========================

The **Ports (COM & LPT)** page contains settings related to the emulated machine's I/O ports.

LPT1-4 Device
-------------

Emulated device to connect to the given parallel (LPT) port.

* **None:** no device connected.
* **Disney Sound Source:** sound device with a resistor ladder DAC (digital-to-analog converter) and FIFO, supported by many games.
* **LPT DAC / Covox Speech Thing:** sound device with a simple resistor ladder DAC, supported by many games (through compatibility with the *Disney Sound Source* above), demos and trackers.
* **Stereo LPT DAC:** stereo version of the LPT DAC, using the *Strobe* pin to select the active output channel.
* **Generic Text Printer:** simple printer capable of outputting text only.

   * Printed documents are saved as .txt files in the ``printer`` subdirectory found in the emulated machine's directory.

* **Generic ESC/P Dot-Matrix:** EPSON ESC/P-compatible printer.

   * Printed pages are saved as .png files in the ``printer`` subdirectory found in the emulated machine's directory.
   * Use the **EPSON LQ-2500** printer driver for best results.
   * This printer will not work on Windows hosts if the included ``freetype.dll`` file is missing from the 86Box directory.

* **Generic PostScript Printer:** PostScript-compatible printer with PDF output.

   * Printed documents are saved as .ps files in the ``printer`` subdirectory found in the emulated machine's directory. These files are automatically converted to .pdf once printing is completed.
   * The original .ps files may remain in the directory if PDF conversion fails, or (on Windows hosts) if the included ``gsdll32.dll`` or ``gsdll64.dll`` file is missing from the 86Box directory.
   * Use the generic PostScript printer driver provided by your operating system.
   * Windows 95 and newer do not have a generic PostScript driver; use the **Apple LaserWriter IIf** driver for grayscale, or the **Apple Color LW 12/660 PS** driver for color.

* **PLIP Network:** A `Parallel Line Internet Protocol <https://en.wikipedia.org/wiki/Parallel_Line_Internet_Protocol>`_ cable connected to the :doc:`emulated network <network>`.

   * The :ref:`emulated network adapter <settings/network:Adapter>` must also be set to **[LPT] PLIP**.
   * PLIP is compatible with the DOS ``plip.com`` packet driver and the Linux ``plip`` driver (only with interrupts enabled). It is not compatible with the Windows *Direct Cable Connection* feature or any other parallel port networking implementations.
   * PLIP works best with the **SLiRP** :ref:`network type <settings/network:Mode>` due to its point-to-point nature.

Serial port 1-4
---------------

Enable emulation of serial ports ranging from COM1 to COM4. Any ports not provided by the machine's motherboard will be emulated as generic ISA or VLB serial cards.

Parallel port 1-4
-----------------

Enable emulation of parallel ports ranging from LPT1 to LPT4. Any ports not provided by the machine's motherboard will be emulated as generic ISA or VLB parallel cards.

.. note:: The 4th parallel port is not widely supported. It is located at I/O port 268h.
