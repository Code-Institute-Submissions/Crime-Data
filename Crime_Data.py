from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

DBS_NAME = 'Crime_Data'
COLLECTION_NAME = 'source'


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/stuff")
def crime_source():
    FIELDS = {'x': True, 'y': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2004': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2005': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2006': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2007': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2008': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2009': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2010': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2011': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2012': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2013': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2014': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2015': True,
              'Attempts or threats to murder, assaults, harassments and related offences 2016': True,
              '_id': False}

    with MongoClient(MONGODB_HOST, MONGODB_PORT) as conn:
        collection = conn[DBS_NAME][COLLECTION_NAME]

        source = collection.find(projection=FIELDS)
        result = json.dumps(list(source))
    return result


if __name__ == "__main__":
    app.run(debug=True)


