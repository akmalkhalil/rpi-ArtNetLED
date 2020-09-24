import time, board, neopixel

NUM_PIXELS = 30

pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness = 0.2)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)
 
 
while True:
    for j in range(255):
#        for i in range(NUM_PIXELS//2):
        for i in range(NUM_PIXELS):
#            pixel_index = (i * 256 // (NUM_PIXELS//2)) + j
            pixel_index = (i*256  // NUM_PIXELS) + j
            pixels[i] = wheel(pixel_index & 255)
#            pixels[NUM_PIXELS-i-1] = wheel(pixel_index & 255)
        time.sleep(0.0001)




