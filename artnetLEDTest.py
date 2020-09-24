from myArtNet import ArtNetNode
import board, neopixel


NUM_PIXELS = 10
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness = 0.5)

node = ArtNetNode("192.168.0.51", 6454) # TODO: sys. get IP

while True:
    artnetData = node.receive()
    for i in range(NUM_PIXELS):
        r = artnetData["ldata"][i*3]
        g = artnetData["ldata"][i*3+1]
        b = artnetData["ldata"][i*3+2]
        pixels[i] = (r,g,b)
