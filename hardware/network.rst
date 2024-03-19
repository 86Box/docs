Networking
==========

86Box supports different connection modes for the :doc:`emulated network cards <../settings/network>`. The specific details on these connection modes and network emulation as a whole are outlined on this page.

Null Driver
-----------

Default mode. The selected network card will be available to the emulated machine, but any packets sent through it will be dropped.

In this mode, the network card will default to a disconnected cable on startup; if the cable is connected through the :ref:`status bar <usage/statusbar:|network| Network>` or :ref:`Media menu <usage/menubar:Media>`, cards with link state detection support will report a connection, but packets will still be dropped.

SLiRP
-----

SLiRP creates a private network with a virtual router, allowing the emulated machine to reach the host, its network and the Internet; on the other hand, the host and other devices on its network cannot reach the emulated machine, unless :ref:`port forwarding <hardware/network:SLiRP port forwarding>` is configured. This is similar to the **NAT** mode on other emulators and virtualizers.

The virtual router provides automatic IP configuration to the emulated machine through DHCP. If that is not an option, use the following static IP settings, replacing *x* with 2, 3, 4 or 5 for the first, second, third or fourth network card to use SLiRP respectively:

* **IP address:** 10.0.\ *x*\ .15
* **Subnet mask:** 255.255.255.0
* **Default gateway:** 10.0.\ *x*\ .2
* **DNS server:** 10.0.\ *x*\ .3

The host can be reached through IP address 10.0.\ *x*\ .2, while other devices on the host's network can be reached through their normal IP addresses.

.. note:: SLiRP is only capable of routing TCP and UDP traffic, with limited ICMP ping support. Other protocols such as IPX and NetBEUI can only be used with :ref:`hardware/network:PCap` or :ref:`hardware/network:VDE` networking.

PCap
----

PCap connects directly to one of the host's network adapters. The emulated machine must be configured as if it were a real machine on your network. This is similar to the **Bridge** mode on other emulators and virtualizers.

On Windows hosts, this mode requires `Npcap <https://npcap.com/>`_ to be installed with **WinPcap API-compatible Mode enabled** (or use another WinPcap-compatible driver), or the correct permissions to be set for accessing ``pcap`` on Linux or ``bpf`` on macOS hosts. **Only wired Ethernet network connections** are compatible; Wi-Fi and other connections will not work at all, as they do not allow PCap to listen for packets bound to the emulated card's MAC address.

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

VDE
---

`Virtual Distributed Ethernet <https://github.com/virtualsquare/vde-2>`_ is a virtual Ethernet switch system for connecting different applications such as 86Box to each other. See `VDE Basic Networking <http://wiki.virtualsquare.org/#!tutorials/vdebasics.md>`_ for a brief overview.

.. note:: VDE is only available on **Linux** and **macOS** hosts.

One of VDE's core concepts is the *plug*. 86Box allows for *plug*\ ging an emulated machine into a virtual switch created by VDE; this virtual layer 2 switch is capable of carrying any Ethernet-based protocols such as IP and IPX.

Installing VDE tools
^^^^^^^^^^^^^^^^^^^^

The VDE tools are required to create the virtual switch that 86Box attaches to with a virtual cable.

Linux
"""""

On Debian, Ubuntu and derivatives, VDE and some of its associated commands are split into different packages. Install the libraries and their associated tools:

.. code-block:: shell

  apt install libvdeplug2 vde-switch vde2

.. note:: Other distributions should have similar package names.

macOS
"""""

VDE is available through Homebrew or MacPorts.

.. code-block:: shell

  brew install vde

.. code-block:: shell

  port install vde2

Creating the virtual switch
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before connecting 86Box, a virtual switch must be created with the ``vde_switch`` tool.

.. note:: ``vde_switch`` requires root privileges to *create* the switch. Applications will be able to connect to the switch with unprivileged (non-root) permissions.

.. code-block:: shell

  vde_switch --mode 666 --numports 8 --mgmt /tmp/vde.mgmt --mgmtmode 666 -s /tmp/vde.ctl

This command:

* Creates the *management* socket at ``/tmp/vde.mgmt``
* Creates the *control* socket at ``/tmp/vde.ctl``
* Sets the sockets' permissions to world read/write to allow unprivileged access
* Sets the number of switch ports to 8

Adding ``--daemon`` to the command will run ``vde_switch`` in the background.

Note the ``/tmp/vde.ctl`` path for the control socket, which is what should be provided in the :ref:`network settings <settings/network:VDE Socket>`.

.. note:: You can adjust the file paths or permissions as necessary. Refer to ``vde_switch -h`` for more information on available options.

Configuring 86Box for VDE
^^^^^^^^^^^^^^^^^^^^^^^^^

Go to the emulated machine's :doc:`network settings <../settings/network>` and select *VDE* as the mode for the emulated network card. Enter the *control* socket path, which is ``/tmp/vde.ctl`` for the example above, in the *VDE Socket* box.

Once these settings are saved, the machine should automatically connect to the VDE switch. Check the :ref:`status bar <usage/statusbar:|network| Network>` or :ref:`Media menu <usage/menubar:Media>` to make sure the emulated network cable is actually connected.

VDE switch status
^^^^^^^^^^^^^^^^^

The ``vdeterm`` command can be used to view the status of the virtual switch. It requires the path to the *management* socket (instead of the *control* socket) created alongside the switch; the command would be ``vdeterm /tmp/vde.mgmt`` for the example above.

Once in the command line, enter ``help`` to view a list of available commands. One helpful command is ``port/allprint`` which displays a list of all virtual switch ports and the processes attached to them:

.. code-block::

  vde[/tmp/vde.mgmt]: port/allprint

  Port 0001 untagged_vlan=0000 ACTIVE - Unnamed Allocatable
   Current User: myusername Access Control: (User: NONE - Group: NONE)
    -- endpoint ID 0003 module unix prog   : 86Box virtual card user=myusername PID=12345
  Success

In addition to ``vdeterm``, the command line interface can be accessed through ``vde_switch`` if it was started without the ``--daemon`` option, by pressing Enter on its terminal.

Other VDE features
^^^^^^^^^^^^^^^^^^

This guide only covers the basics of VDE. It provides many more useful features such as:

* Connecting virtual switches **across host machines** with ``vde_cryptcab``
* Bridging virtual switches with **network interfaces** to provide access to the Internet and other networks
* Connecting to **other emulators and virtualizers** with VDE support such as QEMU and VirtualBox
* Creating **VLANs and access control policies** which can be assigned to switch ports

Advanced networking features
----------------------------

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
