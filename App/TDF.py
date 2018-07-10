from pyspark.ml.feature import HashingTF, IDF, Tokenizer


class TDF():
    def __init__(self, FileName):
         self.name = FileName

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
    

    def stopWords():
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