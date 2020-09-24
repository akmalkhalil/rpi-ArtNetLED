from ola.ClientWrapper import ClientWrapper
#from gpiozero import PWMLED, LED
import board, neopixel
from time import sleep

UNIVERSE = 0
STARTCHAN = 1
NUMLED = 5

#TODO: test that will fit in universe or error

pixels = neopixel.NeoPixel(board.D18, NUMLED)


def NewData(data):
    for i in range(NUMLED):
        red = data[i*3]
        green = data[i*3+1]
        blue = data[i*3+2]
        print(i, ":", red, green, blue)

        pixels[i] = (red, green, blue)



wrapper = ClientWrapper()
client = wrapper.Client()
client.RegisterUniverse(universe, client.Register, NewData)
wrapper.Run()
