import re
import json





with open ('tweets.json', 'r') as f:
   for line in f:
      tweet=json.loads(line)
       
   
      
      print(tweet)

