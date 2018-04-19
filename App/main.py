from flask import Flask,json,request
from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy



ckey= 'ziEH3cxbutb6Yspn80pgBjRgD'
csecret= 'Wm3gCR4RA7Mx0cLl8WuwfkAZJxobBep0yVSuw492OQ1PEoakJE'
atoken= '703575776936005632-3smypE0iZTFxNXO6pEq1bM5rxwYBQix'
asecret= 'vpQrjsZZRsNRTzGYF0RhFKpBETQwP6qJeCo1cG8gBimfX'
KeyWords=['WorldCup','FIFA2018','RussiaWC']
data_store='data.json'

class listener(StreamListener):

    def on_data(self,data):
        try:
            with open(data_store,'a') as _file:
                _file.write(data)
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





