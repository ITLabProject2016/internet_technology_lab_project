__author__ = 'kostis'

import os
import Image
import glob

#gets images from a dir recursively, resizes them to optimal width and copies them to a new dir

##################################
#change me!!!!
DIR = "/home/kostis/Desktop/"
OUT_DIR = "./populate"
opt_width = 300;
##################################

G = glob.glob(DIR+"*.jpg")
G1 = glob.glob(DIR+"*.png")
G2 = glob.glob(DIR+"*.JPEG")
G = G + G1 + G2

for filePath in G:

    file = open(filePath)
    img = Image.open(file)

    width = img.size[0]
    height = img.size[1]

    ratio = opt_width / float(width)

    width = int(width * ratio)
    height = int(height * ratio)

    img = img.resize([width,height])
    img.save(os.path.join(OUT_DIR, os.path.basename(filePath)))
    print os.path.join(OUT_DIR, os.path.basename(filePath))

