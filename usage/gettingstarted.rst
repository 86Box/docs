Getting started
==========================

_Please note that this page is a work in progress._

Here are the basic steps to help you get started with 86Box. The user interface has been designed to resemble Virtual PC, VirtualBox, etc., so if you used those programs before, this should all look familiar to you.

### Step 1: Get the romset

86Box relies on a bunch of external binary files, called ROMs, to emulate various hardware. Together, these files are known as the romset. If you try to start 86Box without one, you'll recieve an error and 86Box will close. You need to download the romset from [here](https://github.com/86Box/roms/releases/latest), create a subfolder named `roms` in the folder where `86Box.exe` is located, and extract it there.

### Step 2: Meet the main window

Once you got the romset in the right place, you can start `86Box.exe`. The main window has three important areas:
* **The menu bar at the top**, where most commands and options are located
* **The display area in the middle**, which is where the output from the emulated machine will be rendered
* **The status bar at the bottom**, containing icons for quickly accessing the configured peripheral devices

The *Action* menu has basic commands for controlling the emulated machine. You can cycle the power (also known as a *hard reset*), send the *CTRL+ALT+DEL* and *CTRL+ALT+ESC* keystrokes, pause the virtual machine or close it.

The *View* menu is mostly filled with various options for advanced users, so we'll skip it for now. The *Tools* menu, on the other hand, is pretty important, as it allows you to access the settings for the virtual machine and take screenshots.
 
In the *About* menu, you can access the *About 86Box* window and see who helped make this emulator.

### Step 3: Configure the hardware

When you start a virtual machine, you probably want to configure it with the hardware options you want. This is much like putting together the hardware components to build a PC. To do this, go to the *Tools* menu and select *Settings*. This will bring up the settings window, which has a lot of options to chose from. So in order to not make this page too long, [click here](settings) to see an overview of the settings window and more in-depth descriptions of individual options.

### Step 4: Configure the BIOS

Once you've selected the hardware components you wish to emulate, you need to make sure they're properly configured. This is done through the system BIOS, same way it's done on a real computer. The specifics of this of course differs from one machine to another, but generally you need to know how to enter the BIOS, which options to change, and which options to leave alone. See [this page](biosconfig) for more information.

### Step 5: Mount some images

Now that you've configured everything, you're ready to run some software in your virtual machine. Maybe you want to install an operating system or play a booter game. In any case, you'll have to mount some virtual media to get going. You can do this with the icons in the status bar. Icons representing removable media appear semi-transparent when their associated drive is empty, and fully opaque when media is inserted.

Depending on the hardware configuration you've chosen, you may or may not see the following icons in the status bar, from left to right:
* **Floppy disk:** the icon is different for 3.5" and 5.25" floppy disk drives. This also determines the kind of floppy disk images you can use with a particular drive. You can have up to 4 floppy drives configured, though BIOS limitations also apply. 
To mount a floppy disk image, click on the floppy disk icon, select *Existing image...*, and select the disk image you wish to mount.
* **CD-ROM:** this represents the CD-ROM drive you've configured, you can have up to 4 drives. To mount a disk image, click on the icon and select *Image...*, then select the image you wish to mount.
* **ZIP disk:** represents the Iomega ZIP drive, also up to four drives. The mounting procedure is the same in this case as well, click on the icon, select *Existing image...* and select your ZIP disk image.
* **Hard disk drive:** currently, this icon is there only to let you know that a hard disk drive has been configured. If you hover over it, the tooltip will tell you which interface was selected for this particular drive. Theoretically you could have an unlimited number of hard disk drives, but interface and BIOS limitations prevent this.
* **Network:** there's always only one network icon at most, it is only present if you've enabled a network interface. It doesn't do anything yet other than let you know that networking capability has been enabled.
* **Sound:** this icon is always present and allows you to set the sound gain level when double-clicked.

Icons will also flash a small green dot every now and then. This means the particular piece of hardware associated with the icon is in use; for example, the data on the hard disk drive is being read or written.

When you want to eject virtual media, click on the particular icon again and select *Eject* (for floppy and ZIP disks) or *Empty* (for CD-ROMs). The icon becomes semi-transparent again.

### Step 6: Mouse and keyboard interaction

Now you're ready to do some stuff inside the emulated machine. Keyboard input is redirected there automatically whenever the emulator window has focus. All key presses and combinations will be redirected to the emulated machine.

Mouse input has to be manually "captured" and "released". To capture the mouse in the emulated mahine, simply click inside the renderer area. Your host mouse cursor will disappear and your mouse movement and clicks will be redirected into the emulated machine. Now you can use the mouse inside the emulated machine (if the software and hardware configuration supports it of course).

To release the mouse, press F8 and F12 simultaneously. You can also use the middle mouse button for this if the emulated mouse only has two buttons.

### Step 7: What now?

If you made it this far, you got the basics of using 86Box, but there's more features and options to explore. For example, you can try out [86Box Manager](https://github.com/86Box/86BoxManager) for easier management of multiple virtual machines. You can see what's under the [*View* menu](viewmenu) or look at some of the more obscure options in the settings.

Keep in mind that because 86Box is constantly in development, various problems will come and go. If you think something's not working the way it should, consider submitting an issue here on GitHub or joining official support channels on Discord or IRC.

Have fun!
