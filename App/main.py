import json
from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import os.path 

<<<<<<< HEAD


=======
>>>>>>> Data_preprocessing
ckey= 'ziEH3cxbutb6Yspn80pgBjRgD'
csecret= 'Wm3gCR4RA7Mx0cLl8WuwfkAZJxobBep0yVSuw492OQ1PEoakJE'
atoken= '703575776936005632-3smypE0iZTFxNXO6pEq1bM5rxwYBQix'
asecret= 'vpQrjsZZRsNRTzGYF0RhFKpBETQwP6qJeCo1cG8gBimfX'
KeyWords=['#worldcup ','#fifaworldcup','#wc2018','#2018worldcup','#russia2018']
<<<<<<< HEAD
data_store='/home/hduser/WorldCup3.json'
=======
data_store='C:/Users/tammy/Documents/python/final.json'
>>>>>>> Data_preprocessing
class listener(StreamListener):

    def on_data(self,data):
        try:
<<<<<<< HEAD
            with open(data_store,'a') as _file:
                _file.write(data)
=======
              
            with open(data_store,'a') as _file:
                _file.write(data)   
>>>>>>> Data_preprocessing
            return True
        except BaseException as e:
                 print ("Error Streaming Data: %s" &str(e))
                 return True 

    def on_error(self,status):
                print (status)
                return True

auth =OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream (auth,listener())
twitterStream.filter(track=KeyWords)





