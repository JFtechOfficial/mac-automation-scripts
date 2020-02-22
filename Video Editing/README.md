## FCPX video editing mode
### What does it do
When launched:
* Activate [Final Cut Pro macro support for external keyboard](https://github.com/JFtechOfficial/FCPX-macro-keyboard)
* Launch Final Cut Pro and set it to fullscreen

When FCPX is in use:
* ~~Disable TrueTone and Night Shift~~ now using [Shifty](https://shifty.natethompson.io/en/)
* Adds a button to the Touchbar. If pressed it quits Final Cut Pro and the macro support

### Requirements
* [USB Overdrive](http://www.usboverdrive.com/USBOverdrive/News.html)
* [CommandPost](http://commandpost.io)

### Installation
* Remove USB Overdrive and CommandPost from login items
* Unzip the `Video Editing.zip` file and move its content to the Application folder. You can edit this app using Automator.
* Unzip the `Quit Video Editing.zip` file and move its content to any folder of your choice. You can edit this workflow using Automator.
* Open BetterTouchTool
* Import the `FCPX.bttpreset` file into BTT
* Select Final Cut Pro in the Select Application sidebar
* Select Quit Video Editing in the Touchbar section
* Open its Predefined Action 
* Select the `Quit Video Editing` file
