from tools import *
from PIL import Image
import cv2
from random import randint

def scale(img, fullSize, roadSize):

	#ratio = predSize#int(fullSize/roadSize)

	ratio = img.size[0]

	new = Image.new("RGB", (fullSize, fullSize), 'black')

	print((fullSize, fullSize))

	roadblock = Image.new("RGB", (roadSize, roadSize), 'white')

	roadpxs = roadblock.load()

	for i in range(ratio):
		for j in range(ratio):
			#print((i*fullSize/roadSize, j*fullSize/roadSize))
			if img.getpixel((i, j)) == (255, 255, 255):
				#print((i*fullSize/roadSize, j*fullSize/roadSize))
				new.paste(roadblock, (int(i*fullSize/ratio), int(j*fullSize/ratio)))

	return new	


def predictionDepiction(t):
	
	prediction = 'predictions/prediction-{}.png'.format(t)
	pathToSave = 'tiles/tile-{}.bmp'.format(t)

	#imageSize = Image.open('images/image_1.tif').size[0]
	predImage = Image.open(prediction)
	roadSize = 128
	fullSize = predImage.size[0] * roadSize


	tile = scale(predImage, fullSize, roadSize)

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


