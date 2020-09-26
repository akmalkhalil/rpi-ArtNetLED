# rpi-ArtNetLED
Using raspberry pi to receive ArtNet protocol to control LED strips
For current set up, flask web interface and LED controller are ran independantly/one does not need to be active for the other

## myArtNet.py
Contains a class description of an ArtNetNode object

## webUI.py
Flask based web interface to set config.ini options for ArtNet Raspberry Pi LED Controller.
Use this to set address/universe of pi and number of LEDs used. Also allows you to give the pi a name :).

## artnedLEDController.py
Uses ArtNetNode class to receive control information and controls pixels
Needs to be ran with sudo to control LEDs


## Big TODOs:
 - start up artnetLEDController from webUI
 - add option in web interface to include "macros" or not which are precoded effects
 - use doctest or some sort of automated testing before project starts to get too big



