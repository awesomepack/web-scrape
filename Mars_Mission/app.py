# Importing Dependencies
from scrape import Scrape
from flask import Flask , render_template , redirect
from flask_pymongo import PyMongo

# Create Flask instance
app = Flask(__name__ , template_folder= 'template')

# Establish connection using PyMongo
mongo = PyMongo(app , uri = "mongodb://localhost:27017/scrape_app")

# / will serve as landing page
@app.route('/')
def root():
    return render_template("index.html" , text = "Welcome to my Home Page")
    

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