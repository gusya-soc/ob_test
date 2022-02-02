from urllib import request
from django.db import connection
import logging
import pymongo
import os
from pymongo import InsertOne,DeleteOne,ReplaceOne


class CosmosDB():
    def __init__(self,collection):
        self.connection_string = os.environ['CON_STRING']
        self.client = pymongo.MongoClient(self.connection_string)
        # self.collection = collection
        self.db = self.client['test']
        self.collection = self.db[collection]

    def insert(self,doc):
        request = [InsertOne(doc)]
        result = self.process(request)
        assert result.inserted_count == 1
        return result
    
    def remove(self,id):
        request = [DeleteOne({"id":id})]
        result = self.process(request)
        assert result.deleted_count == 1
    
    def find_by_id(self,id):
        return self.collection.find_one({"id":id})
 
    def update(self,id,doc):
        request = [ReplaceOne({"id":id},doc,upsert=True)]
        result = self.process(request)
        logging.info(f"{result.modified_conut},{result.upserted_ids}")
    
    def process(self,request):
        result = self.collection.bulk_write(request)
        return result