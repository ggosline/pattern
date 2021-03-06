import nltk
from nltk import PunktSentenceTokenizer as pk
from nltk.tokenize import WordPunctTokenizer
from pattern.fr.inflect import singularize
# from pattern.fr import tokenize, parse
# from nltk.stem import SnowballStemmer

import pickle
import locale
from csv import DictReader

from glosbe1 import glosbe

locale.setlocale(locale.LC_ALL, 'fra')

tker = pk()
tker = nltk.data.load('nltk:tokenizers/punkt/french.pickle')

frengreader = DictReader(open('French-English-Lexicon.csv', encoding='windows-1252'))
frlexicon = {row['French']: row for row in frengreader}

# stemmer = SnowballStemmer('french')
wpktk = WordPunctTokenizer()

with  open('frphrases.txt', encoding='utf-8') as frphrases:

    wset = set()
    for phrase in frphrases:
        desc = phrase.split('\t')[1]
        #print (desc)
        # print (tker.sentences_from_text(text=desc))
        words = wpktk.tokenize(desc)
        wset.update([singularize(word) for word in words])

wlist = sorted(wset, key=locale.strxfrm)

wvocs = []
for word in wlist:
    if word and word.isalpha():
        frlexwrd = frlexicon.get(word)['English'] if frlexicon.get(word) else None
        glosbewrd = glosbe(word)
        wvocs.append((word, frlexwrd, glosbewrd[0] if glosbewrd else None))
        print (word, frlexwrd, glosbewrd[0] if glosbewrd else None)

with open('frwords.txt', mode='w', encoding='utf-8') as frwords:
    for wvoc in wvocs:
        print(wvoc[0], wvoc[1], wvoc[2] ,sep='\t', file=frwords)

pass