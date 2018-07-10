import re 
import sys
import json

class Processor():
    
    def __init__(self, FileName):  
            self.name= FileName

    

    def LoadJsonFile (self):
        tweets = [] 
        tweet_file = open(self.name, "r")
        for obj in tweet_file:
            try:
                tweet = json.loads(obj)
                tweets.append(tweet)
            except Exception as e:
                print ("type error: "+ str(e))
                
        return tweets

    def DoProcessing(self):
        return 0

    def WriteToDB(self, newOut):
        return 0
    

if __name__ =="__main__":
     x = Processor(sys.argv[1])
     x.LoadJsonFile()
     print(x.LoadJsonFile())

    