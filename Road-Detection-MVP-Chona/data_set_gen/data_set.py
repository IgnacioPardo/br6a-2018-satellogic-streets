from __future__ import print_function
import sys
from flask import Flask
import PIL
from PIL import Image
import csv


app = Flask(__name__)

@app.route('/')

def main():

	roadList = []
	notRoadList = []
	
	front = Image.open('layer.png')
	back = Image.open('back.png')
	print(front.getcolors(), file=sys.stderr)
	for i in range(front.size[0]):
		for j in range(front.size[1]):	 
			#if not front.getpixel((i, j)) == (255, 255, 255, 0):
			#	if not front.getpixel((i, j)) == (0, 0, 0, 0):
			#		print(front.getpixel((i, j)), file=sys.stderr)
			if front.getpixel((i, j)) == (255, 255, 255, 255):
				#print(((i, j), 1), file=sys.stderr)
				roadList.append(back.getpixel((i, j)))
			if front.getpixel((i, j)) == (0, 0, 0, 255):
				#print(((i, j), 0), file=sys.stderr)
				notRoadList.append(back.getpixel((i, j)))


	return ":".join([str(x) for x in roadList]) + '<br>' + ":".join([str(x) for x in notRoadList])