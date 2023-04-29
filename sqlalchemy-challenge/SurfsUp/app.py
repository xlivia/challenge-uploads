# Import the dependencies.
import datetime as dt
import numpy as np
import json
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask
from dateutil.relativedelta import relativedelta

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route('/favicon.ico')
def favicon():
    return ''

# Start at the homepage and list all the available routes.
@app.route("/")
def home():
    return (
        f"<h1>Welcome to the Hawaii climate API!<h1>"
        f"<h2>Available routes:<h2>"
        f"<li><a href=\"/api/v1.0/precipitation\">/api/v1.0/precipitation</a></li>"
        f"<li><a href=\"/api/v1.0/stations\">/api/v1.0/stations</a></li>"
        f"<li><a href=\"/api/v1.0/tobs\">/api/v1.0/tobs</a></li>"
        f"<li><a href=\"/api/v1.0/&lt;start&gt;\">/api/v1.0/&lt;start&gt;</a></li>"
        f"<li><a href=\"/api/v1.0/&lt;start&gt;/&lt;end&gt;\">/api/v1.0/&lt;start&gt;/&lt;end&gt;</a></li>"
    ), 200, {'Content-Type': 'text/html'}

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    last_date = dt.datetime.strptime(last_date, '%Y-%m-%d')
    first_date = last_date - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= first_date).all()
    prcp_data = {}
    for date, prcp in results:
        prcp_data[date] = prcp
    session.close()
    return json.dumps(prcp_data, indent=4), 200, {'Content-Type': 'application/json'}

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    # Convert list of tuples into normal list
    stations = list(np.ravel(results))
    session.close()
    return json.dumps(stations, indent=4), 200, {'Content-Type': 'application/json'}

# Define the route and function
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    # Calculate the date 1 year ago from the last data point in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
    one_year_ago = last_date - relativedelta(years=1)
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]
    # Query the most active station for the last year of temperature observation data
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= one_year_ago).all()
    # Create a list of dicts with `date` and `tobs` as the keys and values
    tobs_list = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)
    session.close()
    # Return the JSON representation of the list
    return json.dumps(tobs_list, indent=4), 200, {'Content-Type': 'application/json'}

# define function to calculate TMIN, TAVG, and TMAX for a given date range
def calc_temps(start_date, end_date=None):
    # create session and query database
    session = Session(engine)
    if end_date:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
            .filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    else:
        end_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
        end_date = dt.datetime.strptime(end_date[0], '%Y-%m-%d').date()
        start_date = end_date - relativedelta(years=1)
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
            .filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    # convert results to a list
    temp_list = list(np.ravel(results))
    # close session
    session.close()
    # return results as a JSON object
    return json.dumps(temp_list, indent=4), 200, {'Content-Type': 'application/json'}

# create Flask routes
@app.route('/api/v1.0/<start>')
def temp_range_start(start):
    # call calc_temps function with start date provided
    return calc_temps(start)

@app.route('/api/v1.0/<start>/<end>')
def temp_range_start_end(start, end):
    # call calc_temps function with both start and end dates provided
    return calc_temps(start, end)

# run app if script is executed
if __name__ == '__main__':
    app.run()
