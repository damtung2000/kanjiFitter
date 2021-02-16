#Kanji fitter
import codecs
from os.path import abspath, dirname, join
from math import ceil
# row = input('Input row: ')
# col = input('Input col: ')
row = 20
col = 20
# texts = input('Input text: ')
# table = [['x' for y in range(int(row))] for x in range (int(col))]

texts = codecs.open(abspath(join(dirname(__file__), 'test.txt')),'r', 'UTF-8').read()
def split(word): 
    return list(word)
text = split(texts)

print(text)
totalLength = int(col)*int(row)
essay = texts.split('\r\n')
essay2 = []
for paragraph in essay:
    essay2.append(split(paragraph))
print(essay2)
print(len(essay2[0]))
blocksLeft = totalLength
totalRows = row
# TODO: accommodate Romanji characters
for paragraph in essay2:
    rows = ceil(len(paragraph)/col) # Round up the number
    nullBlocks = col - len(paragraph)%col
    pointer = 0
    found = 0    # check for ocurrences in each paragraph
    for char in paragraph:
        if (char == "、" or char == "。"):
            if (((paragraph.index(char,pointer)-found) % col) == 0):
                nullBlocks += 1 # add back an empty block
                found += 1 # count number of previous ocurrences to deduct
            pointer = paragraph.index(char,pointer) + 1
    blocksLeft -= nullBlocks
    totalRows -= rows
    print('Paragraph ', essay2.index(paragraph) + 1,': ', len(paragraph), ' blocks\n ', rows, ' rows\n ', nullBlocks, 'empty blocks\n ', totalRows, ' rows left\n ')
    
    

