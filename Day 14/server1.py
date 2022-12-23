# running a web application with Flask 
from flask import Flask
from scrape import run as scrape_runner


app = Flask(__name__)

#create routes
@app.route("/", methods=["GET"])
def hello_world():
    return ("Hello World. This is Flask!")

#create routes
@app.route("/abc", methods=["GET"])
def abc_view():
    return ("Hello ABC. This is Flask!")

#scraper route
@app.route("/box-office-mojo-scraper", methods=["POST"])
def box_office_mojo_scraper_world():
    scrape_runner()
    return {"data":[1,2,3]}
    