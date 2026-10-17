Automation socket
=================

The automation socket lets an external program, such as a test harness, a script or an AI agent, control an emulated machine. It can:

* hold the machine and advance it by an exact amount of emulated time;
* inject keyboard and mouse input;
* read the screen, memory and CPU registers;
* change floppy and CD images, reset the machine, record frames, and quit.

Since time doesn't pass while the machine is held, a client can take as long as it needs between moves, and runs driven the same way are repeatable.

The socket was added in `86Box/86Box#8365 <https://github.com/86Box/86Box/pull/8365>`_. It isn't included in official builds: build 86Box yourself with it enabled, then request it when starting 86Box.

Building
--------

Enable it with the ``AUTOMATION`` CMake option, which is off by default (see :doc:`buildguide`):

.. code-block:: bash

   $ cmake … -D AUTOMATION=ON

Without it, none of the automation code is compiled in.

Command line options
--------------------

.. flat-table::
  :header-rows: 1
  :widths: 38 62

  * - Option
    - Description

  * - ``--automation endpoint``
    - Listen for automation commands on ``endpoint``. ``unix:path`` is a domain socket, created so that only the owner can connect. ``tcp:port`` or ``tcp:host:port`` is TCP, on ``127.0.0.1`` unless a host is given. A bare value is a socket path on Unix-compatible operating systems, and a TCP port on Windows.

  * - ``--automation-hold``
    - Start with the machine held, so no emulated time passes until a client asks for it.

  * - ``--automation-token-file path``
    - TCP only: where to write the access token. The default is ``automation.token`` in the machine's folder.

  * - ``--automation-allow-remote``
    - TCP only: allow listening on an address other than loopback.

Over TCP, every connection must first send the per-run random token from the token file. 86Box refuses addresses other than loopback unless ``--automation-allow-remote`` is given. The protocol isn't encrypted, and a client with access controls the machine completely, including its memory. Prefer the domain socket where it's available.

Protocol
--------

Each request is one line of text, and each reply is one line of JSON. The commands are described in `doc/specifications/automation.md <https://github.com/86Box/86Box/blob/master/doc/specifications/automation.md>`_ in the 86Box source.
