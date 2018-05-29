from pymongo import MongoClient
from datetime import datetime
import json
from bson import json_util

client = MongoClient()

dbClass = client ['BigData']
col = dbClass['Tweets']

docs = 'text.json'
with open (docs, 'r') as f:
   for line in f:
    tweet=json.loads(line)
  

#col.insert_many(tweet)
print(col.find_one())


