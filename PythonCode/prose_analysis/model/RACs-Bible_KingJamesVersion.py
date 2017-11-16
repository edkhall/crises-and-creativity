from __future__ import division
import  matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde
from os.path import expanduser
from random import randint
import pandas as pd
import numpy as np
import json
import ast
import sys
import os


mydir = expanduser("~/")
GenPath = mydir + "GitHub/crises-and-creativity/"

def get_kdens_choose_kernel(_list,kernel):
    """ The kernel density function across a list of numbers """
    density = gaussian_kde(_list)
    n = min([100, len(_list)])
    xs = np.linspace(min(_list), max(_list), n)
    density.covariance_factor = lambda : kernel
    density._compute_covariance()
    D = [xs,density(xs)]
    return D

def GetRAD(vector):
    RAD_freqs = []
    RAD_lengths = []
    w2n = []
    lengths = []
    unique = list(set(vector))
    for val in unique:
        RAD_freqs.append(vector.count(val))

    for i in vector:
        lengths.append(len(i))
        w2n.append(unique.index(i))

    unique_lengths = list(set(lengths))
    for val in unique_lengths:
        RAD_lengths.append(lengths.count(val)) # occurrence of a word of a given length

    return RAD_freqs, RAD_lengths, unique, lengths, w2n

W2N = []
Lengths = []
RAC_F = []
RAC_L = []
clist = []
Names = []

names = []
for name in os.listdir(GenPath + 'Literature/Bible_KingJamesVersion/words'):
    names.append(name)

