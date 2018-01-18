from __future__ import division
import matplotlib.pyplot as plt
from matplotlib import transforms
from random import choice, shuffle
import pandas as pd
import numpy as np
import sys
from os.path import expanduser
import re


mydir = expanduser("~/")
GenPath = mydir + "GitHub/crises-and-creativity/"


def GetRAD(v1):
    v2 = []
    for i in v1: v2.append(i.lower())
    RAD, unique = [], list(set(v2))
    for val in unique: RAD.append(v2.count(val))
    RAD, unique = zip(*sorted(zip(RAD, unique)))
    return RAD, unique


def color_text(x, y, ls, lc, **kw):
    t = plt.gca().transData
    fig = plt.gcf()
    plt.axis([0, 10, 0, 10])
    plt.axis('off')

    for i, (s, c) in enumerate(zip(ls, lc)):
        punc = ['.', ',', ':', ';']
        if s in punc:
            text = plt.text(x, y, s+" ", color=c, transform=t, **kw)
        elif i < len(ls)-1 and ls[i+1] in punc:
            text = plt.text(x, y, s, color=c, transform=t, **kw)
        else:
            text = plt.text(x, y, s+" ", color=c, transform=t, **kw)

        text.draw(fig.canvas.get_renderer())
        ex = text.get_window_extent()
        t = transforms.offset_copy(text._transform, x=ex.width*2, units='dots')

    return fig


wp_df = pd.read_csv(GenPath + 'Literature/Bible_KingJamesVersion/words/Bible_KingJamesVersion-Gen-words.txt', sep='\t')
# labels = ['book', 'chapter', 'verse_order', 'sentence_order', 'word_order', 'word=1', 'word_or_punct']

w_df = wp_df[wp_df['chapter'] == 1]
w_df = w_df[w_df['verse_order'] < 11]
w_df['word_or_punct'] = w_df['word_or_punct'].replace(['.'], '. ')
w_df['word_or_punct'] = w_df['word_or_punct'].replace([','], ', ')
w_df['word_or_punct'] = w_df['word_or_punct'].replace([';'], '; ')
w_df['word_or_punct'] = w_df['word_or_punct'].replace([':'], ': ')

text = w_df['word_or_punct'].tolist()

#print len(text), len(text2), '\n', text2, '\n', RAD
#sys.exit()

text = [[''.join(i)] for i in text]
text = ''.join(i[0] for i in text)
text = re.split(r'(\s+)', text)


punc = ['.', ',', ':', ';']
t2 = []
for i, e in enumerate(text):
    if i < len(text)-1 and text[i+1] not in punc and e != ' ':
        t2.append(e)

text = t2
colors = ['black']*len(text)

RAD, text2 = GetRAD(text)


l = 0
j = 0
text1 = [[]]
clrs1 = [[]]
for ii, t in enumerate(text):
    text1[j].append(t)
    clrs1[j].append(colors[ii])
    l += len(t)
    if l > 55:
        l = 0
        j += 1
        text1.append([])
        clrs1.append([])

y = 10
for line_i, lin in enumerate(text1):
    fig = color_text(-1.1, y, lin, clrs1[line_i], size=10)
    y -= 0.6

plt.savefig(GenPath + 'Results/prose_images/Genesis-image-all-prose.png', dpi=200)
plt.close()


last_word = str()
for i, word in enumerate(text2):

    #if i == 10: break

    for ii, char in enumerate(text):
        if char.lower() == word:
            colors[ii] = 'white'

    l = 0
    j = 0
    text1 = [[]]
    clrs1 = [[]]
    for ii, t in enumerate(text):
        text1[j].append(t)
        clrs1[j].append(colors[ii])
        l += len(t)
        if l > 55:
            l = 0
            j += 1
            text1.append([])
            clrs1.append([])

    y = 10
    for line_i, lin in enumerate(text1):
        fig = color_text(-1.1, y, lin, clrs1[line_i], size=10)
        y -= 0.6

    plt.savefig(GenPath + 'Results/prose_images/Genesis-image-removal_of_rank_'+str(len(text2) - i)+'-'+word +'.png', dpi=200)
    plt.close()
