import board, neopixel, time

NUM_PIXELS = 30

pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness = 0.2)

while True:
  for j in range(10):
    for i in range(NUM_PIXELS):
      pixels[i] = (255,0,0)
      time.sleep(0.01)
    for i in range(NUM_PIXELS):
      pixels[i] = (0,255,0)
      time.sleep(0.01)
    for i in range(NUM_PIXELS):
      pixels[i] = (0,0,255)
      time.sleep(0.01)

  for i in range(NUM_PIXELS):
    pixels[i] = (0,0,0)
    time.sleep(0.01)

  for j in range(10):
    for i in range(NUM_PIXELS):
      pixels[i] = (255,0,0)
      pixels[(i-1)%30] = (0,0,0)
      time.sleep(0.01)
    for i  in range(NUM_PIXELS):
      pixels[i] = (0,255,0)
      pixels[(i-1)%30] = (0,0,0)
      time.sleep(0.01)
    for i in range(NUM_PIXELS):
      pixels[i] = (0,0,255)
      pixels[(i-1)%30] = (0,0,0)
      time.sleep(0.01)

  for j in range(5):
    for i in range(NUM_PIXELS):
      pixels[i] = (255,0,0)
      pixels[(i-1)%30] = (200,0,0)
      pixels[(i-2)%30] = (150, 50, 0)
      pixels[(i-3)%30] = (100,60,0)
      pixels[(i-4)%30] = (50,40,0)
      pixels[(i-5)%30] = (0,0,0)
      time.sleep(0.01)
