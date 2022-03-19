.. include:: /include.rst

Port I/O
========

86Box handles the x86 port I/O space through **I/O handlers**. These handlers can be added with the ``io_sethandler`` function and removed with the ``io_removehandler`` function, both provided by ``86box/io.h``.

.. flat-table:: io_sethandler / io_removehandler
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - base
    - The first I/O port (0x0000-0xFFFF) to be covered by this handler.

  * - size
    - The amount of I/O ports (1-65536) starting at ``base`` to be covered by this handler.

  * - inb
    - :rspan:`2` I/O read operation callback functions. Can be ``NULL``. Each callback takes the form of:

      ``TYPE callback(uint16_t addr, void *priv)``

      * ``TYPE``: operation width (``uint8_t`` for ``inb``, ``uint16_t`` for ``inw`` or ``uint32_t`` for ``inl``);
      * ``addr``: exact I/O port being read;
      * ``priv``: opaque pointer (see ``priv`` below);
      * Return value: value read from this port.

  * - inw

  * - inl

  * - outb
    - :rspan:`2` I/O write operation callback functions. Can be ``NULL``. Each callback takes the form of:

      ``void callback(uint16_t addr, TYPE val, void *priv)``

      * ``TYPE``: operation width (``uint8_t`` for ``outb``, ``uint16_t`` for ``outw`` or ``uint32_t`` for ``outl``);
      * ``addr``: exact I/O port being written;
      * ``val``: value being written to this port;
      * ``priv``: opaque pointer (see ``priv`` below).

  * - outw

  * - outl

  * - priv
    - Opaque pointer, passed to this handler's read/write operation callbacks.
      Usually a pointer to the device's :ref:`state structure <dev/api/device:State structure>`.

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

This feature's main use cases are devices which store registers that are 8-bit wide but may be accessed with 16- or 32-bit operations::

    typedef struct {
        uint8_t regs[256];
    } foo_t;

    uint8_t
    foo_inb(uint16_t addr, void *priv)
    {
        foo_t *dev = (foo_t *) priv;
        return dev->regs[addr & 0xff]; /* example: register index = I/O port's least significant byte */
    }

    /* No foo_inw, so a 16-bit read will read two 8-bit registers in succession.
       No foo_inl, so a 32-bit read will read four 8-bit registers in succession. */

Multiple I/O handlers
---------------------

Any given I/O port can have an **unlimited** amount of I/O handlers, such that:

* when a **read** operation occurs, all read callbacks will be called, and their return values will be logically **AND**\ ed together;
* when a **write** operation occurs, all write callbacks will be called with the same written value.

Read callbacks can effectively return "don't care" (without interfering with other handlers) by returning a value with all bits set: ``0xff`` with ``inb``, ``0xffff`` with ``inw`` or ``0xffffffff`` with ``inl``.

.. note:: The same callback fallback rules specified above also apply with multiple handlers. Handlers without valid callbacks for the operation's type and width are automatically skipped.
