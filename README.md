# rpi-ArtNetLED
Using raspberry pi to receive ArtNet protocol to control LED strips

This project is useable but still a WIP. Many things will change, it's full of things I'm just trying out for the first time/for fun.

Project works with WS281x LEDs

## Setup
First Clone repo on to the pi.

For current set up, flask web interface and LED controller are ran independantly/one does not need to be active for the other. Making settings changes while artnet node running will need the node restarted in order to take effect.

There's a not fully implemented/tested button on the web interface to start/stop the artnet LED controller, see below for more information.

DMX address and universe can be set in config/settings.ini or via the web interface. In the future, only the web interface will be recommended.

To access the web interface:

This command must be run before first time running web server:
```
export FLASK_APP=webUI.py
```
see https://flask.palletsprojects.com/en/1.1.x/quickstart/ for more.

To run the webserver:
```
python3 -m flask run --host 0.0.0.0
```

To begin receiving arnet and to control LEDs:
```
sudo python3 arnetLEDController.py
```
 - sudo is required for the neopixel library to control the LEDs

## Files
### ArtNetNode.py
Contains a class description of an ArtNetNode object

### webUI.py
Flask based web interface to set settings.ini options for ArtNet Raspberry Pi LED Controller.
Use this to set address/universe of pi and number of LEDs used. Also allows you to give the pi a name :).

### artnedLEDController.py
Uses ArtNetNode class to receive control information which are used to controls pixels
Needs to be ran with sudo to control LEDs

### tests.py
Automated unit testing using the unittest method. When running tests, config/Config.py needs to be updated to put the software in to "test mode"

I'm trying to write tests for features before implementing feature in order to try out Test Driven Design (TDD).

## Next big TODOs I want:
 - start up artnetLEDController from webUI
 - add option in web interface to include "macros" or not which are precoded effects
 - "register" IP addresses of other pis running this software so that they can all be configured from one web interface rather than logging in to each

### ALC start up from webUI
currently there's a button in the web UI that calls a JS function that sends a request to the web API. The button will currently only start a thread that counts to 30 and stops (or stops when the button is pressed again).

Commenting lines 7 and 8, and uncommenting 6 and 7 in webUI.py will allow the button to run artnetLEDController.
It seems to work but I want to test this further, to fix a bug with with the UI updating and to improve the feature leaving it implemented.
