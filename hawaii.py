import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database setup
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Building Flask app
app = Flask(__name__)

@app.route("/")
def index():
    return (
        "Available Routes:<br />"
        "/api/v1.0/precipitation<br />"
        "/api/v1.0/stations<br />"
        "/api/v1.0/tobs<br />"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    all_prcp = []
    
    #Format into JSON
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict[date] = prcp
        all_prcp.append(prcp_dict)
    
    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
def stations():    
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > '2016-08-23').all()
    session.close()
    
    all_temps = []

    for date, tobs in results:
        temp_dict = {}
        temp_dict[date] = tobs
        all_temps.append(temp_dict)

    return jsonify(all_temps)

if __name__ == "__main__":
    app.run(debug=True)