|ports| Ports (COM & LPT)
=========================

The **Ports (COM & LPT)** page contains settings related to the emulated machine's I/O ports.

.. note:: The **serial port passthrough** options previously available here are now part of the *Serial Passthrough*, *Named Pipe* and *Virtual Console* :ref:`serial devices <settings/ports:COM1-4>`.

|parallel_ports| Parallel ports
-------------------------------

Internal LPT ECP DMA
^^^^^^^^^^^^^^^^^^^^

ISA DMA channel number to use for the on-board parallel port's Extended Capabilities Port mode. Only available on machines with physical DMA configuration jumpers for an on-board ECP-capable parallel port.

LPT1-4
^^^^^^

The check box (left) enables emulation of the corresponding parallel port. Any ports not provided by the machine's motherboard will be emulated as generic ISA or VLB parallel cards.

.. note:: The LPT4 port is not widely supported. It is located at I/O port 268h.

The dropdown (middle) selects an emulated device to connect to the parallel port; click |clear| to search for devices by name. The following devices are supported:

* **None:** no device connected.
* **Disney Sound Source:** sound device with a resistor ladder DAC (digital-to-analog converter) and FIFO, supported by many games.
* **LPT DAC / Covox Speech Thing:** sound device with a simple resistor ladder DAC, supported by many games (through compatibility with the *Disney Sound Source* above), demos and trackers.
* **Stereo LPT DAC:** stereo version of the LPT DAC, using the *Strobe* pin to select the active output channel.
* **Generic Text Printer:** simple printer capable of outputting text only.

  * Printed documents are saved as .txt files in the ``printer`` subdirectory found in the emulated machine's directory.

* **Generic ESC/P 2 Dot-Matrix:** EPSON ESC/P 2-compatible printer.

  * Printed pages are saved as .png files in the ``printer`` subdirectory found in the emulated machine's directory.
  * The printer type, paper size and print quality (draft quality uses a dot-matrix font and letter quality uses TrueType fonts) can be configured through the *Configure* button.
  * Use these printer drivers according to the selected printer type for best results:

    * *EX-1000* (in order): EPSON EX-1000, EX-800, FX-286, FX-185, FX-85, JX-80, FX-100+, FX-80+, FX-100, FX-80, HS-80, MX-100 Type III, MX-82 F/T Type III, MX-80 F/T Type III, MX-80 Type III, MX-100, MX-82, MX-80 F/T Type II, MX-80 Type II, MX-80
    * *ESC/P 2*: EPSON LQ-2500

  * If the emulation speed decreases drastically during printing, disable ECP/EPP mode in the emulated machine's BIOS setup.

* **Generic PostScript Printer:** PostScript-compatible printer with PDF output.

  * Printed documents are saved as .ps files in the ``printer`` subdirectory found in the emulated machine's directory. These files are automatically converted to .pdf once printing is completed; this conversion can be disabled by setting *Language* to *Raw* through the *Configure* button.
  * The original .ps files may remain in the directory if PDF conversion fails, or (on Windows x64 hosts) if the included ``gsdll64.dll`` file is missing from the 86Box directory. PDF conversion is not available on Windows ARM hosts.
  * Use the generic PostScript printer driver provided by your operating system; note that generic drivers may support grayscale only.
  * Windows 95 and newer do not have a generic PostScript driver; use the **Apple LaserWriter IIf** driver for grayscale, or the **Apple Color LW 12/660 PS** driver for color.

* **Generic PCL Printer:** HP Printer Command Language-compatible printer.

  * Printed documents are saved as .pcl or .pxl files in the ``printer`` subdirectory found in the emulated machine's directory.
  * The GhostPCL library required to convert output files to .pdf is not included with 86Box due to a license incompatibility. Set *Language* to *Raw* through the *Configure* button to remove the warning displayed on startup.
  * The following PCL standards can be selected through the *Configure* button:

    * *PCL 5e* (enhanced): introduced in 1992 with HP LaserJet 4;
    * *PCL 5c* (color): introduced in 1992 with HP PaintJet 300XL and HP Color LaserJet;
    * *HP-RTL* (Raster Transfer Language): a subset of PCL;
    * *PCL 6* (PXL): introduced in 1995.

