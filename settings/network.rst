.. include:: /include.rst

|network| Network
=================

The *Network* page contains settings related to the emulated machine's network connectivity.

Network type
------------

Network emulation mode to use. See :doc:`../hardware/network` for more information on these.

* **None:** disable networking.
* **PCap:** connects directly to a host network adapter. Similar to the **Bridge** mode on other emulators and virtualizers.
* **SLiRP:** creates a private network with a virtual router. Similar to the **NAT** mode on other emulators and virtualizers.

PCap device
-----------

Host network adapter to use for PCap mode. If no adapters appear in this list, make sure PCap is :ref:`enabled on your host and a supported network connection is present <hardware/network:PCap>`.

Network adapter
---------------

Network card to emulate. Only cards supported by the machine's expansion buses will be listed.

The *Configure* button opens a new window with settings specific to the selected network card, such as the I/O port and IRQ for ISA cards.

The **[LPT] Parallel Port Internet Protocol** network adapter requires a **PLIP Network** device to be attached to a :ref:`parallel port <settings/ports:Parallel port 1-4>`.
