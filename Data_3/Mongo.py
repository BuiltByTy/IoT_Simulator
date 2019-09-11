
"""

An External Python code to connect data server to the database (monogdb),
Goals:
    -Establish Connection with MongoDB
    -Post data onto database
    -Query and use data from database
    -If connection is severed create a warning
"""


import threading
import pymongo
import logging
import time

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'Your DB name'
COLLECTION_NAME = 'collectionname'
client = MongoClient("localhost", 27017)

# Used to log event in the event of a severed connection to Mongo Server

def thread_function(name):

    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
    
# Functions used to collect and query data from Mongoo
class Mongo_Connection(object):

    def __init__(self, host, port, db_name, collection_name):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name



while client is True:
    print("Connection to Database Succesful")

    

