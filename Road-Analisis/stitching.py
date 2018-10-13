from PIL import Image
from tools import *
from random import randint, choice
import os

def loadTiles():
	ls = []
	for i in range(len(os.listdir(os.getcwd()+'/tiles/'))-3):
		image_filename = 'tiles/tile-{}.bmp'.format(i)
		ls.append([Image.open(image_filename), ])
	return ls

def createBoard(tiles):
	H = 0
	W = 0
	H = tiles[0][0].size[0] * sqrt(len(tiles))
	W = tiles[0][0].size[1] * sqrt(len(tiles))

	return Image.new("RGB", (int(H), int(W)), "black")

def fitTiles(board, tiles):

	grid = range(0,board.size[0],tiles[0][0].size[0])

	a = 0
	for key in range(int(sqrt(len(tiles)))):
		#board.paste(tiles[key][0], (choice(grid), choice(grid)))
		for key2 in range(int(sqrt(len(tiles)))):
			board.paste(tiles[a][0], (grid[key], grid[key2]))
			a += 1
	return board
