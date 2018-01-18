from __future__ import division

import matplotlib.pyplot as plt
from matplotlib import transforms
import matplotlib.animation as animation

from random import choice, shuffle
import pandas as pd
import numpy as np
import sys
from os.path import expanduser
import re


mydir = expanduser("~/")
GenPath = mydir + "GitHub/crises-and-creativity/"


def color_text(fig, x, y, ls, lc, **kw):
    t = plt.gca().transData
    fig = plt.gcf()

    for s,c in zip(ls,lc):
        text = plt.text(x,y," "+s+" ",color=c, transform=t, **kw)
        text.draw(fig.canvas.get_renderer())
        ex = text.get_window_extent()
        t = transforms.offset_copy(text._transform, x=ex.width, units='dots')

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
text = [[''.join(i)] for i in text]
text = ''.join(i[0] for i in text)

t = plt.gca().transData
fig = plt.gcf()
plt.axis([0, 10, 0, 10])
plt.axis('off')

text = re.split(r'(\s+)', text)
colors = ['black']*len(text)
inds = []
ct = 0

indices = [i for i, x in enumerate(text) if x.count(' ') == 0]
indices = [e for e in indices if e not in (22, 24, 26, 28, 38)]
shuffle(indices)
indices.extend([22, 24, 26, 28, 38])
framz = len(indices)-1

# Function called for each successive animation frame:
def nextFrame(arg):		   # arg is the frame number
    global text, fig, colors, ct, swtch

    plt.cla()
    plt.axis('off')

    if len(indices) == 0: return

    i = indices.pop(0)
    inds.append(i)
    colors[i] = 'white'

    l = 0
    j = 0
    text1 = [[]]
    clrs1 = [[]]
    for i, t in enumerate(text):
        text1[j].append(t)
        clrs1[j].append(colors[i])
        l += len(t)
        if l > 55:
            l = 0
            j += 1
            text1.append([])
            clrs1.append([])

    y = 10
    for i, t in enumerate(text1):
        fig = color_text(fig, -1.1, y, t, clrs1[i], size=12)
        y -= 0.6

    print ct
    ct += 1


anim = animation.FuncAnimation(fig, nextFrame, frames=framz, interval=0, blit=False)
#plt.show()
anim.save(GenPath + 'video.gif', writer='imagemagick', fps=2)
sys.exit()
