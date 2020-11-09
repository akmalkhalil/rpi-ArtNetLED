from flask import Flask, request, render_template
import configparser
from config.Config import settingsFileName


# TODO: can I put this stuff in to if __name__ == "__main__ "?
app = Flask(__name__)


settingsIni = configparser.ConfigParser()
foo = settingsIni.read(settingsFileName)

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
    global name
    if request.method == "POST":
        updateSettings(request.form)
        print("Settings Updated")

    return render_template("webTemplate.html", 
                            name = settingsIni["artnetNode"]["name"], 
                            num  = settingsIni["artnetNode"]["numled"],
                            addr = settingsIni["artnetNode"]["startaddr"],
                            univ = settingsIni["artnetNode"]["dmxuniverse"],
                            )


