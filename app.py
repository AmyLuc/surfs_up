#import dependencies
from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#Set up access to databases
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect database for ease of access.
Base = automap_base()
Base.prepare(engine, reflect=True)

#create references to different classes.
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link between Python and the database
session = Session(engine)

#create flask app
app = Flask(__name__)

#create first route
@app.route('/')
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

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    # convert dictionary to JSON file
    precip= {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
# add </api/v1.0/precipitation> to end of http (<flask run> in terminal)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
# add </api/V1.0/stations>

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
# add </api/v1.0/tobs>