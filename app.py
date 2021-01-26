#Create a New Python File and Import the Flask Dependency
#from flask import Flask
#Create a New Flask App Instance
##app = Flask(__name__)
#Create Flask Routes
#Notice the forward slash inside of the app.route? This denotes that we want to put our data at the root of our routes. The forward slash 
#is commonly known as the highest level of hierarchy in any computer system.
#@app.route('/')
#Next, create a function called hello_world(). Whenever you make a route in Flask, you put the code you want in that specific route below 
#@app.route(). Here's what it will look like:
#@app.route('/')
#def hello_world():
    #return 'Hello world'

#Run a Flask App
#The process of running a Flask app is a bit different from how we've run Python files. To run the app, we're first going to need to use 
#the command line to navigate to the folder where we've saved our code. You should save this code in the same folder you've used in the 
#rest of this module.
#Once you've ensured that your code is saved in the proper directory, then run the following command if you are on a Mac. This command 
#sets the FLASK_APP environment variable to the name of our Flask file, app.py.
#export FLASK_APP=app.py
#set FLASK_APP=app.py
#flask run
#Environment variables are essentially dynamic variables in your computer. They are used to modify the way a certain aspect of the 
#computer operates. For our FLASK_APP environment variable, we want to modify the path that will run our app.py file so that we can run our file.

##-----------##

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Set Up the Database
#The create_engine() function allows us to access and query our SQLite database file. Now let's reflect the database into our classes.
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
#Add the following code to reflect the database:
Base.prepare(engine, reflect=True)

#With the database reflected, we can save our references to each table. Again, they'll be the same references as the ones we wrote earlier in this module. We'll create a variable for each of the classes so that we can reference them later, as shown below.
Measurement = Base.classes.measurement
Station = Base.classes.station

#Finally, create a session link from Python to our database with the following code:
session = Session(engine)

#Next, we need to define our app for our Flask application.
#Set Up Flask
#To define our Flask app, add the following line of code. This will create a Flask application called "app."
app = Flask(__name__)

#Notice the __name__ variable in this code. This is a special type of variable in Python. Its value depends on where and how the code is run. For example, if we wanted to import our app.py file into another Python file named example.py, the variable __name__ would be set to example. Here's an example of what that might look like:
#import app

#print("example __name__ = %s", __name__)

#if __name__ == "__main__":
    #print("example is being run directly.")
#else:
    #print("example is being imported")
#However, when we run the script with python app.py, the __name__ variable will be set to __main__. This indicates that we are not using any other file to run this code.

#Now we're ready to build our Flask routes!

#Create the Welcome Route
#All of your routes should go after the app = Flask(__name__) line of code. Otherwise, your code may not run properly.
#We can define the welcome route using the code below:
@app.route("/")

#Now our root, or welcome route, is set up. The next step is to add the routing information for each of the other routes. For this we'll create a function, and our return statement will have f-strings as a reference to all of the other routes. This will ensure our investors know where to go to view the results of our data.
#First, create a function welcome() with a return statement. Add this line to your code:
#Next, add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement. We'll use f-strings to display them for our investors:
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route. This convention signifies that this is version 1 of our application. This line can be updated to support future versions of the app as well.
#The welcome route is now defined, so let's try to run our code. You can run Flask applications by using the command below, but you'll need a web browser to view the results.

#Let's start by using the command line to navigate to your project folder. Then run your code:
#flask run

#Precipitation Route
#Every time you create a new route, your code should be aligned to the left in order to avoid errors.
@app.route("/api/v1.0/precipitation")
#Next, we will create the precipitation() function.
#def precipitation():
    #return
#Now we can add code to the function. This code may look almost identical to code you've written previously, but now we'll dive deeper into our precipitation analysis and figure out how to best integrate it into our application.
#First, we want to add the line of code that calculates the date one year ago from the most recent date in the database. Do this now so that your code looks like the following:
#Next, write a query to get the date and precipitation for the previous year. Add this query to your existing code.
#def precipitation():
   #prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   #precipitation = session.query(Measurement.date, Measurement.prcp).\
      #filter(Measurement.date >= prev_year).all()
   #return

#Notice the .\ in the first line of our query? This is used to signify that we want our query to continue on the next line. You can use the combination of .\ to shorten the length of your query line so that it extends to the next line.
#Finally, we'll create a dictionary with the date as the key and the precipitation as the value. To do this, we will "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file.
#JSON files are structured text files with attribute-value pairs and array data types. They have a variety of purposes, especially when downloading information from the internet through API calls. We can also use JSON files for cleaning, filtering, sorting, and visualizing data, among many other tasks. When we are done modifying that data, we can push the data back to a web interface, like Flask.
#We'll use jsonify() to format our results into a JSON structured file. When we run this code, we'll see what the JSON file structure looks like. Here's an example of what a JSON file might look like:
#{
#"city" : {
#"name" : "des moines",
#        "region" : "midwest"
#}

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)


#Stations Route
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#Monthly Temperature Route
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


#Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


