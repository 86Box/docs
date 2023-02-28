Port I/O
========

86Box handles the x86 port I/O space through **I/O handlers**. These handlers can be added with the ``io_sethandler`` function and removed with the ``io_removehandler`` function, both provided by ``86box/io.h``.

.. flat-table:: ``io_sethandler`` / ``io_removehandler``
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - ``base``
    - First I/O port (0x0000-0xffff) covered by this handler.

  * - ``size``
    - Amount of I/O ports (1-65536) covered by this handler, starting at ``base``.

  * - ``inb``
    - :rspan:`2` I/O read operation callback functions. Can be ``NULL``. Each callback takes the form of:

      ``TYPE callback(uint16_t addr, void *priv)``

      * ``TYPE``: operation width: ``uint8_t`` for ``inb``, ``uint16_t`` for ``inw``, ``uint32_t`` for ``inl``;
      * ``addr``: exact I/O port being read;
      * ``priv``: opaque pointer (see ``priv`` below);
      * Return value: 8- (``inb``), 16- (``inw``) or 32-bit (``inl``) value read from this port.

  * - ``inw``

  * - ``inl``

  * - ``outb``
    - :rspan:`2` I/O write operation callback functions. Can be ``NULL``. Each callback takes the form of:

      ``void callback(uint16_t addr, TYPE val, void *priv)``

      * ``addr``: exact I/O port being written;
      * ``TYPE``: operation width: ``uint8_t`` for ``outb``, ``uint16_t`` for ``outw``, ``uint32_t`` for ``outl``;
      * ``val``: 8- (``outb``), 16- (``outw``) or 32-bit (``outl``) value being written to this port;
      * ``priv``: opaque pointer (see ``priv`` below).

  * - ``outw``

  * - ``outl``

  * - ``priv``
    - Opaque pointer passed to this handler's read/write operation callbacks.
      Usually a pointer to a device's :ref:`state structure <dev/api/device:State structure>`.

I/O handlers can be added or removed at any time, although ``io_removehandler`` must be called with the **exact same** parameters that ``io_sethandler`` was originally called with. For non-Plug and Play devices, you might want to add handlers in the ``init`` callback; for ISA Plug and Play devices, you'd add and/or remove handlers on the ``config_changed`` callback; for PCI devices, you'd do the same whenever the Command register or Base Address (BAR) registers are written to; and so on.

.. note:: There is no need to call ``io_removehandler`` on the device's ``close`` callback, since a hard reset already removes all I/O handlers.

Callback fallbacks
------------------

When an I/O handler receives an operation with a width for which it has no callback, the operation will automatically **fall back** to a lower width for which there is a callback. For example, if an ``inl`` operation falls on a handler which has no ``inl`` callback, 86Box will break the operation down to ``inw`` or ``inb`` callbacks on successive port numbers, then combine their return values:

* ``inl`` callback present::

    uint32_t val = inl(port);

* ``inl`` callback not present, but ``inw`` callback present::

    uint32_t val = inw(port);
    val |= (inw(port + 2) << 16);

* ``inl`` and ``inw`` callbacks not present, but ``inb`` callback present::

    uint32_t val = inb(port);
    val |= (inb(port + 1) << 8);
    val |= (inb(port + 2) << 16);
    val |= (inb(port + 3) << 24);

* ``inl``, ``inw`` and ``inb`` callbacks not present::

    uint32_t val = 0xffffffff; /* don't care */

The same rule applies to write callbacks:

* ``outl`` callback present::

    uint32_t val = /* ... */;
    outl(port, val);

* ``outl`` callback not present, but ``outw`` callback present::

    uint32_t val = /* ... */;
    outw(port,     val & 0xffff);
    outw(port + 2, (val >> 16) & 0xffff);

* ``outl`` and ``outw`` callbacks not present, but ``outb`` callback present::

    uint32_t val = /* ... */;
    outb(port,     val & 0xff);
    outb(port + 1, (val >> 8) & 0xff);
    outb(port + 2, (val >> 16) & 0xff);
    outb(port + 3, (val >> 24) & 0xff);

* ``outl``, ``outw`` and ``outb`` callbacks not present:

  Don't care, no operation performed.

.. note:: Each broken-down operation triggers the I/O handlers for its respective port number, no matter which handlers are responsible for the starting port number. A handler will **never** receive callbacks for ports outside its ``base`` and ``size`` boundaries.

