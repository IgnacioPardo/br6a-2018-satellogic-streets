from PIL import Image
from tools import *
from random import randint, choice
import os
from tqdm import tqdm
from location_tools import *

def loadTiles():
	ls = []

	refs = tileReferences('images/georeferences.csv')

	for i in tqdm(range(len(os.listdir(os.getcwd()+'/tiles/'))-3)):
		image_filename = 'tiles/tile-{}.bmp'.format(i)
		ls.append([Image.open(image_filename), locations[i]])
	return ls

def boardSize(path):

	full_Corner1, full_Corner2, full_Corner3, full_Corner4 = outerPoints(path)

	W = coordinatesToMeters(full_Corner1, full_Corner2)
	H = coordinatesToMeters(full_Corner1, full_Corner4)

	return H, W

def createBoard():
	H = 0
	W = 0

	H, W = boardSize('/dataset/georeferences.csv')

	return Image.new("RGB", (int(H), int(W)), "black")

def fitTiles(board, tiles):
	for tile in tiles:
		board.paste(tile[0], (int(tile[1][1]), int(tile[1][0])))

	return board