.. include:: /include.rst

|network| Network
=================

The **Network** page contains settings related to the emulated machine's network connectivity.

Network Card #1-#4
------------------

Network interface cards to emulate. Up to 4 independent network cards are supported.

Mode
^^^^

Network emulation mode to use on this card. See :doc:`../hardware/network` for more information on these.

* **None:** disable networking.
* **PCap:** connects directly to a host network adapter. Similar to the **Bridge** mode on other emulators and virtualizers.
* **SLiRP:** creates a private network with a virtual router. Similar to the **NAT** mode on other emulators and virtualizers.

Interface
^^^^^^^^^

Host network adapter to use for PCap mode on this card. If no adapters appear on this list, make sure that:

* A WinPcap-compatible driver is installed;
* The installed driver is compatible with your version of Windows;
* At least one compatible (wired) network adapter is present.

Adapter
^^^^^^^

Network card to emulate. Only cards supported by the machine's expansion buses will be listed.

The *Configure* button opens a new window with settings specific to the selected network card, such as the I/O port and IRQ for ISA cards.

The **[LPT] Parallel Port Internet Protocol** network adapter requires a **PLIP Network** device to be attached to a :ref:`parallel port <settings/ports:Parallel port 1-4>`.
