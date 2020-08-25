import board, neopixel, time

NUM_PIXELS = 30

pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness = 0.2)

while True:
  for i in range(NUM_PIXELS):
    pixels[i] = (255,0,0)
  for i in range(NUM_PIXELS):
    pixels[i] = (0,255,0)
  for i in range(NUM_PIXELS):
    pixels[i] = (0,0,255)

