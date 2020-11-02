from flask import Flask, request, render_template
import configparser


# TODO: can I put this stuff in to if __name__ == "__main__ "?
app = Flask(__name__)

confFileName = "config/conf.ini"
config = configparser.ConfigParser()
config.read(confFileName)

# Can be run to create a valid config file with default values already set up
def initConf(fileName = "config.ini.example"):
    pass

def updateConf(form):
    # TODO: form validation? seperate function for validation I think???
    global config
    config["artnetNode"]["name"] = form["inputName"]
    config["artnetNode"]["startaddr"] = form["address"]
    config["artnetNode"]["dmxuniverse"] = form["universe"]
    #config["artnetNode"]["type"] = form["type"]
    config["artnetNode"]["numled"] = form["num"]
    with open(confFileName, 'w') as confFile:
        config.write(confFile)

def validateConf(form):
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
        updateConf(request.form)
        print("Config Updated")

    return render_template("webTemplate.html", 
                            name = config["artnetNode"]["name"], 
                            num  = config["artnetNode"]["numled"],
                            addr = config["artnetNode"]["startaddr"],
                            univ = config["artnetNode"]["dmxuniverse"],
                            )


