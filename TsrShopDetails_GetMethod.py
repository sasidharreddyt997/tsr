# Library Imports
import json # This lib used for converting Python objects to JSON objects
from datetime import datetime
import psycopg2 # For connecting to the database
from flask import Flask, request # To create application object
# To read the request details like parameters / request body
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


# Create the application object using flask framework
app = Flask(__name__)

# Parse the app instance/object to Api Base class to utilise all the services
api = Api(app)

# This a the base class which should have all database table related features
# To work with any database table operations

Base = declarative_base()

# Construct the database URL which will be used for connecting to right database
database_url = "postgresql://postgres:1234@localhost:5432/postgres"

# poolclass=NullPool - Disable sqlalchemy poolling using NullPool
# as by default Postgres has its own pool

# database_url - Constructed url to create engine object which will then
# be used to perform database operations.

# echo - To capture all database events echo set to True which will give more insights about the
# database operations which will eventually help us to understand what's going on while app
# is being using by the end users (customers)
engine = create_engine(database_url, echo=True, poolclass=NullPool)

# Create session using sessio maker
Session = sessionmaker(bind=engine)

# Create the session object -This is the object being used in the all data base transactions!
session = Session()

class TsrShopDetailsProject(Base):
    __tablename__ = "tsrshopdetails"
    Name = Column("name", String)
    Email = Column("email", String)
    City = Column("city", String)
    State = Column("state", String)
    Dealer = Column("dealer", String)
    Vehicle = Column("vehicle", String)
    Dealer_city = Column("dealer_city", String)
    Mobile_number = Column("mobile_number", Integer, primary_key=True)

# http://127.0.0.1:5000/TsrShopDetails/task1/getmethod
@app.route('/TsrShopDetails/task1/getmethod', methods=['GET'])
def tsr_shop_details():
    results = session.query(TsrShopDetailsProject).all()
    results_1 = [item.__dict__ for item in results]
    for item in results_1:
        del item['_sa_instance_state']
    return json.dumps(results_1)
app.run(debug=True)