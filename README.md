# rpi-ArtNetLED
Using raspberry pi to receive ArtNet protocol to control LED strips

Using https://github.com/OpenLightingProject/ola

I've tried following this https://www.openlighting.org/ola/tutorials/ola-led-pixels/
it uses ws2801 LEDs whereas I have ws2812.

python2 ws2812x library
https://github.com/rpi-ws281x/rpi-ws281x-python/



Potential change:
remove OLA, [implement own artnet receiving](https://en.wikipedia.org/wiki/Art-Net#Packet_format), create Flask web interface to set address/SSH keys
Also if I did this I wouldn't need to be using python2 any more
