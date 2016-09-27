import nltk
from nltk import PunktSentenceTokenizer as pk
from nltk.tokenize import WordPunctTokenizer
from pattern.fr.inflect import singularize
from pattern.fr import tokenize, parse
from nltk.stem import SnowballStemmer

import pickle
import locale

locale.setlocale(locale.LC_ALL, 'fra')

tker = pk()
tker = nltk.data.load('nltk:tokenizers/punkt/french.pickle')

stemmer = SnowballStemmer('french')
wpktk = WordPunctTokenizer()

frphrases = open('frphrases.txt', encoding='utf-8')

wset = set()
for phrase in frphrases:
    desc = phrase.split('\t')[1]
    #print (desc)
    # print (tker.sentences_from_text(text=desc))
    words = parse(desc)
    wset.update(words)

wlist = sorted(wset, key=locale.strxfrm)
wstems = [(word, singularize(word), stemmer.stem(word)) for word in wlist]

pass