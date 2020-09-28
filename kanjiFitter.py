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
pointer = 0
for paragraph in essay2:
    rows = ceil(len(paragraph)/col)
    nullBlocks = col - len(paragraph)%col
    for char in paragraph:
        if (char == "、" or char == "。") and ((paragraph.index(char,pointer) % col) == 0):
            nullBlocks+=1
            pointer = paragraph.index(char,pointer)
    blocksLeft -= nullBlocks
    totalRows -= rows
    print('Paragraph ', essay2.index(paragraph) + 1,': ', len(paragraph), ' blocks\n ', rows, ' rows\n ', nullBlocks, 'empty blocks\n ', totalRows, ' rows left\n ')
    
    

