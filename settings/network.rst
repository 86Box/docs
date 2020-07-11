Network
=======

The *Sound* page contains settings related to the emulated machine's network connectivity.

Network type
------------

Network connection type to emulate.

* **None:** disable networking.
* **PCap:** connect directly to a host network adapter, similarly to the *Bridge* setting of other virtualizers. `Npcap <https://nmap.org/npcap/>`_ must be installed, and the host system must be connected to a **wired network**, as support for wireless network adapters is rare.
* **SLiRP:** create a virtual network, similarly to the *NAT* setting of other virtualizers.

   * SLiRP will automatically provide the guest with an IP address through DHCP, but if you are unable to use DHCP, use the following settings:

      * IP address: 10.0.2.15
      * Subnet mask: 255.255.255.0
      * Default gateway: 10.0.2.2
      * DNS server: 10.0.2.3

   * SLiRP does not allow the host machine to communicate directly with the guest machine. If you are running a server on the guest machine, see :ref:`port-forwarding`.

.. note:: PCap can still be used with wireless connections if you install and configure the *Microsoft Loopback Adapter*, then use Windows' *Internet Connection Sharing* feature to share the host's connection with the Loopback Adapter, and configure PCap to use that adapter.

PCap device
-----------

The host network adapter to use for PCap mode. If you aren't seeing any adapters, make sure Npcap is installed correctly.

Network adapter
---------------

Network card to emulate.

The *Configure* button opens a new window with settings specific to the selected network card, such as the I/O port and IRQ for ISA cards.

.. _port-forwarding:

Advanced: SLiRP port forwarding
-------------------------------

Port forwarding allows other machines to connect to TCP or UDP servers running on the guest system through the host's IP address. Port forwarding can be enabled by manually editing the configuration file (``86box.cfg`` by default) to add a ``[SLiRP Port Forwarding]`` section.

Port forwards are numbered starting from zero. The following configuration directives are available under the ``[SLiRP Port Forwarding]`` section (assuming port forward number 0):

* ``0_udp``: If this directive is missing or set to 0, forward a TCP port. If set to 1, forward an UDP port.
* ``0_from``: Port number on the host.
* ``0_to``: Port number on the guest. If this directive is missing, use the same port number as the host.

.. rubric:: Example: forwarding host TCP port 8080 to guest port 80, and host UDP port 5555 to guest port 5555

.. code-block:: none
   
   [SLiRP Port Forwarding]
   0_from = 8080
   0_to = 80
   1_udp = 1
   1_from = 5555
