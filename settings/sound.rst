Sound
=====

The *Sound* page contains settings related to the emulated machine's audio hardware.

Sound card
----------

Sound card to emulate. Only cards supported by the machine's expansion buses will be listed. On machines equipped with an onboard sound chip, the *Internal* option enables the onboard sound.

The *Configure* button opens a new window with settings specific to the selected sound card, such as the I/O ports, IRQ and DMA channels for ISA cards.

MIDI Out Device
---------------

Device to output MIDI music to, for sound cards equipped with an external MIDI output.

* **None:** don't output MIDI music.
* **FluidSynth:** a software soundfont synthesizer. The FluidSynth library file must be present in the 86Box directory, and a soundfont must be configured.
* **Roland MT-32 Emulation:** emulate a Roland MT-32 synthesizer device. Emulation is provided by the `Munt <http://munt.sourceforge.net>`_ library.
* **Roland CM-32L Emulation:** same as above, but emulating a Roland CM-32L instead.
* **System MIDI:** output to a (configurable) host MIDI device, such as the Windows software synthesizer or a USB MIDI adapter.

The *Configure* button opens a new window with settings specific to the selected output device.

MIDI In Device
--------------

Device to receive MIDI music from, for sound cards equipped with an external MIDI input.

* **None:** don't receive MIDI music.
* **System MIDI:** receive from a (configurable) host MIDI device, such as a USB MIDI adapter.

The *Configure* button opens a new window with settings specific to the selected input device.

Standalone MPU-401
------------------

Emulate a standalone **Roland MIDI Processing Unit** ISA card, which allows for MIDI input and output without a MPU-401-equipped sound card.

The I/O port and IRQ can be configured through the *Configure* button.

Innovation SSI-2001
-------------------

Emulate the **Innovation SSI-2001** ISA sound card, based on the MOS Technology 6581 chip (commonly known as the Commodore SID) and supported by a limited number of games.

SID emulation is provided by the `reSID <http://www.zimmers.net/anonftp/pub/cbm/crossplatform/emulators/resid/>`_ library.

CMS / Game Blaster
------------------

Emulate the **Creative Music System** or **Game Blaster** ISA sound card, based on dual Philips SAA1099 chips and supported by some games.

Gravis Ultrasound
-----------------

Emulate the **Gravis UltraSound** ISA sound card.

The type of UltraSound to emulate (Classic or MAX), I/O port and amount of onboard RAM can be configured through the *Configure* button.

Use FLOAT32 sound
-----------------

Use the 32-bit floating point (instead of 16-bit integer) data type for audio output, which is less prone to clipping but may not work at all on some host systems. Try disabling this option if you're getting no audio output from 86Box whatsoever.
