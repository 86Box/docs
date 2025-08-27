External OPL Audio Support
==========================

86Box now supports the **OPL2Board** as an external audio device.  
This allows users to connect a real OPL2 (YM3812) chip through the board and use it alongside the emulator for authentic FM synthesis output.

Usage
-----

1. Connect your OPL2Board to the host system.  
2. Select the sound card **[ISA] OPL2Board [External Device]**.  
3. In the **Configure** button, select the serial port to which the board is connected.

Notes for OPL2Board
-------------------

- You need an **Arduino Nano** and an **OPL2Board** from Cheerful Electronic.
- Follow the **instructions from the manufacturer** and upload ``SerialPassthrough.ino`` to the Arduino Nano.
- If you want **PCM audio**, you can add an **additional sound card** and disable the OPL output.