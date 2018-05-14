from pymongo import MongoClient
from datetime import datetime

client = MongoClient()

dbClass = client ['BigData']
col = dbClass['Tweets']

doc = 'C:/Users/tammy/Documents/python/data.json'

doc_id =  col.insert_one(doc).inserted_id

