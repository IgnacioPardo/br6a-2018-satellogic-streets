from PIL import Image
from tools import *
from random import randint, choice
import os
from tqdm import tqdm
from location_tools import *
import numpy as np
import cv2
from giftWrapping import *

def loadTiles(path):
	ls = []

	refs = tileReferences(path)[1:]

	print(refs)

	for i in tqdm(range(len(os.listdir(os.getcwd()+'/images/'))-2)):
		image_filename = 'images/image-{}.jpg'.format(i)
		ls.append([Image.open(image_filename), refs[i]])
	return ls

def trueOuterPoints(path):

	coordinates = loadLocations(path)

	#latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	print(coordinates)

	print([coord[0] for coord in coordinates])
	print([coord[1] for coord in coordinates])
	print([coord[2] for coord in coordinates])
	print([coord[3] for coord in coordinates])

	maxLatTop = -34.515181#max([coord[0] for coord in coordinates])
	minLonTop = max([coord[1] for coord in coordinates])
	minLatDown = min([coord[2] for coord in coordinates])
	maxLonDown = min([coord[3] for coord in coordinates])

	print(maxLatTop) 
	print(minLonTop) 
	print(minLatDown)
	print(maxLonDown)

	full_Corner1 = [minLonTop,maxLatTop]
	full_Corner2 = [maxLonDown,maxLatTop]
	full_Corner3 = [maxLonDown,minLatDown]
	full_Corner4 = [minLonTop,minLatDown]

	return full_Corner1, full_Corner2, full_Corner3, full_Corner4

def boardSizeOlder(path):

	full_Corner1, full_Corner2, full_Corner3, full_Corner4 = outerPoints(path)

	W = coordinatesToMeters(full_Corner1, full_Corner2)
	H = coordinatesToMeters(full_Corner1, full_Corner4)

	return H, W

def createBoard(path, res):
	H = 10000
	W = 10000

	#H, W = giftWrappedBoardSize(path)

	print(H , W)

	return Image.new("RGB", (int(H * res), int(W * res)), "black")

def fitTiles(board, tiles, res):
	for tile in tiles:
		board.paste(tile[0], (int(tile[1][1] * res), int(tile[1][0] * res)))
	return board

georeferencesPath = '/images/georeferences.csv'


trueOuterPoints(georeferencesPath)


#print(coordinatesToMeters(op[0], op[1]))
#print(coordinatesToMeters(op[0], ['58.515015', '34.518070']))

res = 20/95

tiles = loadTiles(georeferencesPath) 

board = createBoard(georeferencesPath, res) 

board.save('tests/board.png')

premap = fitTiles(board, tiles, res)

premap.save('tests/stitched.png')

#print(a.shape)

#cv2.imshow('Stitched', a)
