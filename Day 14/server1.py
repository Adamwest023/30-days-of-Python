#creating a server with Flask 
from flask import Flask


app = Flask(__name__)

#create routes
@app.route("/", methods=["GET"])
def hello_world():
    return ("Hello World. This is Flask!")

#create routes
@app.route("/abc", methods=["GET"])
def abc_view():
    return ("Hello ABC. This is Flask!")
    