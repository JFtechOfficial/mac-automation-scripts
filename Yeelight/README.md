## Yeelight brightness Touchbar slider
### What does it do
Add a slider to the TouchBar. It controls the brightness of your Yeelight bulb

### Requirements
* [BetterTouchTool](https://a.paddle.com/v2/click/30842/40874?link=1061)
* [Python & pip](https://www.python.org/downloads/)

### Installation
* Activate the LAN control for the lightbulb in the Yeelight app
* Open the Terminal app and install the yeelight module
```shell
pip install yeelight
```
* Insert the lightbulb IP address in the `yeelight_bulb.py` file
* Open BetterTouchTool
* Import the `Yeelight.bttpreset` file into BTT
* Select Custom Applescript Slider Widget in the Touchbar section
* Open its Predefined Action
* Insert the path of the `yeelight_bulb.py` file into the Applescript 
