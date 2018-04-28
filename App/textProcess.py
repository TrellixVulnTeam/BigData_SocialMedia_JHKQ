import json
from nltk.tokenize import word_tokenize
import re 

data_store='C:/Users/tammy/Documents/python/data.json'

with open (data_store, 'r') as f:
    line = f.readline()
    tweet=json.loads(line)
   # print(json.dumps(tweet, indent=4))

each_tweet= 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print(word_tokenize(each_tweet))


emoticons_str = r 

regex_str = [
           emoticons_str,
           r'<[^>]+>', # HTML tags
           r'(?:@[\w_]+)', # @-mentions
           r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
           r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
           r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
           r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
           r'(?:[\w_]+)', # other words
           r'(?:\S)' # anything else
          
]