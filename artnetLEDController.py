# Note: I develop on Windows but this file needs to be ran on a pi, so some commits may not have this tested on a pi
from ArtNetNode import ArtNetNode
import board, neopixel
import configparser
from config.Config import settingsFileName


settingsIni = configparser.ConfigParser()
settingsIni.read(settingsFileName)

NUM_PIXELS = int(settingsIni["artnetNode"]["numled"])
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness = 0.5)
# TODO: Add brightness to settings

node = ArtNetNode("192.168.0.51", 6454) # TODO: sys. get IP
address = int(settingsIni["artnetNode"]["startaddr"])

running = True

def main():
    while running:
        artnetData = node.receive()
        # TODO: change this in to a parseForWS281X() function. So that we have something to test and can try coding in different pixel strings?
        for i in range(address-1, address-1+NUM_PIXELS):
            r = artnetData["ldata"][i*3]
            g = artnetData["ldata"][i*3+1]
            b = artnetData["ldata"][i*3+2]
            pixels[i] = (r,g,b)
    return 0

def stopMain():
    global running
    running = False


if __name__ == "__main__":
    main(running)