from __future__ import division
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from PIL import Image
from random import choice, randint
import sys
from os.path import expanduser

mydir = expanduser("~/")
GenPath = mydir + "GitHub/crises-and-creativity/"

# Read image
file_names = ['Escher-Anima.jpg', 'OKeeffe_RedCanna.jpg',
        'Vermeer_Girl_with_a_pearl_earring.jpg', 'Dr-Martin-Luther-King1.jpg',
        'Dali_dream_caused_by_the_flight_of_a_bee.jpg']

for name in file_names:
    image = Image.open(GenPath + 'Art/' + name)

    #box = (100, 400, 2000, 2000)
    #image = image.crop(box)
    #image.show()

    # record the original shape
    arr = np.array(image)
    shape = arr.shape

    #print shape
    #sys.exit()

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

        for i in range(100000):

            x2 = 0
            y2 = 0
            x_r = randint(0, w-1)
            y_r = randint(0, h-1)
            color = image.getpixel( (x_r, y_r) )


            if np.random.binomial(1, 0.999) == 1:

                d0 = randint(0, 100)
                d1 = int(d0)
                d2 = int(d0)

                #d0 = color[0]
                #d1 = color[1]
                #d2 = color[2]

                x2 = choice([x_r - d0, x_r + d1])
                if x2 < 0: x2 = 0
                elif x2 >= w: x2 = w-1

                #d = randint(0, color[0])
                #d = color[0]
                y2 = choice([y_r - d0, y_r + d2])
                if y2 < 0: y2 = 0
                elif y2 >= h: y2 = h-1

                image.putpixel( (x2, y2), color)

            else:
                c1 = randint(0,256)
                c2 = randint(0,256)
                c3 = randint(0,256)
                image.putpixel( (x_r, y_r), (c1, c2, c3))

        plt.imshow(image)


    anim = animation.FuncAnimation(fig, nextFrame, frames=100, interval=100, blit=False)
    #plt.show()
    anim.save(GenPath + 'Results/gifs/image-erasure_'+name+'.gif', writer='imagemagick', fps=10)
    plt.close()
