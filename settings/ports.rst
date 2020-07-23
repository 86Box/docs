Ports (COM & LPT)
=================

The *Ports (COM & LPT)* page contains settings related to the emulated machine's I/O ports.

LPT1-3 Device
---------------

Emulated device to connect to the given parallel (LPT) port.

* **None:** no device connected.
* **Disney Sound Source:** sound device with a resistor ladder DAC (digital-to-analog converter) and FIFO, supported by many games.
* **LPT DAC / Covox Speech Thing:** sound device with a resistor ladder DAC, supported by many games (through compatibility with the *Disney Sound Source* above), demos and trackers.
* **Stereo LPT DAC:** stereo version of the LPT DAC, using the *Strobe* pin to select the active output channel.
* **Generic Text Printer:** simple printer capable of outputting text only.

   * Printed documents are saved as .txt files in the ``printer`` directory.

* **Generic ESC/P Dot-Matrix:** EPSON ESC/P compatible printer. The FreeType library file must be present in the 86Box directory for this printer to operate.

   * Printed pages are saved as .png files in the ``printer`` directory.
   * Use the **EPSON LQ-2500** printer driver for best results.

* **Generic PostScript Printer:** PostScript compatible printer. The GhostScript library file must be present in the 86Box directory for this printer to output PDF files.

   * Printed documents are saved as .pdf (or .ps if GhostScript is missing) files in the ``printer`` directory.
   * Use the generic PostScript printer driver provided by your operating system.
   * Windows 95 and newer do not have a generic PostScript driver; use the **Apple LaserWriter IIf** or **IIg** driver instead.

Serial port 1-4
---------------

Enable emulation of serial ports ranging from COM1 to COM4. Any ports not supported by the motherboard itself will be emulated as generic ISA or VLB serial cards.

Parallel port 1-3
-----------------

Enable emulation of parallel ports ranging from LPT1 to LPT3. Any ports not supported by the motherboard itself will be emulated as generic ISA or VLB parallel cards.
