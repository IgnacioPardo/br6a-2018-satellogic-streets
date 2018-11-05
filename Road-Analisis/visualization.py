from tools import *
from PIL import Image
import cv2
from random import randint

def scale(img, originalSize, fullSize, roadSize):

	new = Image.new("RGB", (fullSize, fullSize), 'black')

	print((fullSize, fullSize))

	roadblock = Image.new("RGB", (roadSize, roadSize), 'white')

	roadpxs = roadblock.load()

	for i in range(originalSize):
		for j in range(originalSize):
			#print((i*fullSize/roadSize, j*fullSize/roadSize))
			if img.getpixel((i, j)) == (255, 255, 255):
				#print((i*fullSize/roadSize, j*fullSize/roadSize))
				new.paste(roadblock, (int(i*fullSize/originalSize), int(j*fullSize/originalSize)))

	return new	


def predictionDepiction(t):
	
	prediction = 'images/image-{}.png'.format(t)
	pathToSave = 'tiles/tile-{}.bmp'.format(t)

	tile = scale(Image.open(prediction), 16, 512, 32)

	tile.save(pathToSave)


new = Image.new("RGB", (16, 16), 'black')

pxs = new.load()

for i in range(new.size[0]):
	for j in range(new.size[1]):
		if randint(0,8) == 1:
			pxs[i, j] = (255, 255, 255)

new.save('images/image-15.png')

predictionDepiction(15)


