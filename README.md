# sqlalchemy-challenge
Module 10


## Files

#### `Resources`
- This folder contains CSV and sqlite files that was used.

#### `climate.ipynb`
- Analysis Jupyter Notebook

#### `app.py`
-  Flask application


## Usage

**Flask application**:
-  `python app.py`

**Endpoints**:
   - `/`: Home route
   - `/api/v1.0/precipitation`: Returns precipitation data for the last year.
   - `/api/v1.0/stations`: Returns a list of all of the stations.
   - `/api/v1.0/tobs`: Returns temperature observations for the last year
   - `/api/v1.0/<start>`: Returns temperature statistics from a specified start date (format: YYYY-MM-DD)
   - `/api/v1.0/<start>/<end>`: Returns temperature statistics for a specified date range (format: YYYY-MM-DD/YYYY-MM-DD).
