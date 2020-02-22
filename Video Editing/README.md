## 'Set as Project Folder' in contextual menu
### What does it do
When launched:
* Copy the content of a template folder into a selected folder
* Rename some of the content to the name of the selected folder
* Move the folder to external volume if mounted

### Requirements
* [FiScript](https://github.com/Mortennn/FiScript)

### Installation
* Create a new Action in FiScript
* Open the `New-Project-Folder-FiScript.sh` file with TextEdit
* Insert the template folder path and the external storage path
* Copy/Paste its content into the `Script` textbox
* Enable only the `Use on directories` and `Get notification when execution has finished` toggle 
* Add icon, name and description if you want

You can modify the script to do whatever you want pretty much. Do NOT modify the script using FiScript, please use any other text editor and then copy/paste ([here is why](https://github.com/Mortennn/FiScript/issues/15)). The script was tested in **bash**. Note that it would not run outside FiScirpt, since it uses the `$PATH` variable provided by FiScript (change that to allow terminal execution). If you modify the template, you may also need to modify the script. 

---

## FCPX Video Editing mode
### What does it do
When launched:
* Activate [Final Cut Pro macro support for external keyboard](https://github.com/JFtechOfficial/FCPX-macro-keyboard)
* Launch Final Cut Pro and set it to fullscreen

When FCPX is in use:
* ~~Disable TrueTone and Night Shift~~ now using [Shifty](https://shifty.natethompson.io/en/)
* Adds a button to the TouchBar. If pressed it quits Final Cut Pro and the macro support

### Requirements
* [BetterTouchTool](https://a.paddle.com/v2/click/30842/40874?link=1061)
* [USB Overdrive](http://www.usboverdrive.com/USBOverdrive/News.html)
* [CommandPost](http://commandpost.io)

### Installation
* Remove USB Overdrive and CommandPost from login items
* Unzip the `Video Editing.zip` file and move its content to the Application folder. You can edit this app using Automator
* Unzip the `Quit Video Editing.zip` file and move its content to any folder of your choice. You can edit this workflow using Automator
* Open BetterTouchTool
* Import the `FCPX.bttpreset` file into BTT
* Select Final Cut Pro in the Select Application sidebar
* Select Quit Video Editing in the Touchbar section
* Open its Predefined Action 
* Select the `Quit Video Editing` file

---

## Start FCPX Video Editing mode when drive is connected

### What does it do
* Open a Dialog box when your editing drive is connected. Clicking on `Continue` will launch FCPX Video Editing mode

### Requirements
* [FCPX Video Editing mode](#FCPX-Video-Editing-mode)
* [Keyboard Maestro](https://www.keyboardmaestro.com/main/)

### Installation
* Import the `Editing Drive Alert.kmmacros` into Keyboard Maestro
* Modify the macro to match your external dirve exact name

---

## 'Start FCPX Video Editing mode' in contextual menu

### What does it do
* launch FCPX Video Editing mode from any Final Cut Pro X library file

### Requirements
* [FCPX Video Editing mode](#FCPX-Video-Editing-mode)
* [FiScript](https://github.com/Mortennn/FiScript)

### Installation
* Create a new Action in FiScript
* Open the `Start-Video-Editing-FiScript.sh` file with TextEdit
* Copy/Paste its content into the `Script` textbox
* Set `Accepted file types` to `.fcpbundle`
* Enable only the `Use on files` and `Use on directories` toggle 
* Add icon, name and description if you want

You can modify the script to do whatever you want pretty much. Do NOT modify the script using FiScript, please use any other text editor and then copy/paste ([here is why](https://github.com/Mortennn/FiScript/issues/15)). The script was tested in **bash**. Note that [FiScript doesn't work in external drives](https://github.com/Mortennn/FiScript/issues/18), so this functionality is not 100% compatible with [Start FCPX Video Editing mode when editing drive is connected](#start-fcpx-video-editing-mode-when-drive-is-connected)
