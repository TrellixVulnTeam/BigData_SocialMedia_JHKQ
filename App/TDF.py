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
       

    def tokens (self, sentenceData):
        tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
        wordsData = tokenizer.transform(sentenceData)

    def hashing(self, wordsData):

        hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
        featurizedData = hashingTF.transform(wordsData)
       # alternatively, CountVectorizer can also be used to get term frequency vectors

        idf = IDF(inputCol="rawFeatures", outputCol="features")
        idfModel = idf.fit(featurizedData)
        rescaledData = idfModel.transform(featurizedData)

        rescaledData.select("label", "features").show()
    

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
    #myTdf.stopWordsRemove()
    print (myTdf.doCounter())
    myTdf.Visual()