This feature's main use cases are devices which store registers that are 8-bit wide but may be accessed with 16- or 32-bit operations:

.. container:: toggle

    .. container:: toggle-header

        Code example: ``inb`` handler for reading 8-bit registers

    .. code-block::

        typedef struct {
            uint8_t regs[256];
        } foo_t;

        static uint8_t
        foo_io_inb(uint16_t addr, void *priv)
        {
            foo_t *dev = (foo_t *) priv;
            return dev->regs[addr & 0xff]; /* register index = I/O port's least significant byte */
        }

        /* No foo_io_inw, so a 16-bit read will read two 8-bit registers in succession.
           No foo_io_inl, so a 32-bit read will read four 8-bit registers in succession. */

Multiple I/O handlers
---------------------

Any given I/O port can have an **unlimited** amount of I/O handlers, such that:

* when a **read** operation occurs, all read callbacks will be called, and their return values will be logically **AND**\ ed together;
* when a **write** operation occurs, all write callbacks will be called with the same written value.

Read callbacks can effectively return "don't care" (without interfering with other handlers) by returning a value with all bits set: ``0xff`` for ``inb``, ``0xffff`` for ``inw`` or ``0xffffffff`` for ``inl``.

.. note:: The same callback fallback rules specified above also apply with multiple handlers. Handlers without callbacks for the operation's type and (same or lower) width are automatically skipped.

I/O traps
---------

A second type of I/O handler, **I/O traps** allow a device (usually System Management Mode on chipsets or legacy compatibility mechanisms on PCI sound cards) to act upon a read/write operation to an I/O port operation without affecting its result.

.. container:: toggle

    .. container:: toggle-header

        Code example: I/O trap on ports ``0x220``-``0x22f``

    .. code-block::

        typedef struct {
            void *trap_220;
        } foo_t;

        static void
        foo_trap_220(int size, uint16_t addr, uint8_t write, uint8_t val, void *priv)
        {
            /* Get the device state structure. */
            foo_t *dev = (foo_t *) priv;

            /* Do whatever you want. */
            pclog("Foo: Trapped I/O %s to port %04X, size %d\n",
                  write ? "write" : "read", addr, size);
            if (write)
              pclog("Foo: Written value: %02X\n", val);
        }

        static void *
        foo_init(const device_t *info)
        {
            /* Allocate the device state structure. */
            foo_t *dev = /* ... */

            /* Add I/O trap. */
            dev->trap_220 = io_trap_add(foo_trap_220, dev);

            /* Map I/O trap to 16 ports starting at 0x220. */
            io_trap_remap(dev->trap_220, 1, 0x220, 16);

            return dev;
        }

        static void
        foo_close(void *priv)
        {
            /* Get the device state structure. */
            foo_t *dev = (foo_t *) priv;

            /* Remove I/O trap before deallocating the device state structure. */
            io_trap_remove(dev->trap_220);
            free(dev);
        }

        const device_t foo4321_device = {
            /* ... */
            .init = foo_init,
            .close = foo_close,
            /* ... */
        };

.. flat-table:: ``io_trap_add``
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - ``func``
    - Function called whenever an I/O operation of any type or size is performed to the trap's I/O address range. Takes the form of:

      ``void func(int size, uint16_t addr, uint8_t write, uint8_t val, void *priv)``

      * ``size``: I/O operation width: ``1``, ``2`` or ``4``;
      * ``addr``: I/O address the operation is being performed on;
      * ``write``: ``0`` if this operation is a *read*, or ``1`` if it's a *write*;
      * ``val``: value being written if this operation is a write;
      * ``priv``: opaque pointer (see ``priv`` below).

  * - ``priv``
    - Opaque pointer passed to the ``func`` callback above.
      Usually a pointer to a device's :ref:`state structure <dev/api/device:State structure>`.

  * - **Return value**
    - Opaque (``void``) pointer representing the newly-created I/O trap.

.. flat-table:: ``io_trap_remap``
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - ``trap``
    - Opaque pointer representing the I/O trap to remap.

  * - ``enable``
    - * ``1`` to enable this trap;
      * ``0`` to disable it.

  * - ``addr``
    - First I/O port (0x0000-0xffff) covered by this trap.

  * - ``size``
    - Amount of I/O ports (1-65536) covered by this trap.
