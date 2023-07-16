# Kanji fitter
import codecs
from operator import concat
from os import remove
import string
from os.path import abspath, dirname, join
from math import ceil
from typing import List, Sequence

# row = input('Input row: ')
# col = input('Input col: ')
row = 20
col = 20
# texts = input('Input text: ')
# table = [['x' for y in range(int(row))] for x in range (int(col))]

texts = codecs.open(abspath(join(dirname(__file__), "test.txt")), "r", "UTF-8").read()


# text = list(texts)

# print(text)
totalLength = int(col) * int(row)
essay = texts.split("\r\n")
essay.remove("")
listOfParagraphs = list(map(lambda paragraph: list(paragraph), essay))

print(listOfParagraphs)
# print(len(listOfParagraphs[0]))
blocksLeft = totalLength
rowsLeft = row
# TODO: accommodate Romanji characters
alphabetLowerCase = list(string.ascii_lowercase)
alphabetUpperCase = list(string.ascii_uppercase)
romanjiAlphabet = concat(alphabetLowerCase, alphabetUpperCase)

for paragraph in listOfParagraphs:
    rowsTaken = ceil(len(paragraph) / col)  # Round up the number
    emptyBlocks = col - len(paragraph) % col
    pointer = 0
    found = 0  # check for ocurrences in each paragraph
    for char in paragraph:
        if char == "、" or char == "。":
            if ((paragraph.index(char, pointer) - found) % col) == 0:
                emptyBlocks += 1  # add back an empty block
                found += 1  # count number of previous ocurrences to deduct
            pointer = paragraph.index(char, pointer) + 1
        if char in romanjiAlphabet:
            print("alpha found")
    blocksLeft -= emptyBlocks
    rowsLeft -= rowsTaken
    print(
        "Paragraph ",
        listOfParagraphs.index(paragraph) + 1,
        ": ",
        len(paragraph),
        " blocks\n ",
        rowsTaken,
        " rows\n ",
        emptyBlocks,
        "empty blocks\n ",
        rowsLeft,
        " rows left\n ",
    )
