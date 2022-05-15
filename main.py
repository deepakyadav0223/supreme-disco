
import nltk
import numpy as np
#nltk.download("punkt") for first time here tokennier is present
from nltk.stem.porter import PorterStemmer
stemmer =  PorterStemmer()

def tokenize(string):
    return nltk.word_tokenize(string)

def stem(word):
     return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence , all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype = np.float32)
    for index, w, in enumerate(all_words):
        if w in tokenized_sentence:
            bag[index] = 1.0
    return bag







