External OPL audio
==================

The **OPL2Board** :ref:`sound card <settings/sound:Sound card #1-#4>` allows for a real Yamaha OPL2 (YM3812) chip to be connected to the emulated machine for authentic FM synthesis output.

Usage
-----

1. Connect the `OPL2 Audio Board from Cheerful Electronic <https://www.cheerful.nl/OPL2_Audio_Board/>`_ to a `supported Arduino board <https://github.com/DhrBaksteen/ArduinoOPL2/wiki/Connecting-the-OPL2-Audio-Board>`_.
2. Connect the Arduino board to the host system.
3. Select the **OPL2Board (External Device)** sound card on the :ref:`emulated machine's configuration <settings/sound:Sound card #1-#4>`.
4. Use the *Configure* button to select the Arduino's serial port.

.. note::
  * The **OPL3 Duo!** board is currently not supported.
  * Regular **PCM/wave audio** still requires an emulated sound card to be configured. If the emulated sound card provides its own OPL, it can often be **muted** through a mixer utility within the machine.
