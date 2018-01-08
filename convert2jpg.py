#!/bin/python



from PIL import Image

import glob

import os



path = raw_input('Enter your path:')

bb = str(path)+"/*.png"

filenamewpath = glob.glob(bb)

leng = len(filenamewpath)



if len(filenamewpath) <= 0:

		print "Did you get the path right? Looks like no PNG was found."



for i in range(0, len(filenamewpath)):

	filename = filenamewpath[i].split("/")[-1]

	#print filenamewpath



	im = Image.open(str(filenamewpath[i]))

	rgb_im = im.convert('RGB')

	rgb_im.save(str(path)+"/"+str(filename.split(".")[0])+'.jpg')



if leng >= 1:	

	print str(leng)+" image(s) converted to JPG."



# 	os.popen("rm *.png")
