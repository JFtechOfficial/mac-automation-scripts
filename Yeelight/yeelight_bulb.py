from yeelight import Bulb
import sys

bulb = Bulb("192.168.1.24", auto_on=True)
brightness = int(float(sys.argv[1].replace(',', '.')) * 100)
if brightness < 1:
    bulb.turn_off()
else:
    bulb.set_brightness(brightness)
