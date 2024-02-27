# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a dictionary of prepresentation"""
    start = dt.date(2017,8,23)
    year_ago = start - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).\
                            filter(Measurement.date >= year_ago).all()
    one_year_precipitation = {date: prcp for date, prcp in results}

    return jsonify(one_year_precipitation)



@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations from the dataset"""
    results = session.query(Station.station).all()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)



@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of temperature observations for the previous year"""
    start = dt.date(2017,8,23)
    year_ago = start - dt.timedelta(days=365)
    results = session.query(Measurement.date,Measurement.tobs).filter((Measurement.date >= year_ago)).all()
                # filter((Measurement.station == 'USC00519281')).all()

    temperature_data = []
    for date, tobs in results:
        temperature_dict = {}
        temperature_dict["date"] = date
        temperature_dict["temperature"] = tobs
        temperature_data.append(temperature_dict)

    return jsonify(temperature_data)



@app.route("/api/v1.0/<start>")
def start(start):
    
    results = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
                filter(Measurement.date >= start).all()

    stats_list = []
    for min, max,avg in results:
        stats_dict = {}
        stats_dict["Min"] = min
        stats_dict["Max"] = max
        stats_dict["Average"] = avg
        stats_list.append(stats_dict)

    return jsonify(stats_list)



@app.route("/api/v1.0/<start>/<end>")
def startend(start,end):
    
    results = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
                    filter(Measurement.date >= start, Measurement.date <= end).all()

    stats_list = []
    for min, max,avg in results:
        stats_dict = {}
        stats_dict["Min"] = min
        stats_dict["Max"] = max
        stats_dict["Average"] = avg
        stats_list.append(stats_dict)

    return jsonify(stats_list)



if __name__ == '__main__':
    app.run(debug=True)
    session.close()








