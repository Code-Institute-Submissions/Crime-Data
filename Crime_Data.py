import json
import os

from flask import Flask
from flask import render_template
from pymongo import MongoClient

app = Flask(__name__)

# code for running locally
# MONGODB_HOST = 'localhost'
# MONGODB_PORT = 27017
# DBS_NAME = 'Crime_Data'
# COLLECTION_NAME = 'new_data'
# code for running locally

# code for running on heroku
# MONGODB_URI = os.getenv('MONGODB_URI')
# DBS_NAME = os.getenv('MONGO_DB_NAME', 'Crime_Data')
# COLLECTION_NAME = os.getenv('MONGO_COLLECTION_NAME', 'Crime_Data')


MONGODB_URI = 'mongodb://heroku_69fn47cd:i9lqct7bi6jv94mbk4dfi4j20@ds137550.mlab.com:37550/heroku_69fn47cd'
DBS_NAME = 'heroku_69fn47cd'
COLLECTION_NAME = 'new_data'

# code for running on heroku

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/crime")
def crime_new_data():
    FIELDS = {'Theft and related offences': True,
              'Kidnapping and related offences': True,
              'Public order and other social code offences': True,
              'Damage to property and to the environment': True,
              'Offences against government, justice procedures and organisation of crime': True,
              'Burglary and related offences': True,
              'Fraud, deception and related offences': True,
              'Controlled drug offences': True,
              'Weapons and Explosives Offences': True,
              'Station': True,
              'Robbery, extortion and hijacking offences': True,
              'Attempts or threats to murder, assaults, harassments and related offences': True,
              'Year': True,
              'Dangerous or negligent acts': True,
              'County': True,
              '_id': False}

    with MongoClient(MONGODB_URI) as conn:
        collection = conn[DBS_NAME][COLLECTION_NAME]

        new_data = collection.find(projection=FIELDS)
        result = json.dumps(list(new_data))
    return result


if __name__ == "__main__":
    app.run(debug=True)

# for getting database on m lab MongoDB
# mongoimport -h ds135820.mlab.com:35820 -d heroku_m8nfsm78 -c new_data -u heroku_m8nfsm78 -p eq55vmr1br17alr2djut1joke3 --file garda_stations.csv --type csv --headerline



# mongoimport -h ds137550.mlab.com:37550 -d heroku_69fn47cd -c new_data -u heroku_69fn47cd -p i9lqct7bi6jv94mbk4dfi4j20 --file Crime_Data_new_data_498887.json
#
# mongodb://heroku_69fn47cd:i9lqct7bi6jv94mbk4dfi4j20@ds137550.mlab.com:37550/heroku_69fn47cd

# mongoexport -h ds137550.mlab.com:37550 -d heroku_69fn47cd -c new_data -u heroku_69fn47cd -p i9lqct7bi6jv94mbk4dfi4j20 -o new_data.json