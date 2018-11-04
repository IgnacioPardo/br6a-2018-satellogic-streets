from PIL import Image
from tools import *
from random import randint, choice
import os
from tqdm import tqdm
from location_tools import *

def loadTiles():
	ls = []

	locations = coordinatesToPixels(loadLocations('/tiles/dataset_georeferences.csv'))

	if len(os.listdir(os.getcwd()+'/tiles/')) == 1:
		image_filename = 'tiles/tile-0.bmp'
		ls.append([Image.open(image_filename), None])
		return ls

	for i in tqdm(range(len(os.listdir(os.getcwd()+'/tiles/'))-3)):
		image_filename = 'tiles/tile-{}.bmp'.format(i)
		ls.append([Image.open(image_filename), locations[i]])
	return ls

def createBoard():
	H = 0
	W = 0
	#H = tiles[0][0].size[0] * sqrt(len(tiles))
	#W = tiles[0][0].size[1] * sqrt(len(tiles))

	H, W = boardSize('dataset/georeferences.csv')

	return Image.new("RGB", (int(H), int(W)), "black")

def fitTiles(board, tiles):

	#board = createBoard()

	#tiles = loadTiles()

	for tile in tiles:
		board.paste(tile[0], (tile[1][1], tile[1][0]))

	return board