Network
=======

The *Network* page contains settings related to the emulated machine's network connectivity.

Network type
------------

Network emulation mode to use. See :doc:`../hardware/network` for more information on these.

* **None:** disable networking.
* **PCap:** connects directly to a host network adapter. Similar to the **Bridge** mode on other virtualizers.
* **SLiRP:** creates a private network with a virtual router. Similar to the **NAT** mode on other virtualizers.

PCap device
-----------

Host network adapter to use for PCap mode. If no adapters appear on this list, make sure that:

* A WinPcap-compatible driver is installed;
* The installed driver is compatible with your version of Windows;
* At least one compatible (wired) network adapter is present.

Network adapter
---------------

Network card to emulate. Only cards supported by the machine's expansion buses will be listed.

The *Configure* button opens a new window with settings specific to the selected network card, such as the I/O port and IRQ for ISA cards.
