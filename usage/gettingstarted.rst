Getting started
===============

Here are the basic steps to help you get started with 86Box. The user interface has been designed to resemble Virtual PC, VirtualBox and other virtualizers, so if you used those programs before, this should all look familiar to you.

.. rubric:: Step 1: Get the ROM set

86Box relies on a set of ROM dumps gathered from physical hardware to emulate it. This includes the system BIOS, as well as any option ROMs used by expansion cards. If you try to start 86Box without one, you'll receive an error and 86Box will close. You need to download the ROM set from `here <https://github.com/86Box/roms/releases/latest>`_, and extract it into one of the :doc:`supported locations <roms>`.

.. rubric:: Step 2: Meet the main window

Once you got the romset in the right place, you can start ``86Box.exe``. The main window has three important areas:

* **The menu bar at the top**, where most controls and options are located. See :doc:`menubar` for more information.
* **The display area in the middle**, which is where the display output from the emulated machine will be rendered.
* **The status bar at the bottom**, containing icons for quickly accessing the configured peripheral devices. See :doc:`statusbar` for more information.

.. rubric:: Step 3: Configure the hardware

When you start an emulated machine, you probably want to configure it with the hardware options you want. This is much like putting together the hardware components to build a PC. To do this, go to the *Tools* menu and select *Settings*. This will bring up the *Settings* window, which has many options to choose from, split into :doc:`a handful of categories <../settings/index>`.

.. rubric:: Step 4: Configure the BIOS

Once you've selected the hardware components you wish to emulate, you need to make sure they're properly configured. This is done through the system BIOS, the same way it's done on a real computer. The specifics of this will of course differ from one machine to another, but generally speaking, you need to know how to enter the BIOS, which options to change, and which options to leave alone.

.. rubric:: Step 5: Mount some images

Now that you've configured everything, you're ready to run some software in your emulated machine. Maybe you want to install an operating system or play a booter game. In any case, you'll have to mount some virtual media to get going. You can do this with the icons in the :doc:`status bar <statusbar>`. Icons representing removable media appear semi-transparent when their associated drive is empty, and fully opaque when media is inserted.

When you want to eject virtual media, click on the particular icon again and select *Eject* (for floppy and ZIP disks) or *Empty* (for CD-ROMs). The icon becomes semi-transparent again.

.. rubric:: Step 6: Mouse and keyboard interaction

Now you're ready to do some stuff inside the emulated machine. Keyboard input is redirected there automatically whenever the emulator window has focus. All key presses and combinations will be redirected to the emulated machine.

Mouse input has to be manually "captured" and "released". To capture the mouse in the emulated mahine, simply click inside the renderer area. Your host mouse cursor will disappear and your mouse movement and clicks will be redirected into the emulated machine. Now you can use the mouse inside the emulated machine - if the software and hardware configuration supports it, of course.

To release the mouse, press :kbd:`F8 + F12` simultaneously (on Windows) or :kbd:`Ctrl + End` (on Linux). You can also use the middle mouse button for this if the emulated mouse only has two buttons.

.. rubric:: Step 7: What now?

If you made it this far, you got the basics of using 86Box, but there's more features and options to explore. For example, you can try out `86Box Manager <https://github.com/86Box/86BoxManager>`_ for easier management of multiple emulated machines. You can see what's under the *View* menu, or look at some of the more obscure options in the *Settings* window.

You may eventually encounter the need to get files *into* your machine. Please see :ref:`this section for information on disk image formats<hardware/diskimages:Disk images>` and :ref:`this section on creating and using disk images<hardware/diskimages:Creating and using disk images>`.

Keep in mind that because 86Box is constantly in development, various problems will come and go. If you think something's not working the way it should, consider `submitting an issue on GitHub <https://github.com/86Box/86Box/issues>`_ or joining official support channels on Discord or IRC.

Have fun!
