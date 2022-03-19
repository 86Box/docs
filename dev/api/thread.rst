.. include:: /include.rst

Threads
=======

Compute-intensive tasks can be offloaded from the main emulation flow with **threads**. Unless otherwise stated, all structures, functions and constants in this page are provided by ``86box/plat.h``.

.. warning:: 86Box API functions (excluding those in this page) are generally **not thread-safe** and must be called from the **main emulation thread**. Thread-unsafe actions (like raising an interrupt) can be performed by the callback of a free-running :doc:`timer <timer>` which looks for data written to the device's :ref:`state structure <dev/api/device:State structure>` by a thread, as timers run on the main emulation thread.

.. note:: The contents of ``thread_t`` and other structures used by ``thread_*`` functions are platform-specific; therefore, pointers to those structures should be treated as opaque pointers.

Starting
--------

Threads can be started with the ``thread_create`` function. Additionally, the ``thread_wait`` function can be used to wait for a thread's function to return.

.. flat-table:: thread_create
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - thread_func
    - Function to run in the thread. Takes the form of:

      ``void thread_func(void *priv)``

      * ``priv``: opaque pointer (see ``priv`` below).

  * - priv
    - Opaque pointer passed to the ``thread_func`` above.
      Usually a pointer to a device's :ref:`state structure <dev/api/device:State structure>`.

  * - **Return value**
    - ``thread_t`` pointer representing the newly-created thread.
      That pointer will become **invalid** once the thread's function returns.

.. flat-table:: thread_wait
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - arg
    - ``thread_t`` pointer representing the thread to wait for.

  * - **Return value**
    - * ``0`` on success;
      * Any other value on failure.

Events
------

**Events** allow for synchronization between threads. An event, represented by an ``event_t`` pointer returned by the ``thread_create_event`` function, can be *set* (``thread_set_event`` function) or *reset* (``thread_reset_event`` function), and a thread can wait for an event to be *set* with the ``thread_wait_event`` function. Events that are no longer to be used should be deallocated with the ``thread_destroy_event`` function.

.. flat-table:: thread_create_event
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - **Return value**
    - ``event_t`` pointer representing the newly-created event.

.. flat-table:: thread_set_event / thread_reset_event / thread_destroy_event
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - arg
    - ``event_t`` pointer representing the event to *set* (``thread_set_event``), *reset* (``thread_reset_event``) or deallocate (``thread_destroy_event``).

.. flat-table:: thread_wait_event
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - arg
    - ``event_t`` pointer representing the event to wait for.

  * - timeout
    - Maximum amount of time in **milliseconds** (not microseconds, unlike :doc:`timers <timer>`) to spend waiting for the event to be *set*. If set to ``-1``, this function will not return until the event is *set*.

  * - **Return value**
    - * ``0`` on success;
      * Any other value if ``timeout`` was reached or the wait otherwise failed.

.. note:: A ``thread_wait_event`` call does not *reset* the event once it is *set*; the event must be *reset* manually with ``thread_reset_event``. ``thread_wait_event`` returns immediately if the event is already *set*.

Mutexes
-------

`Mutexes <https://en.wikipedia.org/wiki/Mutual_exclusion>`_, also known as **locks**, can control access to a shared resource, ensuring no concurrent modifications or other issues arise from multiple threads attempting to use the same resource at the same time. A mutex, represented by a ``mutex_t`` pointer returned by the ``thread_create_mutex`` function, can be *locked* with the ``thread_wait_mutex`` function (which waits until the mutex is *released*) and *released* with the ``thread_release_mutex`` function. Additionally, the status of a mutex can be independently checked with the ``thread_test_mutex`` function. Mutexes that are no longer to be used should be deallocated with the ``thread_close_mutex`` function.

.. flat-table:: thread_create_mutex
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - **Return value**
    - ``mutex_t`` pointer representing the newly-created mutex.

.. flat-table:: thread_wait_mutex / thread_release_mutex / thread_close_mutex
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - arg
    - ``mutex_t`` pointer representing the mutex to *lock* (``thread_wait_mutex``), *release* (``thread_release_mutex``) or deallocate (``thread_close_mutex``).
      If the mutex is locked, ``thread_wait_mutex`` will not return until the mutex is *released* by another thread.

.. flat-table:: thread_test_mutex
  :header-rows: 1
  :widths: 1 999

  * - Parameter
    - Description

  * - arg
    - ``mutex_t`` pointer representing the mutex to check.

  * - **Return value**
    - * ``0`` if the mutex is *locked*;
      * Any other value if the mutex is *released*.
