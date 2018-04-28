import json
from nltk.tokenize import word_tokenize

data_store='C:/Users/tammy/Documents/python/data.json'

with open (data_store, 'r') as f:
    line = f.readline()
    tweet=json.loads(line)
   # print(json.dumps(tweet, indent=4))

each_tweet= 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print(word_tokenize(each_tweet))