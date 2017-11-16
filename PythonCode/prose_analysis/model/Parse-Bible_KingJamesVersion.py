from __future__ import division
from os.path import expanduser
import json
import nltk
from nltk import tokenize
import re
import sys

mydir = expanduser("~/")
GenPath = mydir + "GitHub/crises-and-creativity/"

TEXT = open(GenPath + 'Literature/Bible_KingJamesVersion/Bible_KingJamesVersion.txt', 'r')
vs, ss, ws = 0, 0, 0
books = []

for line in TEXT:
    line = line.strip('\n')
    m = re.search('\A\w+\W\d+\W\d+\W\s+', line)
    verse_lab = m.group(0)

    verse = line.strip(verse_lab)
    verse_lab = verse_lab.strip(' ')
    verse_lab = verse_lab.replace('|', ':')
    verse_lab = verse_lab[:-1]
    book, chapter, verse_num = verse_lab.split(':')

    if book not in books:
        books.append(book)
        wOUT = open(GenPath + 'Literature/Bible_KingJamesVersion/words/Bible_KingJamesVersion-'+book+'-words.txt', 'w+')
        col_headers = 'book\tchapter\tverse_order\tsentence_order\tword_order\tword=1\tword_or_punct\tword_class'
        print>>wOUT, col_headers
        wOUT.close()
        sOUT = open(GenPath + 'Literature/Bible_KingJamesVersion/sentences/Bible_KingJamesVersion-'+book+'-sentences.txt', 'w+')
        col_headers = 'book\tchapter\tverse_order\tsentence_order\tsentence'
        print>>sOUT, col_headers
        sOUT.close()
        vOUT = open(GenPath + 'Literature/Bible_KingJamesVersion/verses/Bible_KingJamesVersion-'+book+'-verses.txt', 'w+')
        col_headers = 'book\tchapter\tverse_order'
        print>>vOUT, col_headers
        vOUT.close()

    wOUT = open(GenPath + 'Literature/Bible_KingJamesVersion/words/Bible_KingJamesVersion-'+book+'-words.txt', 'a+')
    sOUT = open(GenPath + 'Literature/Bible_KingJamesVersion/sentences/Bible_KingJamesVersion-'+book+'-sentences.txt', 'a+')
    vOUT = open(GenPath + 'Literature/Bible_KingJamesVersion/verses/Bible_KingJamesVersion-'+book+'-verses.txt', 'a+')

    print>>vOUT, book,'\t',verse_num,'\t',verse
    vs += 1

    sentences = tokenize.sent_tokenize(verse)
    for i, sentence in enumerate(sentences):
        ss += 1
        print>>sOUT, book,'\t',chapter,'\t',verse_num,'\t',i+1,'\t',sentence

        words_and_punct = tokenize.word_tokenize(sentence)
        for j, word_or_punct in enumerate(words_and_punct):

            if word_or_punct in [',','.', '?', '!', ':',';','\'','\"','(',')','[','[','{','}','#','^','&','\'s']:
                print>>wOUT, book,'\t',chapter,'\t',verse_num,'\t',i+1,'\t',j+1,'\t',0,'\t',word_or_punct
            else:
                text = nltk.word_tokenize(word_or_punct)
                text = nltk.pos_tag(text)
                word = text[0][0]
                word_class = text[0][1]
                print>>wOUT, book,'\t',chapter,'\t',verse_num,'\t',i+1,'\t',j+1,'\t',1,'\t',word_or_punct,'\t',word_class
                ws += 1

    wOUT.close()
    sOUT.close()
    vOUT.close()


TEXT.close()
print "\nLines      : ", vs
print "Sentences  : ", ss
print "Words      : ", ws
