from flask import Flask,json,request
from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy

app = Flask(__name__)
app.config.from_object('config')

auth = tweepy.OAuthHandler(app.config['ziEH3cxbutb6Yspn80pgBjRgD'],app.config('Wm3gCR4RA7Mx0cLl8WuwfkAZJxobBep0yVSuw492OQ1PEoakJE'))
auth.set_access_token(app.config['703575776936005632-3smypE0iZTFxNXO6pEq1bM5rxwYBQix'],app.config['vpQrjsZZRsNRTzGYF0RhFKpBETQwP6qJeCo1cG8gBimfX'])
tweepy_api=tweepy.API(auth)



@app.route('/')
class listener(StreamListener):
    def on_data(self,data):
       
        return data 

    def on_error(self,status):
        return status



if __name__=='__main__':
    app.run(debug=True)


