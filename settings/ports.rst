.. include:: /include.rst

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

The check box (left) enables emulation of the specified parallel port. Any ports not provided by the machine's motherboard will be emulated as generic ISA or VLB parallel cards.

.. note:: The LPT4 port is not widely supported. It is located at I/O port 0268h.

The dropdown (middle) selects an emulated device to connect to the parallel port:

* **None:** no device connected.
* **Disney Sound Source:** sound device with a resistor ladder DAC (digital-to-analog converter) and FIFO, supported by many games.
* **LPT DAC / Covox Speech Thing:** sound device with a simple resistor ladder DAC, supported by many games (through compatibility with the *Disney Sound Source* above), demos and trackers.
* **Stereo LPT DAC:** stereo version of the LPT DAC, using the *Strobe* pin to select the active output channel.
* **Generic Text Printer:** simple printer capable of outputting text only.

  * Printed documents are saved as .txt files in the ``printer`` subdirectory found in the emulated machine's directory.

* **Generic ESC/P 2 Dot-Matrix:** EPSON ESC/P 2-compatible printer.

  * Printed pages are saved as .png files in the ``printer`` subdirectory found in the emulated machine's directory.
  * Paper size and print quality can be configured through the *Configure* button.
  * Use the **EPSON LQ-2500** printer driver for best results.

* **Generic PostScript Printer:** PostScript-compatible printer with PDF output.

  * Printed documents are saved as .ps files in the ``printer`` subdirectory found in the emulated machine's directory. These files are automatically converted to .pdf once printing is completed; this conversion can be disabled by setting *Language* to *Raw* through the *Configure* button.
  * The original .ps files may remain in the directory if PDF conversion fails, or (on Windows hosts) if the included ``gsdll32.dll`` or ``gsdll64.dll`` file is missing from the 86Box directory.
  * Use the generic PostScript printer driver provided by your operating system.
  * Windows 95 and newer do not have a generic PostScript driver; use the **Apple LaserWriter IIf** driver for grayscale, or the **Apple Color LW 12/660 PS** driver for color.

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

The check box (left) enables emulation of the specified serial port. Any ports not provided by the machine's motherboard will be emulated as generic ISA or VLB serial cards.

The dropdown (middle) selects an emulated device to connect to the serial port:

* **None:** no device connected.
* **Serial Passthrough:** connect to a serial port on the host system.

  * The serial port's parameters (baud rate, parity, data bits and stop bits) are controlled directly by the emulated machine, unlike in previous 86Box versions which required configuring those separately in the passthrough settings.

* **Named Pipe:** connect to a named pipe on the host system.

  * On Windows hosts, the *Pipe path* does not require a ``\\.\pipe\`` prefix.
  * On Linux and macOS hosts, two pipes are created (adding ``.in`` and ``.out`` suffixes to the *Pipe path*) for bidirectional communication:

    .. list-table::
     :header-rows: 1
     :widths: 1 999 999

     * - Mode
       - ``.in`` pipe function
       - ``.out`` pipe function

     * - Auto
       - Send data from emulated machine to pipe if an application is already reading from it, otherwise send data from pipe to emulated machine
       - Opposite of ``.in`` pipe

     * - Server
       - Write data to emulated machine
       - Read data from emulated machine

     * - Client
       - Read data from emulated machine
       - Write data to emulated machine

* **File:** write all data to a file and/or read data from a file on the host system.
* **Virtual Console:** connect to a terminal on the host system, in one of multiple modes.

  * On Windows hosts, this device always connects to a Command Prompt window (limited to one per emulated machine); the modes below are only available on Linux and macOS hosts.
  * *Use standard input/output* connects to stdin and stdout, available when starting the machine directly from a terminal through the ``-P``/``--vmpath`` command line option.
  * *Create pseudoterminal* creates a PTY pseudoterminal, connects to it and displays its device path when the machine is started.
  * *Start terminal emulator* connects to the system's default terminal emulator.

    * On Linux hosts, ``xdg-terminal-exec`` or ``x-terminal-emulator`` is used; if neither of those is available, a suitable terminal is guessed.
    * On macOS hosts, the Apple Terminal app is always used; note that its default settings keep the terminal window open after the port is disconnected.

  * *Run custom command* creates a PTY pseudoterminal, connects to it and executes the configured *Custom command*.

    * The default command (leave blank to restore it) starts a GNU Screen session, which runs in the background and can be attached to by running ``screen -r`` on a terminal.
    * Variables ``$PTY`` (device path to the pseudoterminal), ``$VMNAME`` (machine :ref:`display name <usage/manager:Machine list>`) and ``$PORT`` (emulated port name such as ``COM1``) are passed to the command.

* **Loopback Plug:** a serial plug with pins wired together in a null-modem configuration, for use with diagnostic software.

The *Configure* button (right) opens a new window with settings specific to the selected device, such as the host serial port to use for passthrough.
