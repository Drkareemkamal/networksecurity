import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')


import certifi
ca = certifi.where() # retrieve the path to bundle of ca certificates provide by certificate

import pandas as pd
import numpy as np
import pymongo


## import logging exception --> in networksecurity.exception
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract:
    def __init__(self):
        
        pass

    def cv_to_json_convertor(self,file_path):
            
        try :
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e :
            raise NetworkDataExtract(e,sys)
        
    def insert_data_mongodb(self,records,collection,database):

        try :
            self.records = records
            self.database = database
            self.collection = collection
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__ == "__main__":
    FILE_PATH = 'Network_Data\phisingData.csv'
    DATABASE = 'drkareemkamal'
    collection = 'NetworkData'
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,collection)
    print(no_of_records)