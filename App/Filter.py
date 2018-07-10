
import nltk
import re 
import string 

class Filter():

    def __init__(self, FileName):
        self.name = FileName

    def RegFormula(self):
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

    def strip_links(self, text):
        return  ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text).split())

    