from ola.ClientWrapper import ClientWrapper
from rpi_ws281x import PixelStrip, Color
import argparse
from time import sleep


print "set up"


UNIVERSE = 0
STARTCHAN = 1
NUMLED = 30
LED_PIN = 18

strip = PixelStrip(NUMLED, LED_PIN)
strip.begin()


def NewData(data):
    for i in range(NUMLED):
        red = data[i*3]
        green = data[i*3+1]
        blue = data[i*3+2]
        print(i, ":", red, green, blue)

        #pixels[i] = (red, green, blue)
	strip.setPixelColorRGB(i, red, green, blue)
    strip.show()


print "running"



wrapper = ClientWrapper()
client = wrapper.Client()
client.RegisterUniverse(UNIVERSE, client.REGISTER, NewData)
wrapper.Run()
