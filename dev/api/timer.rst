.. include:: /include.rst

Timers
======

**Timers** allow for devices to perform tasks after a set period. This period is **automatically scaled** to match the emulation speed, which helps 86Box stay relatively accurate, unlike other emulators and virtualizers which may operate timers in real time independently of speed. Unless otherwise stated, all structures, functions and constants in this page are provided by ``86box/timer.h``.

.. note:: Timers are processed after each instruction in interpreter mode, or each recompiled code block in dynamic recompiler mode (unless an instruction requests a Time Stamp Counter (TSC) update). In both cases, timer accuracy **should** be in the single-digit microseconds at a minimum, which is good enough for most time-sensitive applications like 48 KHz audio playback.

Adding
------

Timers can be added with the ``timer_add`` function. The best place for adding a timer is in a :doc:`device <device>`'s ``init`` callback, storing the ``pc_timer_t`` object in the :ref:`state structure <dev/api/device:State structure>`::

    #include <86box/device.h>
    #include <86box/timer.h>

    typedef struct {
    	/* ... */
    	pc_timer_t countdown_timer;
    } foo_t;

    /* ... */

    /* Called once the timer period is reached. */
    static void
    foo_countdown_timer(void *priv)
    {
        foo_t *dev = (foo_t *) priv;

        /* Do whatever you want. */
    }

    /* ... */

    static void *
    foo_init(const device_t *info)
    {
        foo_t *dev = /* ... */

        /* Add timer. */
        timer_add(&dev->countdown_timer, foo_countdown_timer, foo, 0);

        /* ... */
    }

.. flat-table:: timer_add
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - timer
    - Pointer to a ``pc_timer_t`` object stored somewhere, usually in a device's :ref:`state structure <dev/api/device:State structure>`.

  * - callback
    - Function called every time the timer's period is reached. Takes the form of:

      ``void callback(void *priv)``

      * ``priv``: opaque pointer (see ``priv`` below).

  * - priv
    - Opaque pointer passed to the ``callback`` above.
      Usually a pointer to a device's :ref:`state structure <dev/api/device:State structure>`.

  * - start_timer
    - Part of the :ref:`legacy API <dev/api/timer:Legacy API>`, should always be ``0``.

Triggering
----------

The ``timer_on_auto`` function can be used to start (with the provided microsecond period) or stop a timer. It can also be called from a timer callback to restart the timer::

    #include <86box/timer.h>

    typedef struct {
        /* ... */
        uint8_t regs[256];
        pc_timer_t countdown_timer;
    } foo_t;

    /* ... */

    static void
    foo_countdown_timer(void *priv)
    {
        foo_t *dev = (foo_t *) priv;

        /* ... */

        /* Example: restart timer automatically if bit 1 (0x02) of register 0x80 is set. */
        if (dev->regs[0x80] & 0x02)
            timer_on_auto(&dev->countdown_timer, 100.0);
    }

    /* Example: writing to I/O port register 0x__80:
       - Bit 0 (0x01) set: start 100-microsecond countdown timer;
       - Bit 0 (0x01) clear: stop countdown timer. */
    static void
    foo_outb(uint16_t addr, uint8_t val, void *priv)
    {
        foo_t *dev = (foo_t *) priv;
        /* ... */

        if ((addr & 0xff) == 0x80) {
            dev->regs[0x80] = val;
            if (val & 0x01)
                timer_on_auto(&dev->countdown_timer, 100.0);
            else
                timer_on_auto(&dev->countdown_timer, 0.0);
        }

        /* ... */
    }

    /* ... */

.. flat-table:: timer_on_auto
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - timer
    - Pointer to the timer's ``pc_timer_t`` object.

  * - period
    - Period after which the timer callback is called, in microseconds (1/1,000,000th of a second or 1/1,000th of a millisecond) as a ``double``.
      A period of ``0.0`` stops the timer if it's active.

Legacy API
----------

Existing devices may use the ``timer_set_delay_u64`` and ``timer_advance_u64`` functions, which are considered legacy and will not be documented here for simplicity. These functions used an internal 64-bit period unit, which had to be obtained by multiplying the microsecond value by the ``TIMER_USEC`` constant, and updated by the device's ``speed_changed`` callback. The new ``timer_on_auto`` function is much simpler, requiring no constant multiplication or updates.
