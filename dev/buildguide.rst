Build guide
===========

86Box is built using `CMake <https://cmake.org/>`_ in combination with other build systems. The build actions are described in ``CMakeLists.txt`` files in most directories, which are the translated to the build system of choice by a CMake generator.

The following files are of particular interest:

* ``./CMakeLists.txt`` is the top level file, which defines the 86Box project and available configuration options;
* ``./src/CMakeLists.txt`` defines the main 86Box executable target

Toolchain files
---------------

Toolchain files are contained in the ``cmake`` directory. They define compiler flags and the 86Box-specific ``Release``, ``Debug`` and ``Optimized`` build types.

It is not required to use the included toolchain files, but it is highly recommended to make sure your build is compiled with the same configuration as used by the rest of the team and our userbase.

The currently included files are:

* ``flags-gcc.cmake`` contains the generic flags used by GCC-like compilers
  
  * ``flags-gcc-<arch>.cmake`` includes flags specific to builds for a given architecture

* ``llvm-win32-<arch>.cmake`` defines the build environment for use with LLVM/clang and vcpkg on Windows

Toolchain files are consumed during the initial project generation stage by passing their path in the ``CMAKE_TOOLCHAIN_FILE`` variable, e.g.:

.. code-block:: bash

    $ cmake … -D CMAKE_TOOLCHAIN_FILE=./cmake/flags-gcc-x86_64.cmake

.. note:: When using vcpkg, which uses its own toolchain file, the 86Box toolchain files must be chainloaded using the ``VCPKG_CHAINLOAD_TOOLCHAIN_FILE`` variable.

Presets
-------

The ``CMakePresets.json`` file contains several common compilation options for 86Box:

.. list-table::
    :header-rows: 1

    * - Build name
      - Debug
      - New dynarec
      - Dev. branch
      - Optimized
    * - ``regular`` 
      - ❌
      - ❌
      - ❌
      - ❌
    * - ``debug``
      - ✅
      - ❌
      - ❌
      - ❌
    * - ``experimental``
      - ✅
      - ✅
      - ✅
      - ❌
    * - ``optimized``
      - ❌
      - ❌
      - ❌
      - ✅

The presets are consumed during the initial project generation stage by using the ``--preset`` CMake command line option, e.g.:

.. code-block:: bash

    $ cmake … --preset regular

.. note:: Presets require CMake 3.21 or newer.

Obtaining the source code
-------------------------

There are multiple ways to obtain the 86Box source code in order to build it:

* Use the ``git`` command line. The utility needs to be installed and present in the search path.

  .. code-block:: bash

        $ git clone https://github.com/86Box/86Box.git

* Use GitHub Desktop, SourceTree, Git for Windows or other Git frontend on your host.

* Download a ZIP file from GitHub and extract it. (not recommended)

Prerequisites
-------------

The build process requires the following tools:

* CMake (>= 3.15)
* ``pkg-config``

Development files for the following libraries are also needed:

* FreeType
* libpng
* RtMidi
* SDL2
* FAudio (optional on Windows)
* Qt5 or Qt6 (optional, can be disabled)

Obtaining the dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^

MSYS2
"""""

.. code-block:: bash

    $ pacman -Syu $MINGW_PACKAGE_PREFIX-ninja $MINGW_PACKAGE_PREFIX-cmake $MINGW_PACKAGE_PREFIX-gcc $MINGW_PACKAGE_PREFIX-pkg-config $MINGW_PACKAGE_PREFIX-openal $MINGW_PACKAGE_PREFIX-freetype $MINGW_PACKAGE_PREFIX-SDL2 $MINGW_PACKAGE_PREFIX-zlib $MINGW_PACKAGE_PREFIX-libpng $MINGW_PACKAGE_PREFIX-rtmidi $MINGW_PACKAGE_PREFIX-qt5-static $MINGW_PACKAGE_PREFIX-qt5-translations

.. note:: The command installs the packages only for the currently used MinGW environment, therefore you will need to repeat the procedure for every target you plan to build for.

Ubuntu, Debian
""""""""""""""

.. code-block:: bash

    $ sudo apt install build-essential cmake extra-cmake-modules pkg-config ninja-build libfreetype-dev libsdl2-dev libpng-dev libopenal-dev librtmidi-dev libfaudio-dev qtbase5-dev qtbase5-private-dev qttools5-dev libevdev-dev libxkbcommon-dev libxkbcommon-x11-dev


Arch
""""

.. code-block:: bash
  
    $ sudo pacman -Sy base-devel cmake extra-cmake-modules pkg-config ninja libfreetype sdl2 libpng lib32-openal rtmidi faudio qt5-base qt5-xcb-private-headers qt5-tools libevdev libxkbcommon libxkbcommon-x11 vulkan-devel

.. note:: Make sure to enable the multilib repository in your ``pacman.conf`` file.


macOS (Homebrew)
""""""""""""""""

.. code-block:: bash

    $ brew install cmake ninja pkg-config freetype sdl2 libpng openal-soft rtmidi faudio qt@5

Building
--------

Building 86Box can generally be condensed to the following steps:

1. Generate the project. This generally involves invoking the following base command line with additional options according to the development environment:

   .. code-block:: bash

        $ cmake -B <build directory> -S <source directory>


   Build directory is where the resulting binaries and other build artifacts will be stored. Source directory is the location of the 86Box source code.

   Toolchain files and presets are specified at this point by using the respective options.

   Other options can be specified using the ``-D`` option, e.g. ``-D NEW_DYNAREC=ON`` enables the new dynamic recompiler. See ``CMakeLists.txt`` in the root of the repository for the full list of available options.

2. Build the project itself. This can be done by changing to the chosen build directory and invoking the chosen build system, or you can use the following universal CMake command:

   .. code-block:: bash

        $ cmake --build <build directory>

   Appending the ``-jN`` option (where ``N`` is a number of threads you want to use for the compilation process) will run the build on multiple threads, speeding up the process some.

   .. note:: If you make changes to the CMake build files, running the command will automatically regenerate the project. There is no need to repeat step 1 or to delete the build directory.

3. If everything succeeds, you should find the resulting executable in the build directory. Depending on the build system, it might be located in some of its subdirectories.

.. tip:: The executable can be copied to a consistent location by running the following command:

   .. code-block:: bash

        $ cmake --install <build directory> --prefix <destination>

   The emulator file should then be copied into a ``bin`` directory in the specified location.

   Appending the ``--strip`` parameter will also strip debug symbols from the executable in the process.