namesDict = {}
namesDict['Bible_KingJamesVersion-Gen-words.txt'] = {'name' : 'Genesis'}
namesDict['Bible_KingJamesVersion-Exo-words.txt'] = {'name' : 'Exodus'}
namesDict['Bible_KingJamesVersion-Lev-words.txt'] = {'name' : 'Leviticus'}
namesDict['Bible_KingJamesVersion-Num-words.txt'] = {'name' : 'Numbers'}
namesDict['Bible_KingJamesVersion-Deu-words.txt'] = {'name' : 'Deuteronomy'}
namesDict['Bible_KingJamesVersion-Jos-words.txt'] = {'name' : 'Joshua'}
namesDict['Bible_KingJamesVersion-Jdg-words.txt'] = {'name' : 'Judges'}
namesDict['Bible_KingJamesVersion-Rut-words.txt'] = {'name' : 'Ruth'}
namesDict['Bible_KingJamesVersion-Sa1-words.txt'] = {'name' : '1 Samuel'}
namesDict['Bible_KingJamesVersion-Sa2-words.txt'] = {'name' : '2 Samuel'}
namesDict['Bible_KingJamesVersion-Kg1-words.txt'] = {'name' : '1 Kings'}
namesDict['Bible_KingJamesVersion-Kg2-words.txt'] = {'name' : '2 Kings'}
namesDict['Bible_KingJamesVersion-Ch1-words.txt'] = {'name' : '1 Chronicles'}
namesDict['Bible_KingJamesVersion-Ch2-words.txt'] = {'name' : '2 Chronicles'}
namesDict['Bible_KingJamesVersion-Ezr-words.txt'] = {'name' : 'Ezra'}
namesDict['Bible_KingJamesVersion-Neh-words.txt'] = {'name' : 'Nehemiah'}
namesDict['Bible_KingJamesVersion-Est-words.txt'] = {'name' : 'Esther'}
namesDict['Bible_KingJamesVersion-Job-words.txt'] = {'name' : 'Job'}
namesDict['Bible_KingJamesVersion-Psa-words.txt'] = {'name' : 'Psalms'}
namesDict['Bible_KingJamesVersion-Pro-words.txt'] = {'name' : 'Proverbs'}
namesDict['Bible_KingJamesVersion-Ecc-words.txt'] = {'name' : 'Ecclesiastes'}
namesDict['Bible_KingJamesVersion-Sol-words.txt'] = {'name' : 'Song of Solomon'}
namesDict['Bible_KingJamesVersion-Isa-words.txt'] = {'name' : 'Isaiah'}
namesDict['Bible_KingJamesVersion-Jer-words.txt'] = {'name' : 'Jeremiah'}
namesDict['Bible_KingJamesVersion-Lam-words.txt'] = {'name' : 'Lamentations'}
namesDict['Bible_KingJamesVersion-Eze-words.txt'] = {'name' : 'Ezekiel'}
namesDict['Bible_KingJamesVersion-Dan-words.txt'] = {'name' : 'Daniel'}
namesDict['Bible_KingJamesVersion-Hos-words.txt'] = {'name' : 'Hosea'}
namesDict['Bible_KingJamesVersion-Joe-words.txt'] = {'name' : 'Joel'}
namesDict['Bible_KingJamesVersion-Amo-words.txt'] = {'name' : 'Amos'}
namesDict['Bible_KingJamesVersion-Oba-words.txt'] = {'name' : 'Obadiah'}
namesDict['Bible_KingJamesVersion-Jon-words.txt'] = {'name' : 'Jonah'}
namesDict['Bible_KingJamesVersion-Mic-words.txt'] = {'name' : 'Micah'}
namesDict['Bible_KingJamesVersion-Nah-words.txt'] = {'name' : 'Nahum'}
namesDict['Bible_KingJamesVersion-Hab-words.txt'] = {'name' : 'Habakkuk'}
namesDict['Bible_KingJamesVersion-Zep-words.txt'] = {'name' : 'Zephaniah'}
namesDict['Bible_KingJamesVersion-Hag-words.txt'] = {'name' : 'Haggai'}
namesDict['Bible_KingJamesVersion-Zac-words.txt'] = {'name' : 'Zechariah'}
namesDict['Bible_KingJamesVersion-Mal-words.txt'] = {'name' : 'Malachi'}
namesDict['Bible_KingJamesVersion-Mat-words.txt'] = {'name' : 'Matthew'}
namesDict['Bible_KingJamesVersion-Mar-words.txt'] = {'name' : 'Mark'}
namesDict['Bible_KingJamesVersion-Luk-words.txt'] = {'name' : 'Luke'}
namesDict['Bible_KingJamesVersion-Joh-words.txt'] = {'name' : 'John'}
namesDict['Bible_KingJamesVersion-Act-words.txt'] = {'name' : 'Acts'}
namesDict['Bible_KingJamesVersion-Rom-words.txt'] = {'name' : 'Romans'}
namesDict['Bible_KingJamesVersion-Co1-words.txt'] = {'name' : '1 Corinthians'}
namesDict['Bible_KingJamesVersion-Co2-words.txt'] = {'name' : '2 Corinthians'}
namesDict['Bible_KingJamesVersion-Gal-words.txt'] = {'name' : 'Galatians'}
namesDict['Bible_KingJamesVersion-Eph-words.txt'] = {'name' : 'Ephesians'}
namesDict['Bible_KingJamesVersion-Phi-words.txt'] = {'name' : 'Philippians'}
namesDict['Bible_KingJamesVersion-Col-words.txt'] = {'name' : 'Colossians'}
namesDict['Bible_KingJamesVersion-Th1-words.txt'] = {'name' : '1 Thessalonians'}
namesDict['Bible_KingJamesVersion-Th2-words.txt'] = {'name' : '2 Thessalonians'}
namesDict['Bible_KingJamesVersion-Ti1-words.txt'] = {'name' : '1 Timothy'}
namesDict['Bible_KingJamesVersion-Ti2-words.txt'] = {'name' : '2 Timothy'}
namesDict['Bible_KingJamesVersion-Tit-words.txt'] = {'name' : 'Titus'}
namesDict['Bible_KingJamesVersion-Plm-words.txt'] = {'name' : 'Philemon'}
namesDict['Bible_KingJamesVersion-Heb-words.txt'] = {'name' : 'Hebrews'}
namesDict['Bible_KingJamesVersion-Jam-words.txt'] = {'name' : 'James'}
namesDict['Bible_KingJamesVersion-Pe1-words.txt'] = {'name' : '1 Peter'}
namesDict['Bible_KingJamesVersion-Pe2-words.txt'] = {'name' : '2 Peter'}
namesDict['Bible_KingJamesVersion-Jo1-words.txt'] = {'name' : '1 John'}
namesDict['Bible_KingJamesVersion-Jo2-words.txt'] = {'name' : '2 John'}
namesDict['Bible_KingJamesVersion-Jo3-words.txt'] = {'name' : '3 John'}
namesDict['Bible_KingJamesVersion-Jde-words.txt'] = {'name' : 'Jude'}
namesDict['Bible_KingJamesVersion-Rev-words.txt'] = {'name' : 'Revelation'}


