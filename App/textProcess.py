import sys
import os
import re
import json
from json import JSONDecoder
from functools import partial
from collections import Counter
from nltk.tokenize import word_tokenize

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

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
docs = 'C:/Users/tammy/Documents/python/text.json'
count = 0
data = []

#buffer 
def json_parse (fileobj, decoder=JSONDecoder(), buffersize=2048):
    buffer = ''
    for chunk in iter(partial(fileobj.read, buffersize), ''):
        buffer += chunk
        while buffer:
            try:
                result, index = decoder.raw_decode(buffer)
                yield result
                buffer = buffer[index:]
            except ValueError:
                #not enough data to decode, read more
                break


diction = [] 

def MergeJSONFile():
    
#splitting function
def ConvertToDictionary():
    with open (docs, 'r') as f:
        
        for line in f:
            diction = json.loads(line)
          
        for i in range (len(diction)):
            tweet.append(diction[i]['text'])
    return tweet

def TermOccurence():
    _data = ConvertToDictionary()
    count_all = Counter()
    terms =  [term for term in preprocess(str(_data))]
    count_all.update(terms)
    return  count_all.most_common(5)
        

print (TermOccurence())