* **Parallel Line Internet Protocol:** a `PLIP <https://en.wikipedia.org/wiki/Parallel_Line_Internet_Protocol>`_ cable connected to the :doc:`emulated network <network>`.

  * The :ref:`emulated network adapter <settings/network:Adapter>` must also be set to **[LPT] PLIP**.
  * PLIP is compatible with the DOS ``plip.com`` packet driver and the Linux ``plip`` driver (only with interrupts enabled). It is not compatible with the Windows *Direct Cable Connection* feature or any other parallel port networking implementations.
  * PLIP only works with the **SLiRP** :ref:`network type <settings/network:Mode>` due to its point-to-point nature.

* **Loopback Plug:** a parallel plug with pins wired together in a specific manner, for use with diagnostic software.

  * Different wirings can be selected through the *Configure* button.

The *Configure* button (right) opens a new window with settings specific to the selected device, such as the output file format for printers.

|serial_ports| Serial ports
---------------------------

COM1-4
^^^^^^

The check box (left) enables emulation of the corresponding serial port. Any ports not provided by the machine's motherboard will be emulated as generic ISA or VLB serial cards.

The dropdown (middle) selects an emulated device to connect to the serial port; click |clear| to search for devices by name. The following devices are supported:

* **None:** no device connected.
* **Serial Passthrough:** connect to a serial port on the host system.

  * The host port's parameters (baud rate, parity, data bits and stop bits) are automatically configured to match the emulated port's parameters, unlike in previous 86Box versions which required manual configuration in the passthrough settings.

* **Named Pipe:** create or connect to a named pipe on the host system.

  * On Windows hosts, *Auto* mode creates or connects to the pipe depending on whether or not it already exists, *Server* mode always creates the pipe and *Client* mode always connects to an existing pipe. The ``\\.\pipe\`` prefix is optional.
  * On Linux and macOS hosts, two pipes are created (adding ``.in`` and ``.out`` suffixes to the *Pipe path*) for bidirectional communication:

    .. list-table::
     :header-rows: 1
     :widths: 73 287 287

     * - Mode
       - ``.in`` pipe function
       - ``.out`` pipe function

     * - Auto
       - Same as Client mode if an application is already reading from this pipe; otherwise, same as Server mode
       - Opposite direction of ``.in`` pipe

     * - Server
       - Write data to emulated machine
       - Read data from emulated machine

     * - Client
       - Read data from emulated machine
       - Write data to emulated machine

  * On Linux and macOS hosts, the *Pipe path* can also point to a character device (such as a pseudoterminal created by the **Virtual Console** device on another emulated machine), in which case the *Auto* and *Client* modes will connect to that device instead.

* **File:** write all outgoing data to a file and/or read incoming data from a file on the host system.

  * If *Append to file if it exists* is unchecked, the outgoing data file is cleared every time the emulated machine is started or hard reset.

* **Virtual Console:** connect to a terminal on the host system, in one of multiple modes.

  * On Windows hosts, this device always connects to a Command Prompt window (limited to one per emulated machine). The modes below are only available on Linux and macOS hosts.
  * *Use standard input/output* connects to stdin and stdout, available when starting the machine directly from a terminal through the ``-P``/``--vmpath`` command line option.
  * *Create pseudoterminal* creates a PTY device, connects to it and displays its path when the machine is started.

    * The **Named Pipe** device can be used to manually connect another machine to the pseudoterminal.

  * *Start terminal emulator* connects to the system's default terminal emulator.

    * On Linux hosts, ``xdg-terminal-exec`` or ``x-terminal-emulator`` is used; if neither of those is available, a suitable terminal is guessed.
    * On macOS hosts, the Apple Terminal app is always used; note that its default settings keep the terminal window open after the port is disconnected.

  * *Run custom command* creates a PTY device, connects to it and executes the configured *Custom command*.

    * The default command (leave blank to restore it) connects to a new GNU Screen session, which runs in the background and can be attached to by running ``screen -r`` on a terminal.
    * Variables ``$PTY`` (path to the PTY device), ``$VMNAME`` (machine :ref:`display name <usage/manager:Machine list>`), ``$PORT`` (emulated port name such as ``COM1``) and ``$PIPECMD`` (command used in *Start terminal emulator* mode) are passed to the command.

* **Loopback Plug:** a serial plug with pins wired together in a null-modem configuration, for use with diagnostic software.

The *Configure* button (right) opens a new window with settings specific to the selected device, such as the host serial port to use for passthrough.