for name in os.listdir(GenPath + 'Literature/Bible_KingJamesVersion/words'):
    Names.append(namesDict[name]['name'])
    wp_df = pd.read_csv(GenPath + 'Literature/Bible_KingJamesVersion/words/'+name, sep='\t')
    # labels = ['book', 'chapter', 'verse_order', 'sentence_order', 'word_order', 'word=1', 'word_or_punct']

    w_df = wp_df[wp_df['word=1'] == 1]
    words = w_df['word_or_punct'].tolist()
    RAD_freqs, RAD_lengths, unique, lengths, w2n = GetRAD(words)

    Lengths.append(lengths)
    W2N.append(w2n)
    RAC_F.append(RAD_freqs)
    RAC_L.append(RAD_lengths)

    r = lambda: randint(0,255)
    clr = '#%02X%02X%02X' % (r(),r(),r())
    while clr in clist:
        r = lambda: randint(0,255)
        clr = '#%02X%02X%02X' % (r(),r(),r())
    clist.append(clr)

kernel = 0.4
fig = plt.figure()

fig.add_subplot(2, 2, 1)
for i, j in enumerate(W2N):
    D = get_kdens_choose_kernel(j, kernel)
    if Names[i] == 'Genesis': plt.plot(D[0], np.log10(D[1]), color = 'k', lw=1, label=Names[i])
    else: plt.plot(D[0], np.log10(D[1]), color = clist[i], lw=0.5, alpha=0.5, label=Names[i])

plt.xlabel('Occurrence of a word', fontsize=8)
plt.ylabel('Density'+r'$log_{10}$', fontsize=8)
plt.tick_params(axis='both', labelsize=5)

plt.legend(bbox_to_anchor=(-0.02, 1.05, 2.38, 0.7), loc=10, ncol=5, mode="expand", prop={'size':4})
#frame = legend.get_frame()
#frame.set_edgecolor('k')

fig.add_subplot(2, 2, 2)
for i, j in enumerate(Lengths):
    D = get_kdens_choose_kernel(j, kernel)
    if Names[i] == 'Genesis': plt.plot(D[0], D[1], color = 'k', lw=1)
    else: plt.plot(D[0], D[1], color = clist[i], lw=0.5, alpha=0.5)

plt.xlabel('Length of a word', fontsize=8)
plt.ylabel('Density', fontsize=8)
plt.tick_params(axis='both', labelsize=5)

maxx = 0
fig.add_subplot(2, 2, 3)
for i, j in enumerate(RAC_F):
    j.sort(reverse=True)
    if max(j) > maxx: maxx = max(j)
    ranks = range(len(j))

    if Names[i] == 'Genesis': plt.plot(ranks, np.log10(j), color = 'k', lw=1)
    else: plt.plot(ranks, np.log10(j), color = clist[i], lw=0.5, alpha=0.5)

plt.xlabel('Rank in occurrence of a word', fontsize=8)
plt.ylabel('Occurrence of a word, '+r'$log_{10}$', fontsize=8)
plt.ylim(-0.1, np.log10(maxx))
plt.tick_params(axis='both', labelsize=5)

maxx = 0
fig.add_subplot(2, 2, 4)
for i, j in enumerate(RAC_L):
    j.sort(reverse=True)
    if max(j) > maxx: maxx = max(j)
    ranks = range(len(j))
    if Names[i] == 'Genesis': plt.plot(ranks, np.log10(j), color = 'k', lw=1)
    else: plt.plot(ranks, np.log10(j), color = clist[i], lw=0.5, alpha=0.5)

plt.xlabel('Rank', fontsize=8)
plt.ylabel('Occurrence of words with\na given length, '+r'$log_{10}$', fontsize=8)
plt.ylim(-0.1, np.log10(maxx))
plt.tick_params(axis='both', labelsize=5)


#### Final Format and Save #####################################################
plt.subplots_adjust(wspace=0.35, hspace=0.35)
plt.savefig(GenPath + '/Results/Figures/RACs-word_frequency-word_length.png', dpi=400, bbox_inches = "tight")

plt.close()
