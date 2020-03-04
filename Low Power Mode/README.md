## Low Power Mode for MacOS
### What does it do
When launched:
* Activate a macro that turns off all power consuming settings of your macbook
  1. Set Integrated Display Brightness to 1
  2. Turn Do Not Disturb On
  3. Mute Volume 
  4. Set Integrated Keyboard Backlight Brightness to 0
  5. Turn Bluetooth Off
* If already in Low Power Mode revert back all the settings to the previous state

### Requirements
* [BetterTouchTool](https://a.paddle.com/v2/click/30842/40874?link=1061)
* [Python 3](https://www.python.org/downloads/)

### Installation
* Move `Low Power Mode.app` into the Application folder. You can edit this app using Automator
* Open BetterTouchTool
* Import the `LowPowerMode.bttpreset` file into BTT

You can modify the macro file located at `Low Power Mode.app/Contents/LowPowerMode.py` to change which setting it will toggle
