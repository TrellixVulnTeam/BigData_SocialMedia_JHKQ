<<<<<<< HEAD
def runTest():
    return 0
=======
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import pyLDAvis.gensim
import sys


class LDA:
    def __init__(self, oldFile):
        self.oldfile = oldFile
    def do(self):
        tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
        en_stop = get_stop_words('en')

        p_stemmer = PorterStemmer()

        tweet_file = open(self.oldfile, "r")
# create sample documents

        doc = []
        for w in tweet_file:
            doc.append(w)
        doc_set = doc 
        texts = []
        
        for i in doc_set:
            raw = i.lower()
        tokens = tokenizer.tokenize(raw)

        stopped_token = [i for i in tokens if not i in en_stop]

        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_token]

        texts.append(stemmed_tokens)

        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=4)

        print(ldamodel.print_topics(num_topics=5))

#pyLDAvis.enable_notebook()
        visualisation = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)
        pyLDAvis.save_html(visualisation, 'C:/Users/tammy/Documents/python/Low_Visualization.html')
        print ("Visual Created")


if __name__ == '__main__':

    load = LDA(sys.argv[1])
    load.do()


>>>>>>> Data_preprocessing
