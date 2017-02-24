#encoding:utf-8

from pymongo import MongoClient
from scrapy.conf import settings


class MongoDBUtil( object ):

   def __init__( self,collection_name):
     client = MongoClient(settings[ 'MONGODB_HOST' ], settings[ 'MONGODB_PORT' ])
     self.db = client[settings[ 'MONGODB_DATABASE' ]]
     self .collection = self.db[collection_name]


   def write2Mongo(self, item):
       self.collection.insert(item)

   def setCollection(self,collection_name):
       self.collection = self.db[collection_name]
