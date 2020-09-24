# rpi-ArtNetLED
Using raspberry pi to receive ArtNet protocol to control LED strips

## myArtNet.py

## Big TODOs:
 - create flask server to set number LEDs and DMX address of first pixel in web interface
    - have an options.py or options.txt file which has these options set in them
 - add option in web interface to include "macros" or not which are precoded effects
 - use doctest or some sort of automated testing 


## Old
Originally I tried using OLA but found that it was python2 based and the code contained a lot of C++ as well
Realised artnet receiving's not that hard to implement so I went and did it myself giving me more control and a smaller code base

https://github.com/OpenLightingProject/ola

I've tried following this https://www.openlighting.org/ola/tutorials/ola-led-pixels/
it uses ws2801 LEDs whereas I have ws2812.

python2 ws2812x library
https://github.com/rpi-ws281x/rpi-ws281x-python/

