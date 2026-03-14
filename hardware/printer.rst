Printer
=======

This page lists the available printer types, their behavior and quirks.

Generic Text Printer
--------------------

The most basic printer. It saves whatever you throw at it as a `.txt` file.

Generic ESC/P 2 Dot-Matrix Printer
----------------------------------

ESC/P is a printing language made by Epson. This printer saves pages as `.png` files and has a primitive color support: fully cyan, magenta, yellow, black, red, green and blue. Currently, two modes are emulated.

Epson EX-1000
^^^^^^^^^^^^^

A 9-pin ESC/P printer released in 1987, one of the few supporting moving in all four directions of the page (most printers can't move up). In case your guest OS doesn't support this printer, use one of these in that order:

EX-800, FX-286, FX-185, FX-85, JX-80, FX-100+, FX-80+, FX-100, FX-80, HS-80, MX-100 Type III, MX-82 F/T Type III, MX-80 F/T Type III, MX-80 Type III, MX-100, MX-82, MX-80 F/T Type II, MX-80 Type II, MX-80

ESC/P 2
^^^^^^^

A generic printer supporting a subset of the ESC/P's second version. Notably, it can't print a test page yet.

Options
^^^^^^^

There are a few options besides selecting a type of printer.

* **Paper size** is self-explanatory.
* **Quality** lets you switch between draft, in which a dot-matrix 6x9 font is used, and (near in 9-pin printers) letter quality that uses FreeSerif, FreeSans, FreeMono and a few other fonts.
* **Auto LF** sends a line feed automatically after carriage return. It's meant to be used with programs that don't do that themselves. Currently it's unknown what programs exhibit such behavior.

Issues
^^^^^^

Emulation speed drops to 1-2% when you print on Windows 9x unless ECP/EPP is disabled in BIOS setup.

Generic PostScript Printer
--------------------------

A printer that either saves raw PostScript data as a `.ps` file or uses Ghostscript to convert such data to a `.pdf` document. It has full color support and embeds fonts in documents.

Early Windows versions have a printer model "PostScript printer" that doesn't support color even if there are some supported printers that do print in color.

Generic PCL Printer
-------------------

Printer Command Language was made by HP. Similarly to the PostScript printer, it can either print raw received data in `.pcl` or `.pxl` format or convert it to `.pdf` with Ghostscript. An emulated printer can support one of the following standards:

* PCL 5e (enhanced), introduced in 1992 with HP LaserJet 4
* PCL 5c (color), introduced in 1992 with HP PaintJet 300XL and HP Color LaserJet
* HP-RTL (Raster Transfer Language), a subset of PCL
* PCL 6, also known as PXL, introduced in 1995
