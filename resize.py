#! /usr/bin/env python

#A Batch Image Resizer
#By Dave Fowler 2007: davefowler@gmail.com

"""Image Resizer"""

from PIL import Image
import glob, os, sys

resize_folder = 'resized'

maxW = float(sys.argv[1])
maxH = float(sys.argv[2])

for infile in glob.glob("*.jpeg"):
    file, ext = os.path.splitext(infile)
    if not os.path.exists( os.path.abspath(resize_folder) ):
        os.makedirs( os.path.abspath(resize_folder) )
    im = Image.open(infile)
    size = im.size
    #if maxW/size[0] < maxH/size[1]:
    #    newsize = (int(maxW), int(maxW/size[0]*size[1]))
    #else:
    #    newsize = (int(maxH/size[1]*size[0]), int(maxH))
    newsize = (int(maxW),int(maxH))
    im = im.resize(newsize, Image.ANTIALIAS)
    im.save(resize_folder + '/' + infile, "JPEG")