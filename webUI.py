from flask import Flask, request, render_template
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read("conf.ini")


def updateConf(form):
    global config
    config["artnetNode"]["name"] = form["inputName"]
    config["artnetNode"]["startaddr"] = form["address"]
    config["artnetNode"]["dmxuniverse"] = form["universe"]
    #config["artnetNode"]["type"] = form["type"]
    config["artnetNode"]["numled"] = form["num"]
    with open("conf.ini", 'w') as confFile:
        config.write(confFile)

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


