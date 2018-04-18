from flask import Flask,json,request
from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy



ckey= 'ziEH3cxbutb6Yspn80pgBjRgD'
csecret= 'Wm3gCR4RA7Mx0cLl8WuwfkAZJxobBep0yVSuw492OQ1PEoakJE'
atoken= '703575776936005632-3smypE0iZTFxNXO6pEq1bM5rxwYBQix'
asecret= 'vpQrjsZZRsNRTzGYF0RhFKpBETQwP6qJeCo1cG8gBimfX'

class listener(StreamListener):

    def on_data(self,data):
        print (data)
        return True 

    def on_error(self,status):
        print (status)



auth =OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream (auth,listener())
twitterStream.filter(track=["WorldCup"])





