import xml.etree.cElementTree as ET
import csv

tree = ET.ElementTree(file='fdgvol29_final.xml')
root = tree.getroot()

taxa = root.findall('.//taxon')
frphrases = open("frphrases.txt", mode='w', encoding='utf-8')

for taxon in taxa:
    taxonnames = taxon.findall('nomenclature/homotypes/nom[@class="accepted"]/name')
    # print(taxonname.findtext('name[@class="genus"]'), taxonname.findtext('name[@class="species"]'))
    for namepart in taxonnames:
        print (namepart.get('class'), namepart.text)
    description = taxon.find('feature[@class="description"]')
    if description:
        for char in description.findall('char'):
            print(char.get('class'), '\t', " ".join(list(txt.strip() for txt in char.itertext())), file=frphrases)

frphrases.close()
# frenlex = open(r'C:\Users\gg12kg\PycharmProjects\pattern\French-English-Lexicon.csv')
#
# fr_en_lex = csv.DictReader(frenlex)
#
# frlex = [row for row in fr_en_lex]

pass


