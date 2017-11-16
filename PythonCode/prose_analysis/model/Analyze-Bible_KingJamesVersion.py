from __future__ import division
from os.path import expanduser
import pandas as pd
import json
import ast
import sys

mydir = expanduser("~/")
GenPath = mydir + "GitHub/crises-and-creativity/"

def GetRAD(vector):
    RAD = []
    unique = list(set(vector))
    for val in unique: RAD.append(vector.count(val))
    return RAD, unique



wp_df = pd.read_csv(GenPath + 'Literature/Bible_KingJamesVersion/Bible_KingJamesVersion-Act-words.txt', sep='\t')
# labels = ['book', 'chapter', 'verse_order', 'sentence_order', 'word_order', 'word=1', 'word_or_punct']
#print list(WP_df),'\n'
#print WP_df.iloc[0]

w_df = wp_df[wp_df['word=1'] == 1]
words = w_df['word_or_punct']
#print len(w_df['word_or_punct'])
p_df = wp_df[wp_df['word=1'] == 0]
pmarks = p_df['word_or_punct']
#print len(p_df['word_or_punct'])
