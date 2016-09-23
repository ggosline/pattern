import nltk

frphrases = open('frphrases.txt', encoding='utf-8')

for phrase in frphrases:
    desc = phrase.split('\t')[1]
    print (desc)