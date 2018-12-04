from tools import *
from PIL import Image
import cv2
from random import randint
import numpy as np

def scale(img, fullSize1, fullSize2, roadSize):

	#ratio = predSize#int(fullSize/roadSize)

	ratio = img.size[0]

	new = Image.new('1', (fullSize1, fullSize2), 'black')

	roadblock = Image.new('1', (roadSize, roadSize), 'white')

	roadpxs = roadblock.load()

	for i in range(img.size[0]):
		for j in range(img.size[1]):
			#print((i*fullSize/roadSize, j*fullSize/roadSize))
			#if img.getpixel((i, j)) == (255, 255, 255):
			if img.getpixel((i, j)) > 125:# and img.getpixel((i, j))[1] > 125 and img.getpixel((i, j))[2] > 125:
				#print((i*fullSize/roadSize, j*fullSize/roadSize))
				new.paste(roadblock, (int(i*fullSize1/img.size[0]), int(j*fullSize2/img.size[1])))

	return new	


def predictionDepiction(t):
	
	prediction = 'predictions/prediction-{}.bmp'.format(t)
	
	pathToSave = 'tiles/tile-{}.bmp'.format(t)

	#imageSize = Image.open('images/image_1.tif').size[0]
	predImage = Image.open(prediction)

	#predImage.save('tests/holaaaaaa.png')
	
	#input()

	roadSize = 32

	fullSize1 = predImage.size[0] * roadSize
	fullSize2 = predImage.size[1] * roadSize

	tile = scale(predImage, fullSize1, fullSize2, roadSize)

	tile.save(pathToSave)


#new = Image.new("RGB", (16, 16), 'black')
#
#pxs = new.load()
#
#for i in range(new.size[0]):
#	for j in range(new.size[1]):
#		if randint(0,8) == 1:
#			pxs[i, j] = (255, 255, 255)
#
#new.save('images/image-15.png')
#
#predictionDepiction(15)


