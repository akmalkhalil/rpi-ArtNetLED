from myArtNet import ArtNetNode
import board, neopixel
import configparser

config = configparser.ConfigParser()
config.read("conf.ini")

NUM_PIXELS = config["artnetNode"]["numled"]
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness = 0.5)
# TODO: Add brightness to config

node = ArtNetNode("192.168.0.51", 6454) # TODO: sys. get IP
address = config["artnetNode"]["startaddr"]
incMacros = bool(config["artnetNode"]["macros"])

def runMacro(dmxVal):
    pass
    # TODO
    # K here's the plan
    # need to map dmxVal to a row in macroList.csv
    # for now I think 0-10: don't run macro
    # 10-50: run clear
    # 51-100: colourRun
    # 101-150: rainbow
    # 151-200: speedflash
    # 200-255: do nothing (future expansion)

while True:
    artnetData = node.receive()
    for i in range(address-1, address-1+NUM_PIXELS):
        r = artnetData["ldata"][i*3]
        g = artnetData["ldata"][i*3+1]
        b = artnetData["ldata"][i*3+2]
        pixels[i] = (r,g,b)
    if (incMacros):
        print(address+NUM_PIXELS, artnetData["ldata"][address+NUM_PIXELS])
        # Because the for loop iterates over pixels rather than over each address
        runMacro(artnetData["ldata"][address+NUM_PIXELS])
