from myArtNet import ArtNetNode
import board, neopixel
import configparser

confFileName = "config/conf.ini"
config = configparser.ConfigParser()
config.read(confFileName)

NUM_PIXELS = int(config["artnetNode"]["numled"])
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness = 0.5)
# TODO: Add brightness to config

node = ArtNetNode("192.168.0.51", 6454) # TODO: sys. get IP
address = int(config["artnetNode"]["startaddr"])

if __name__ == "__main__":
    while True:
        artnetData = node.receive()
        for i in range(address-1, address-1+NUM_PIXELS):
            r = artnetData["ldata"][i*3]
            g = artnetData["ldata"][i*3+1]
            b = artnetData["ldata"][i*3+2]
            pixels[i] = (r,g,b)
