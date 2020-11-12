from flask import Flask, request, render_template, redirect, url_for
import configparser
from config.Config import settingsFileName
from threading import Thread
#from artnetLEDController import main as ALCMain
#from artnetLEDController import stopMain as ALCStop
from threadTester import main as ALCMain
from threadTester import stop as ALCStop


# TODO: can I put this stuff in to if __name__ == "__main__ "?
app = Flask(__name__)


settingsIni = configparser.ConfigParser()
foo = settingsIni.read(settingsFileName)

ALCRunning = False
ALCThread = Thread(target = ALCMain)


# Can be run to create a valid settings file with default values already set up
def initSettings(fileName = "settings.ini.example"):
    pass

def updateSettings(form):
    # TODO: form validation? seperate function for validation I think???
    settingsIni["artnetNode"]["name"] = form["inputName"]
    settingsIni["artnetNode"]["startaddr"] = form["address"]
    settingsIni["artnetNode"]["dmxuniverse"] = form["universe"]
    #settingsIni["artnetNode"]["type"] = form["type"]
    settingsIni["artnetNode"]["numled"] = form["num"]
    with open(settingsFileName, 'w') as setFile:
        settingsIni.write(setFile)

def validateSettings(form):
    errors = []

    try:
        addr = int(form["address"])
    except ValueError:
        errors.append("Address must be a number")
        return errors
    try:
        univ = int(form["universe"])
    except ValueError:
        errors.append("Universe must be number")
        return errors
    if not (addr<= 512 and addr>= 1):
        errors.append("Address must be in range in range 1-512 inclusive")
    
    
    

    return errors

@app.route("/", methods = ['GET', 'POST'])
def index():
    global name, ALCRunning
    if request.method == "POST":
        updateSettings(request.form)
        print("Settings Updated")

    return render_template("webTemplate.html", 
                            name = settingsIni["artnetNode"]["name"], 
                            num  = settingsIni["artnetNode"]["numled"],
                            addr = settingsIni["artnetNode"]["startaddr"],
                            univ = settingsIni["artnetNode"]["dmxuniverse"],
                            ALCRunning = ALCRunning,
                            )

@app.route("/test")
def testPage():
    return "Hello World!"

@app.route("/toggleALC")
def toggleALC():
    global ALCRunning, ALCThread
    print("toggl", ALCRunning)
    ALCRunning = not ALCRunning
    if ALCRunning:
        ALCThread = Thread(target = ALCMain)
        ALCThread.start()
        print("STARTED THREAD")
    else:
        ALCStop()
        ALCThread.join()
        print("THREAD KILLED")
    return redirect(url_for("testPage"))
    # Ok new plan
    # when button is pressed, load a new page that just says "wait"
    # have a ready() function or wait til end of .join()
    # then after we know it's done we send them back to the index page
    # or
    # hmm
    # maybe we press the button and the button deactivates with JS
    # JS polls server asking if action is complete, when it is the button reactivates
    # I can do that right? I don't like a lot of JS though, worth considering at least
