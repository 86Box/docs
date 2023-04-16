.. include:: /include.rst

|sound| Sound
=============

The **Sound** page contains settings related to the emulated machine's audio hardware.

Parallel port sound devices such as the **Disney Sound Source** and **Covox Speech Thing** are not present on this page; they can be configured through the :ref:`Ports page <settings/ports:LPT1-4 Device>`.

Sound card #1-#4
----------------

Sound cards to emulate. Up to 4 independent sound cards are supported. Only cards supported by the machine's expansion buses will be listed. On machines equipped with an onboard sound chip, the *Internal* option for sound card #1 enables the onboard sound.

The *Configure* button opens a new window with settings specific to the selected sound card, such as the I/O ports, IRQ and DMA channels for ISA cards.

Emulation for the Yamaha OPL series of synthesizers (used by many of the emulated cards) is provided by a modified `Nuked OPL3 <https://github.com/nukeykt/Nuked-OPL3>`_ or `ymfm <https://github.com/aaronsgiles/ymfm>`_ library, per the :ref:`selection below <settings/sound:FM synth driver>`.

.. note:: The **Innovation SSI-2001**, **CMS / Game Blaster** and **Gravis Ultrasound** are now selectable here, replacing the previous separate options for each.

MIDI Out Device
---------------

Device to output MIDI music to, for sound cards equipped with an external MIDI output.

* **None:** don't output MIDI music.
* **FluidSynth:** a software soundfont synthesizer. Selecting a soundfont file is required. There will be no synthesizer output if no soundfont is configured, or (on Windows hosts) if the included ``libfluidsynth.dll`` or ``libfluidsynth64.dll`` file is missing from the 86Box directory.
* **Roland MT-32**/**CM-32L Emulation:** emulate a Roland synthesizer module. Emulation is provided by the `Munt <http://munt.sourceforge.net>`_ library.
* **System MIDI:** output to a MIDI device on the host system, such as the Windows software synthesizer or a USB MIDI adapter.

The *Configure* button opens a new window with settings specific to the selected output device, such as the soundfont to use for *FluidSynth* and the host MIDI device to use for *System MIDI*.

MIDI In Device
--------------

Device to receive MIDI music from, for sound cards equipped with an external MIDI input.

* **None:** don't receive MIDI music.
* **System MIDI:** receive from a MIDI device on the host system, such as a USB MIDI adapter.

The *Configure* button opens a new window with settings specific to the selected input device, such as the host MIDI device to use for *System MIDI*.

Standalone MPU-401
------------------

Emulate a standalone **Roland MIDI Processing Unit** ISA card, which allows for MIDI input and output without a MPU-401-equipped sound card.

The I/O port and IRQ can be configured through the *Configure* button.

Use FLOAT32 sound
-----------------

Use the 32-bit floating point (instead of 16-bit integer) data type for audio output, which is less prone to clipping but may not work at all on some host systems. Try disabling this if you're getting no audio output from 86Box at all.

FM synth driver
---------------

Yamaha OPL2/3 emulation back-end to use. **Nuked** is the default, while **YMFM** may improve emulation performance at the cost of accuracy.

.. note:: **YMFM** is always used for OPL4 emulation on sound cards equipped with that synthesizer.
