# Note: I develop on Windows but this file needs to be ran on a pi, so some commits may not have this tested on a pi
from ArtNetNode import ArtNetNode
import board, neopixel
import configparser
from config.Config import settingsFileName


settingsIni = configparser.ConfigParser()
settingsIni.read(settingsFileName)

NUM_PIXELS = int(settingsIni["artnetNode"]["numled"])
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness = 0.5, auto_write=False)
# TODO: Add brightness to settings

node = ArtNetNode("192.168.0.51", 6454) # TODO: sys. get IP
address = int(settingsIni["artnetNode"]["startaddr"])

running = True

def main():
    while running:
        artnetData = node.receive()
        # TODO: change this in to a parseForWS281X() function. So that we have something to test and can try coding in different pixel strings?
        # TODO: only run this for loop if there's been a change in the values of artnet
        # TODO: can I parallise this loop?
        for i in range(address-1, address-1+NUM_PIXELS):
            addr = i*3
            r = artnetData["ldata"][addr]
            g = artnetData["ldata"][addr+1]
            b = artnetData["ldata"][addr+2]
            pixels[i] = (r,g,b)
        pixels.show()
    return 0

def stopMain():
    global running
    running = False


if __name__ == "__main__":
    main(running)