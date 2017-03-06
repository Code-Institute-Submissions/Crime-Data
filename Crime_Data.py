from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

DBS_NAME = 'Crime_Data'
COLLECTION_NAME = 'projects'


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/crime")
def crime_projects():
    FIELDS = {'x': True, 'y': True,
              'Station': True,
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
              'Divisions': True,
              'Dangerous or negligent acts 2003': True,
              'Dangerous or negligent acts 2004': True,
              'Dangerous or negligent acts 2005': True,
              'Dangerous or negligent acts 2006': True,
              'Dangerous or negligent acts 2007': True,
              'Dangerous or negligent acts 2008': True,
              'Dangerous or negligent acts 2009': True,
              'Dangerous or negligent acts 2010': True,
              'Dangerous or negligent acts 2011': True,
              'Dangerous or negligent acts 2012': True,
              'Dangerous or negligent acts 2013': True,
              'Dangerous or negligent acts 2014': True,
              'Dangerous or negligent acts 2015': True,
              'Dangerous or negligent acts 2016': True,
              'Kidnapping and related offences 2003': True,
              'Kidnapping and related offences 2004': True,
              'Kidnapping and related offences 2005': True,
              'Kidnapping and related offences 2006': True,
              'Kidnapping and related offences 2007': True,
              'Kidnapping and related offences 2008': True,
              'Kidnapping and related offences 2009': True,
              'Kidnapping and related offences 2010': True,
              'Kidnapping and related offences 2011': True,
              'Kidnapping and related offences 2012': True,
              'Kidnapping and related offences 2013': True,
              'Kidnapping and related offences 2014': True,
              'Kidnapping and related offences 2015': True,
              'Kidnapping and related offences 2016': True,
              'Robbery, extortion and hijacking offences 2003': True,
              'Robbery, extortion and hijacking offences 2004': True,
              'Robbery, extortion and hijacking offences 2005': True,
              'Robbery, extortion and hijacking offences 2006': True,
              'Robbery, extortion and hijacking offences 2007': True,
              'Robbery, extortion and hijacking offences 2008': True,
              'Robbery, extortion and hijacking offences 2009': True,
              'Robbery, extortion and hijacking offences 2010': True,
              'Robbery, extortion and hijacking offences 2011': True,
              'Robbery, extortion and hijacking offences 2012': True,
              'Robbery, extortion and hijacking offences 2013': True,
              'Robbery, extortion and hijacking offences 2014': True,
              'Robbery, extortion and hijacking offences 2015': True,
              'Robbery, extortion and hijacking offences 2016': True,
              'Burglary and related offences 2003': True,
              'Burglary and related offences 2004': True,
              'Burglary and related offences 2005': True,
              'Burglary and related offences 2006': True,
              'Burglary and related offences 2007': True,
              'Burglary and related offences 2008': True,
              'Burglary and related offences 2009': True,
              'Burglary and related offences 2010': True,
              'Burglary and related offences 2011': True,
              'Burglary and related offences 2012': True,
              'Burglary and related offences 2013': True,
              'Burglary and related offences 2014': True,
              'Burglary and related offences 2015': True,
              'Burglary and related offences 2016': True,
              'Theft and related offences 2003': True,
              'Theft and related offences 2004': True,
              'Theft and related offences 2005': True,
              'Theft and related offences 2006': True,
              'Theft and related offences 2007': True,
              'Theft and related offences 2008': True,
              'Theft and related offences 2009': True,
              'Theft and related offences 2010': True,
              'Theft and related offences 2011': True,
              'Theft and related offences 2012': True,
              'Theft and related offences 2013': True,
              'Theft and related offences 2014': True,
              'Theft and related offences 2015': True,
              'Theft and related offences 2016': True,
              'County': True,
              '_id': False}

    with MongoClient(MONGODB_HOST, MONGODB_PORT) as conn:
        collection = conn[DBS_NAME][COLLECTION_NAME]

        projects = collection.find(projection=FIELDS)
        result = json.dumps(list(projects))
    return result


if __name__ == "__main__":
    app.run(debug=True)


