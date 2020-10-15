from flask import Flask, request, render_template
import configparser


# TODO: can I put this stuff in to if __name__ == "__main__ "
app = Flask(__name__)

config = configparser.ConfigParser()
config.read("conf.ini")

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
    if (form.get("macros") == "True"):
        config["artnetNode"]["macros"] = '1'
    else:
        config["artnetNode"]["macros"] = '0'
    with open("conf.ini", 'w') as confFile:
        config.write(confFile)

@app.route("/", methods = ['GET', 'POST'])
def index():
    global name
    if request.method == "POST":
        print(request.form.get("macros"))
        updateConf(request.form)
        print("Config Updated")

    return render_template("webTemplate.html", 
                            name  = config["artnetNode"]["name"], 
                            num   = config["artnetNode"]["numled"],
                            addr  = config["artnetNode"]["startaddr"],
                            univ  = config["artnetNode"]["dmxuniverse"],
                            macros= config["artnetNode"]["macros"],
                            )


