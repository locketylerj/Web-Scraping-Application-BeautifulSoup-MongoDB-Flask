# Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

# Store the return value in Mongo as a Python dictionary.
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"]="mongodb://localhost:27017/mars_app"

mongo = PyMongo(app)

@app.route("/")
def home():
    
    
    marsdata = mongo.db.marsUpdates.find_one()

    return render_template("index.html", marsdata=marsdata)

@app.route("/scrape")
def scrape():

    marsdata = mongo.db.marsUpdates

    mars_update = scrape_mars.scrape()
    
    marsdata.update({},mars_update, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)