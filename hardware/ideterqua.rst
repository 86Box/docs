Tertiary and quaternary IDE
===========================

The additional tertiary and quaternary IDE controllers, enabled through the :ref:`Storage controllers <settings/storage:Hard disk>` settings page, are not supported by all emulated BIOSes and may require manual configuration of the emulated operating system. The specific details are outlined on this page.

System resources
----------------

The following resources are used by these additional controllers:

+----------+-------------+---------------+---+
|Channel   |Main I/O port|Status I/O port|IRQ|
+==========+=============+===============+===+
|Tertiary  |01E8h        |03EEh          |11 |
+----------+-------------+---------------+---+
|Quaternary|0168h        |036Eh          |10 |
+----------+-------------+---------------+---+

.. note:: The tertiary and quaternary I/O ports and IRQs were incorrectly switched in 86Box versions prior to 4.0.1.

Each controller's IRQ can be configured through its respective *Configure* button on the :ref:`hard disk controller selector <settings/storage:Hard disk>`. The *Plug and Play* option on the *IRQ* box enables Plug and Play functionality, allowing a PnP compliant operating system to automatically set the controller's IRQ, while all other options set a static IRQ with no Plug and Play.

.. note:: * When using a non-Plug and Play IDE controller on an emulated machine which supports Plug and Play, remember to mark the IRQ as being used by a legacy ISA device in the BIOS setup utility.
          * Many operating systems do not allow non-Plug and Play IDE controllers to use IRQs outside of the default ones listed on the table above.

BIOS support
------------

The tertiary and quaternary controllers are not visible and not bootable by the BIOS on most machines currently emulated by 86Box, no matter whether or not they are Plug and Play.

Machines with **MR BIOS version 3** are the rare exception to this rule, since that BIOS provides full support for non-Plug and Play controllers (as long as the :ref:`default IRQs for each controller <hardware/ideterqua:System resources>` are used), including bootability and INT 13h services.

Operating system support
------------------------

DOS and real mode
^^^^^^^^^^^^^^^^^

**DOS and other real mode operating systems** rely on INT 13h services provided by the BIOS to access hard disks. These are only provided for the tertiary and quaternary channels by **MR BIOS version 3**, as mentioned above.

Windows 95, 98 and Me
^^^^^^^^^^^^^^^^^^^^^

The **Windows 9x family** will automatically detect Plug and Play IDE controllers on boot. Non-Plug and Play controllers will be detected during installation :ref:`only if the BIOS supports them <hardware/ideterqua:BIOS support>`. Follow these steps to enable a non-Plug and Play controller on an already-installed system:

1. Go to the *Add New Hardware* control panel.
2. Add a *Standard IDE/ESDI Hard Disk Controller* from the *Hard disk controllers* category.
3. Don't restart the system when asked to.
4. Go to the *Device Manager* tab of the *System* control panel.
5. Select the newly-added *Standard IDE/ESDI Hard Disk Controller* device from the *Hard disk controllers* category and click *Properties*.
6. Go to the *Resources* tab.
7. Select *Basic configuration 4* in the *Settings based on* box.
8. Change the resource settings to match the I/O ports on the :ref:`table above <hardware/ideterqua:System resources>` and the configured IRQ. The first *Input/Output Range* range corresponds to the **main** I/O port, the second one corresponds to the **status** I/O port, and *Interrupt Request* corresponds to the IRQ.

   * The status I/O port range is off by 6. Select 03E8 for the tertiary channel or 0368 for the quaternary channel.
   * The screenshot below shows an example configuration for the tertiary channel.

9. If both the tertiary and quaternary channels are enabled, repeat the steps above to enable the other controller.

.. image:: images/ideterqua_win98.png
   :align: center

Windows NT, 2000 and XP
^^^^^^^^^^^^^^^^^^^^^^^

**Windows 2000 and XP** will automatically detect Plug and Play IDE controllers on boot. Additionally, **Windows NT 3.5, 4.0, 2000 and XP** will automatically detect non-Plug and Play controllers during installation, regardless of BIOS support; however, this auto-detection of non-PnP controllers does not work on most machines with **Award BIOS**.

.. note:: If you install the system to a hard disk on one of the additional controllers, it will not be bootable unless :ref:`the BIOS supports booting from these controllers <hardware/ideterqua:BIOS support>`.

On **Windows 2000 only**, non-Plug and Play controllers can be enabled on an already-installed system through *Add New Hardware* similarly to :ref:`Windows 9x as shown above <hardware/ideterqua:Windows 95, 98 and Me>`. The resource parameters cannot be changed, and therefore, only the :ref:`default IRQs for each controller <hardware/ideterqua:System resources>` are supported. *Basic configuration 0002* corresponds to the **tertiary** channel, while *Basic configuration 0003* corresponds to the **quaternary** channel.

Windows Vista and 7
^^^^^^^^^^^^^^^^^^^

The **Windows NT 6 family** does not support legacy (ISA or VLB) IDE controllers, and therefore cannot use the additional channels as currently emulated by 86Box.

Linux
^^^^^

There are different steps for enabling additional IDE controllers on Linux, depending on which IDE driver stack is used by your distribution's kernel.

Modules can be loaded at any time with the ``modprobe`` command, or loaded on boot by adding the module's name (and parameters if required) to a file in ``/etc/modules-load.d`` on newer systemd-based distributions, or the ``/etc/modules`` file on older distributions.

* **Legacy IDE** (typically kernels **older than 2.6.19**):

   * Load the ``ide-pnp`` module to enable Plug and Play controllers.
   * Non-Plug and Play controllers require editing the kernel command line on your bootloader to add each controller's I/O ports and IRQ:

      * **Tertiary:** ``ide2=0x1e8,0x3ee,11`` (assuming IRQ 11)
      * **Quaternary:** ``ide3=0x168,0x36e,10`` (assuming IRQ 10)

* **libATA** (typically kernels **2.6.19 and above**):

   * Load the ``pata_isapnp`` module to enable Plug and Play controllers.
   * Load the ``pata_legacy`` module with the ``probe_all=1`` parameter to automatically detect and enable non-Plug and Play controllers. Only the :ref:`default IRQs for each controller <hardware/ideterqua:System resources>` are supported.

.. note:: Some distributions may automatically detect additional IDE controllers; however, that is very rarely the case.
