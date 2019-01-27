# mac_automation_scripts
* Install [BetterTouchTool](https://folivora.ai)
* Import the `Default.bttpreset` file into BTT

## FCPX video editing setup
### What does it do
When launched:
* Activate macro support for external keyboard *(will add macros and shortcuts to this repo as soon as I'm convinced with their usefulness)*
* Launch Final Cut Pro and set it to fullscreen
* Disable TrueTone on launch

 When Final Cut Pro is active a new button gets added to the Touchbar. It can toggle TrueTone

### Requirements
* [USB Overdrive](http://www.usboverdrive.com/USBOverdrive/News.html)

### Installation
* Remove USB Overdrive from login items
* Unzip the `Video Editing.zip` file and move its content to the Application folder

---
## Touchbar Yeelight brightness slider
### What does it do
Add a slider to the Touchbar. It controls the brightness of your Yeelight bulb
### Requirements
* [Python 3 & pip](https://www.python.org/downloads/)

### Installation
* Activate the LAN control for the lightbulb in the Yeelight app
* Install the yeelight module
```shell
pip install yeelight
```
* Insert the lightbulb IP address in the `yeelight_bulb.py` file
* Open BTT and aelect the Custom Applescript Slider Widget in the Touchbar section
* Open its Predefined Action
* Insert the path of the `yeelight_bulb.py` file into the Applescript 

## Other stuff
* tip-tap trackpad gestures added. Switch between tabs in Safari
* app switcher widget added to the Touchbar
