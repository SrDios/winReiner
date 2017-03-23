
from PIL import ImageGrab
#from PIL import ImageOps
import os
#import code
import time

# Globals
# ------------------

x_pad = 455 #You should find your own game grid
y_pad = 30

def screenGrab():
    limits = (x_pad+1, y_pad+1,x_pad+367,y_pad+655) #where i should take the snapshopt?
    im = ImageGrab.grab(limits)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def screenGrab2():
    limits = (x_pad+1, y_pad+1,x_pad+367,y_pad+655)
    im = ImageGrab.grab(limits)
    #print(im.getpixel(code.Cord.c_rectangle))
    #print(im.getpixel(code.Cord.s_blue))
    #print(im.getpixel(code.Cord.s_green))
    #print(im.getpixel(code.Cord.s_magenta))
    #print(im.getpixel(code.Cord.s_yellow))

    return im

def main():
    screenGrab2()


if __name__ == '__main__':
    main()