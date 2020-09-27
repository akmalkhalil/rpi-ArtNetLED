# rpi-ArtNetLED
Using raspberry pi to receive ArtNet protocol to control LED strips

This project is useable but still a WIP. Many things will change, it's full of things I'm just trying out for the first time/for fun.

Project works with WS2801x LEDs

## Setup
First Clone repo on to pi.

For current set up, flask web interface and LED controller are ran independantly/one does not need to be active for the other. Making config changes while artnet node running will need node restarted in order to take effect.

DMX address and universe can be set in config.ini or via the web interface. In the future, only the web interface will be recommended.

To access the web interface.

This command must be run before first time running web server:
```
export FLASK_APP=webUI.py
```

To run webserver:
```
python3 -m flask run --host 0.0.0.0
```

To begin receiving arnet and control LEDs:
```
sudo python3 arnetLEDController.py
```

 - sudo is required for the neopixel library to control the LEDs

## Files
### myArtNet.py
Contains a class description of an ArtNetNode object

### webUI.py
Flask based web interface to set config.ini options for ArtNet Raspberry Pi LED Controller.
Use this to set address/universe of pi and number of LEDs used. Also allows you to give the pi a name :).

### artnedLEDController.py
Uses ArtNetNode class to receive control information and controls pixels
Needs to be ran with sudo to control LEDs

### tests.py
Automated unit testing using the unittest method. Some methods/functions (in the other files) may contain small doctest strings, this will be for documentation as apposed to testing.
Simply run the file to run tests.

Is currently pretty bare because I wanted to make sure I had the idea of testing set up early in this project.

## Next big TODOs I want:
 - start up artnetLEDController from webUI
 - add option in web interface to include "macros" or not which are precoded effects



