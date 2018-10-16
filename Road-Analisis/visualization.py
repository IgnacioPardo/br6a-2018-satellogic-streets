from tools import *
from PIL import Image
import cv2
from random import randint
	
def colorBlock(i, j, pxs, tup):
	for k in range(16):
		for q in range(16):
			pxs[i+k,j+q] = tup
	return pxs


def makeGrid(ls):

	#pxs = img.load()

	roadblock = Image.new("RGB", (16, 16), 'white')
	
	a = Image.new("RGB", (512, 512), 'black')

	#grid = range(0,512,16)

	#for e in range(1.024):
	#	a.paste(roadblock, (ls[e] * 16,))#(choice(grid), choice(grid)))

	#for e in ls:
	#	print(e, '\n')

	for i in range(0, 512,16):
		for j in range(0, 512,16):
			if (ls[int(i/16)][int(j/16)] == 1):
				#print(ls[int(i/16)][int(j/16)], (i, j))
				#a.paste(roadblock, (i, j))


	#a.save('tiles/tile-{}.bmp'.format(i))

	return a


def predictionDepiction(t):
	
	pathToImage = 'images/image-{}.png'.format(t)
	pathToSave = 'tiles/tile-{}.bmp'.format(t)

	#tile = Image.open(pathToImage)
	#prediction = open().read() #Archivo de Tomislav

	#Color predicted road blocks

	#prediction = [[randint(0,1) for a in range(32)] for a in range(32)]

	tile = makeGrid(prediction)

	tile.save(pathToSave)

#predictionDepiction(15)
