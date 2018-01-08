#!/bin/python
from PIL import Image
import glob
import os

path = raw_input('Enter your path:')
bb = str(path)+"/*.png"
filenamewpath = glob.glob(bb)
leng = len(filenamewpath)

if leng = 0:
		print "Did you get the path right? Looks like no PNG was found."

elif leng >= 1:
	for i in range(0, leng):
		filename = filenamewpath[i].split("/")[-1]

		im = Image.open(str(filenamewpath[i]))
		rgb_im = im.convert('RGB')
		rgb_im.save(str(path)+"/"+str(filename.split(".")[0])+'.jpg')
	print str(leng)+" image(s) converted to JPG."

# 	os.popen("rm *.png")
