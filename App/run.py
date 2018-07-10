
import json
import matplotlib.pyplot as plt
import pandas as pd   
import re, string  
from nltk.corpus import stopwords
from collections import Counter
from nltk import word_tokenize
from nltk.tokenize import wordpunct_tokenize
import ijson 
from itertools import islice



fname = 'C:/Users/tammy/Documents/python/data.json'
tweet_data = []
tweet_file = open (fname, "r")


def read():    
    for line in tweet_file:
        try:
            tweet= json.loads(line)
            tweet_data.append(tweet)
        except:
         continue
    
    return tweet_data         

def strip_links(text):
    return  ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text).split())

def writeToDB():
    myfile = "C:/Users/tammy/Documents/python/final.txt"
    tweet = read()
    with open (myfile, 'w') as f:
        
        for t in tweet:
            data = strip_links(t['text'])
            try:
               f.write(data)
            except:
                continue
        #f.close()
            
      

def display():
     myfile =open("C:/Users/tammy/Documents/python/clean.txt", "r", encoding="utf-8-sig")
     wordcount = Counter(myfile.read().split())
    
     
     for item in wordcount.items():
        print ("{}\t{}".format(*item))
     
     print(wordcount.most_common(10))      


def trial():
    myfile =open("C:/Users/tammy/Documents/python/final.txt")
    stop_words = set(stopwords.words('english'))
    line = myfile.read()
    words = line.split()
    for r in words:
        if not r in stop_words:
           appendfile = open('C:/Users/tammy/Documents/python/clean.txt', 'a')
           appendfile.write(" "+r)
           appendfile.close()

    print ("success")
    



#trial()


display()

#print(read())
#writeToDB()
