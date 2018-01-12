from __future__ import division
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from PIL import Image
from random import randint
import sys
from os.path import expanduser

mydir = expanduser("~/")
GenPath = mydir + "GitHub/crises-and-creativity/"

# Read image
image1 = Image.open(GenPath + 'Art/Dali_dream_caused_by_the_flight_of_a_bee.jpg')#.convert('RGBA')

box = (1000, 1000, 1500, 1500)
image = image1.crop(box)
#image.show()

# record the original shape
arr = np.array(image)
shape = arr.shape

fig = plt.figure()
plt.axis('off')

h = shape[0]
w = shape[1]
ct = 0

# Function called for each successive animation frame:
def nextFrame(arg): # arg is the frame number
    global h, w, image, ct

    plt.cla()
    plt.axis('off')

    print ct
    ct += 1

    # Process every pixel
    for x in range(w):
        for y in range(h):

            x_r = randint(0, w-1)
            y_r = randint(0, h-1)

            #print x_r, y_r

            color = image.getpixel( (x_r, y_r) )

            if np.random.binomial(1, 0.1) == 1:
                image.putpixel( (x,y), color)

            #if color == (0, 0, 0) or color == (255, 255, 255): continue
            #if np.random.binomial(1, 0.1) == 1:
            #    if np.random.binomial(1, 0.5) == 1:
            #        image.putpixel( (x,y), (0, 0, 0))
            #    elif np.random.binomial(1, 0.5) == 1:
            #        image.putpixel( (x,y), (255, 255, 255))

    plt.imshow(image)

anim = animation.FuncAnimation(fig, nextFrame, frames=100, interval=0, blit=False)
#plt.show()
anim.save(GenPath + 'Results/gifs/image-erasure_DominanceReplacement.gif', writer='imagemagick', fps=2)
sys.exit()
