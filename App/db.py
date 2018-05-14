from pymongo import MongoClient
from datetime import datetime

client = MongoClient()

dbClass = client ['tutorial']

doc = ''
