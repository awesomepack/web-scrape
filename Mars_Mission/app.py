# Importing Dependencies
from scrape import Scrape
from flask import Flask , render_template , redirect
from flask_pymongo import PyMongo
import pymongo

# Create Flask instance
app = Flask(__name__ , template_folder= 'template')

# Establish connection using PyMongo
mongo = PyMongo(app , uri = "mongodb://localhost:27017/scrape_app")

# / will serve as landing page
@app.route('/')
def root():

    # Create connection to local instance of mongo
    conn = 'mongodb://localhost:27017'

    # Pass connection to PyMongo
    client = pymongo.MongoClient(conn)

    # Connect to the scrape_app DB
    db = client.scrape_app

    # Drops collection if exists to prevent duplicates
    db.scrape_app.drop()

    # Collecting data from collection
    mars_data = db.collection.find_one({})



    # Render HTML file by passing queried data
    return render_template("index.html" , mars_data  = mars_data)
    

# /scrape will extract data from websites and store as dictionary for loading in mongo db
@app.route('/scrape')
def scrape():

    # Call the Scrape function
    scrape_data = Scrape()

    # Updating mongo database with scraped data
    mongo.db.collection.update({}, scrape_data , upsert = True)

    # Return to Home Page
    return redirect('/')



if __name__ == '__main__':
    app.run(debug = True)