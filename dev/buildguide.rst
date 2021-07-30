Build guide
===========
In order to compile 86Box, please follow these steps:

1. Install the `MSYS2 <https://www.msys2.org/>`_ environment. The rest of the guide will refer to the directory that you install it to (`C:\\msys32` or `C:\\msys64` by default) as the MSYS2 root.

2. Launch your MSYS2 environment using the `MSYS2 MinGW 32-bit` shortcut. If you do not want to use the shortcut, launch it using the `mingw32.exe` executable in the MSYS2 root.

3. Once launched, you should update the environment:
    .. code-block:: bash

        $ pacman -Syu

   You may need to do this twice, just follow the on-screen instructions. Make sure you re-run the command periodically to keep the environment up-to-date.

4. Run the following command to install all of the dependencies: 
    .. code-block:: bash
   
        $ pacman -S gdb make git mingw-w64-i686-toolchain mingw-w64-i686-openal mingw-w64-i686-freetype mingw-w64-i686-SDL2 mingw-w64-i686-zlib mingw-w64-i686-libpng

5. Once the environment is fully updated and all dependencies are installed, change directory to ``src``:
    .. code-block:: bash
    
        $ cd path/to/86Box/src

6. Start the actual compilation process:
    .. code-block:: bash

        $ make -f win/Makefile.mingw
    
   By default, ``make`` does not run in parallel. If you want it to use more threads, use the ``-j`` switch with the number of threads, e.g. ``-j4``. However, keep in mind that you should not exceed your thread (logical processor) count, since that just uses more resources for little to no gain.

8. If the compilation succeeded (which it almost always should), you will find ``86Box.exe`` in the ``src`` directory.

9. In order to test your fresh build, replace the ``86Box.exe`` in your current 86Box environment with your freshly built one. If you do not have a pre-existing 86Box environment, download the latest successful build from https://ci.86box.net, and the latest ROM set from https://github.com/86Box/roms.

10. Enjoy using and testing the emulator! :)

If you encounter issues at any step or have additional questions, please join
the IRC channel or the appropriate channel on our Discord server and wait patiently for someone to help you.
