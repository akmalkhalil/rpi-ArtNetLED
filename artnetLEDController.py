# Note: I develop on Windows but this file needs to be ran on a pi, so some commits may not have this tested on a pi
from ArtNetNode import ArtNetNode, getIPAddressOfDevice
import board, neopixel
import configparser
from config.Config import settingsFileName


settingsIni = configparser.ConfigParser()
settingsIni.read(settingsFileName)

NUM_PIXELS = int(settingsIni["artnetNode"]["numled"])
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness = 0.5, auto_write=False)
# TODO: Add brightness to settings

node = ArtNetNode(getIPAddressOfDevice(), 6454) 
address = int(settingsIni["artnetNode"]["startaddr"]) # I think I should hide all this away in the Config class I created

# TODO: have a check to make sure that we're not going over one universe here. If we are, need some way to bump channels on to the next universer/have it overflow or whatever (this option can be set in the web interface if this is what we want)

running = True

def main():
    while running:
        artnetData = node.receive()
        if int(artnetData["physical"][0]) == 0: # TODO: need to generalise this and make it better
            # TODO: change this in to a parseForWS281X() function. So that we have something to test and can try coding in different pixel strings?
            # TODO: only run this for loop if there's been a change in the values of artnet
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
    main()
