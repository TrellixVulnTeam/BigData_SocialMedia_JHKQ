import re 
import sys
import json
from Filter import Filter


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
                continue
                
        return tweets

    def DoProcessing(self):
        return 0

    def WriteToDB(self):
        tweet = self.LoadJsonFile()
        myfile = "C:/Users/tammy/Documents/python/Output.txt"
        Filtering = Filter(self.name)

        with open (myfile, 'w') as f:
            for t in tweet:
                data = Filtering.strip_links(t['text'])
                try:
                   f.write(data)
                except Exception as ex:
                   print ("Error :" + str(ex))

        print("Write success")
     
if __name__ =="__main__":
     x = Processor(sys.argv[1])
     x.LoadJsonFile()
     x.WriteToDB()


    