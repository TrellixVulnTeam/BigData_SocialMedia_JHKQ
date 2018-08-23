from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from nltk.corpus import stopwords
from collections import Counter
from nltk import word_tokenize
from nltk.tokenize import wordpunct_tokenize
import sys
import matplotlib.pyplot as plt 

class TDF():
    def __init__(self, FileName, NewFile):
         self.name = FileName
         self.newfile = NewFile
    
    def computeTDF(self, myfile):
        import math 
        
        idfDict ={}
        N = len(myfile)
        idfDict = dict.fromkeys(myfile[0].keys() , 0)
        for doc in myfile:
            for word, val in doc.items():
                if val > 0:
                    idfDict[word] += 1
        for word, val in idfDict.items():
            idfDict[word] = math.log10(N / float(val) )
        return idfDict 
    
    def computeTDFIF(self,tfBow, idfs):
        tfidf = {}
        for word, val in tfidf.items():
            tfidf[word] = val * idfs[word]
        return tfidf
    def stopWordsRemove(self):
        myfile =open(self.name)
        stop_words = set(stopwords.words('english'))
        line = myfile.read()
        words = line.split()
        for r in words:
            if not r in stop_words:
               appendfile = open(self.newfile, 'a')
               appendfile.write(" "+r)
               appendfile.close()

    print ("success")

    def doCounter(self):
        myfile =open(self.newfile, "r", encoding="utf-8-sig")
        wordcount = Counter(myfile.read().split())
        dic =  wordcount.most_common(7)
        return dic 

    def Visual(self):
        plt.subplot(111, facecolor='w')
        alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}        
        t = plt.text(0.0, 0.9, 'Hot Topics World Cup', size='large', **alignment)
        yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]
        myDict = self.doCounter()
        for k, family in enumerate(myDict):
            t = plt.text(0.0, yp[k], family, family=family, **alignment)
        x = -0.4

        plt.axis([-1, 1, 0, 1])
        plt.show()

if __name__ == "__main__":
    original = sys.argv[1]
    newfile = sys.argv[2]
    myTdf = TDF(original, newfile)
    myTdf.stopWordsRemove()
    #print (myTdf.doCounter())
    #myTdf.Visual()