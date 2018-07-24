import re 
import sys
import json
from Filter import Filter


class Processor():
    
    def __init__(self, FileName, newFile):  
            self.name= FileName
            self.newfile = newFile


    def LoadJsonFile (self):
        tweets = [] 
        tweet_file = open(self.name, "r")
        for obj in tweet_file:
            try:
                tweet = [json.loads(obj).get('text')]
                tweets.append(tweet)
               # print (tweets)
            except:
                pass
                
        return tweets

    def DoProcessing(self):
        return 0

    def WriteToDB(self):
        tweet = self.LoadJsonFile()
        myfile = self.newfile
        Filtering = Filter(self.name)

        with open (myfile, 'w') as f:
            for t in tweet:
                data = Filtering.strip_links(str(t))
                
                try:
                   f.write(data)
                   print(data)
                  
                  
                except:
                  pass 
                  f.flush()
                  f.close()
               

        print("Write success")
     
if __name__ =="__main__":
     x = Processor(sys.argv[1], sys.argv[2])
     x.LoadJsonFile()
     x.WriteToDB()


    