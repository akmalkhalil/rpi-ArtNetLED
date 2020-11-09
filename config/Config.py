# Created so that I can set a variable whether I'm running tests or actually running a server





### Edit variables below ###
TESTING = False




### Do not edit past this point ###
if TESTING:
    settingsFile = "settingsTest.ini"
else:
    settingsFile = "settings.ini"