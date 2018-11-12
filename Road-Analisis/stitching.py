from PIL import Image
from tools import *
from random import randint, choice
import os
from tqdm import tqdm
from location_tools import *
from giftWrapping import *

def loadTiles(path):

	ls = []

	refs = tileReferences(path)

	for i in tqdm(range(len(os.listdir(os.getcwd()+'/tiles/'))-3)):
		image_filename = 'tiles/tile-{}.bmp'.format(i)
		ls.append([Image.open(image_filename), refs[i]])
	return ls

def createBoard(path, res):

	H = 0
	W = 0

	H, W = giftWrappedBoardSize(path)

	return Image.new("RGB", (int(H * res), int(W * res)), "black")

def fitTiles(board, tiles, res):

	for tile in tiles:
		board.paste(tile[0], (int(tile[1][1] * res), int(tile[1][0] * res)))
	return board