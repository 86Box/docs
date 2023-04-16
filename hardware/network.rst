Networking
==========

86Box supports two connection modes for the :doc:`emulated network cards <../settings/network>`. The specific details on these connection modes and network emulation as a whole are outlined on this page.

SLiRP
-----

SLiRP creates a private network with a virtual router, allowing the emulated machine to reach the host, its network and the Internet; on the other hand, the host and other devices on its network cannot reach the emulated machine, unless :ref:`port forwarding <hardware/network:SLiRP port forwarding>` is configured. This is similar to the **NAT** mode on other emulators and virtualizers.

The virtual router provides automatic IP configuration to the emulated machine through DHCP. If that is not an option, use the following static IP settings, replacing *x* with 2, 3, 4 or 5 for the first, second, third or fourth network card to use SLiRP respectively:

* **IP address:** 10.0.\ *x*\ .15
* **Subnet mask:** 255.255.255.0
* **Default gateway:** 10.0.\ *x*\ .2
* **DNS server:** 10.0.\ *x*\ .3

The host can be reached through IP address 10.0.\ *x*\ .2, while other devices on the host's network can be reached through their normal IP addresses.

.. note:: SLiRP is only capable of routing TCP and UDP traffic. Other protocols such as IPX and NetBEUI can only be used with :ref:`hardware/network:PCap` networking.

PCap
----

PCap connects directly to one of the host's network adapters. The emulated machine must be configured as if it were a real machine on your network. This is similar to the **Bridge** mode on other emulators and virtualizers.

This mode requires `Npcap <https://nmap.org/npcap/>`_ (or another WinPcap-compatible driver) to be installed on the host. Only **wired Ethernet network connections** are compatible; Wi-Fi and other connections will not work at all, as they do not allow PCap to listen for packets bound to the emulated card's MAC address.

Private PCap network
^^^^^^^^^^^^^^^^^^^^

If you have an incompatible network connection on your host system (such as Wi-Fi), or if you wish to connect the emulated machine to the host without also connecting it to your network, a private network can be created with PCap in one of two ways:

* Install and configure the *Microsoft KM-TEST Loopback Adapter* included with Windows.

   * Guides on how to install this adapter are available online.
   * The adapter alone only provides a direct connection to the host, with no DHCP server, therefore requiring manual IP configuration on both the host and the emulated machine.
   * Windows' *Internet Connection Sharing* feature can be used to connect the emulated machine to the host's network and the Internet, with DHCP for automatic IP configuration, similarly to SLiRP but with the added benefit that the host can reach the emulated machine without port forwarding.

      * Port forwarding can be performed through Internet Connection Sharing's *Settings*.

* If VMware is installed, use one of the VMnet adapters included with it.

   * *VMnet1* (Host-only) connects to the host only.
   * *VMnet8* (NAT) connects to the host, its network and the Internet.

      * Port forwarding can be performed through the Virtual Network Editor's *NAT Settings*.

Advanced features
-----------------

The following advanced features can be accessed by directly editing the emulated machine's configuration file, which is ``86box.cfg`` by default.

MAC address
^^^^^^^^^^^

With the exception of **[LPT] Parallel Port Internet Protocol**, every emulated network card stores its MAC address in the ``mac`` directive of its respective configuration file section. Only the suffix (last three octets) of the MAC address can be edited; the prefix (first three octets) will always be an `Organizationally Unique Identifier <https://en.wikipedia.org/wiki/Organizationally_unique_identifier>`_ belonging to the manufacturer, such as ``00:E0:4C`` for Realtek.

.. container:: toggle-always-show

    .. container:: toggle-header

        Example: MAC address ``00:E0:4C:35:F4:C2`` for the Realtek RTL8029AS

    .. code-block:: none

        [Realtek RTL8029AS]
        mac = 35:f4:c2

SLiRP port forwarding
^^^^^^^^^^^^^^^^^^^^^

Port forwarding allows the host system and other devices on its network to access TCP and UDP servers running on the emulated machine. This feature is configured through the ``[SLiRP Port Forwarding #x]`` section of the configuration file, where x is the number of the emulated network card, in the range of 1 to 4.

Each port forward must be assigned a number, starting at 0 and counting up (skipping a number will result in all subsequent port forwards being ignored), which replaces ``X`` on the following directives:

* ``X_protocol``: Port type: ``tcp`` or ``udp`` (default: ``tcp``)
* ``X_external``: Port number on the host (default: same port number as ``X_internal``)
* ``X_internal``: Port number on the emulated machine (default: same port number as ``X_external``)

The host system can access forwarded ports through 127.0.0.1 or its own IP address, while other devices on the network can access them through the host's IP address.

.. note:: The emulated machine's IP address must be set to 10.0.\ *x*\ .15 (the default IP provided through DHCP) for port forwarding to work.

.. container:: toggle-always-show

    .. container:: toggle-header

        Example: forward host TCP port 8080 to emulated machine port 80, and host UDP port 5555 to emulated machine port 5555

    .. code-block:: none

        [SLiRP Port Forwarding #1]
        0_external = 8080
        0_internal = 80
        1_protocol = udp
        1_external = 5555
