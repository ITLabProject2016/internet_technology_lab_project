__author__ = 'kostis'

import os
import Image
import glob

#gets images from a dir recursively, resizes them to optimal width and copies them to a new dir

##################################
#change me to your pictures dir!!!!
DIR = "/home/kostis/Desktop/img/"

#story icons are saved at  "./populate_img/stories"  with width 100
#story point icons are saved at  "./populate_img/points"  with width 350

OUT_DIR = "./populate_img/stories"
opt_width = 100;
##################################

G = glob.glob(DIR+"*.jpg")
G1 = glob.glob(DIR+"*.png")
G2 = glob.glob(DIR+"*.JPEG")
G3 = glob.glob(DIR+"*.JPG")
G = G + G1 + G2 + G3

for filePath in G:

    file = open(filePath)
    img = Image.open(file)

    width = img.size[0]
    height = img.size[1]

    ratio = opt_width / float(width)

    width = int(width * ratio)
    height = int(height * ratio)

    img = img.resize([width,height])
    img.save(os.path.join(os.path.join(OUT_DIR, os.path.splitext(os.path.basename(filePath))[0]))+".jpg")
    print os.path.join(os.path.join(OUT_DIR, os.path.splitext(os.path.basename(filePath))[0]))+".jpg"

