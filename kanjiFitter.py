#Kanji fitter
import codecs
from math import ceil
# row = input('Input row: ')
# col = input('Input col: ')
row = 20
col = 20
# texts = input('Input text: ')
# table = [['x' for y in range(int(row))] for x in range (int(col))]
texts = codecs.open('test.txt','r', 'UTF-8').read()
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
for paragraph in essay2:
    rows = ceil(len(paragraph)/col)
    nullBlocks = col - len(paragraph)%col
    blocksLeft -= nullBlocks
    totalRows -= rows
    print('Paragraph ', essay2.index(paragraph),': ', len(paragraph), ' blocks\n ', rows, ' rows\n ', nullBlocks, 'empty blocks\n ', totalRows, ' rows left\n ')
    
    

