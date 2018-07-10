import sys
import os
import re
import json
from functools import partial
from collections import Counter
from nltk.tokenize import word_tokenize
import pandas as pd 
import matplotlib.pyplot as plt 

#emoticons extracted 
tweet= []
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )""" 
regex_str  = [
    emoticons_str,
    r'<[^>]+>',#HTML hash tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
docs = 'C:/Users/tammy/Documents/python/tweets.json'

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

def getHash(tweet):
    entities = tweet.get('entities', {})
    hashtags = entities.get('hashtags', [])
    return [tag['text'].lower() for tag in hashtags]


def read():
    fname = 'C:/Users/tammy/Documents/python/final2.json'
    tweets = []
    count = Counter()

    with  open (fname, 'r') as f:
        
        for line in f:
            try:
          
                tweet= json.loads(line)
                tweets.append(tweet)
            #terms_all = [term for term in preprocess(tweet['text'])]
            #count.update(terms_all)
            except:
             continue
           
        tweets = pd.DataFrame() 
        tweets["text"] = map(lambda tweet:tweet["text", tweets])
        tweets["lang"] = map(lambda tweet:tweet["lang", tweets])
          
read()

