from PIL import Image
from tools import *
from random import randint, choice
import os
from tqdm import tqdm
from location_tools import *
from giftWrapping import *

def loadTiles(path, amt = None, correction=False):

	ls = []

	refs = dictTileReferences(path, correction)#tileReferences(path)[1:]

	if amt == None:
		cant = len(list(filter(lambda s: s.endswith(".jpg"), os.listdir("images/"))))
	else:
		cant = amt
	print(cant)
	print('Loading Tiles')
	for i in range(cant):#tqdm(range(len(os.listdir(os.getcwd()+'/tiles/'))-1)):
		image_filename = 'tiles/tile-{}.bmp'.format(i)
		ls.append([Image.open(image_filename), refs[i]])
		print(image_filename)
	return ls

def loadImages(path, amt = None, correction=False):
	ls = []

	refs = dictTileReferences(path, correction)#tileReferences(path)[1:]

	if amt == None:
		cant = len(list(filter(lambda s: s.endswith(".jpg"), os.listdir("images/"))))
	else:
		cant = amt

	print('Loading Images')
	for i in range(cant):#tqdm(range(len(os.listdir(os.getcwd()+'/images/'))-2)):
		image_filename = 'images/image-{}.jpg'.format(i)
		ls.append([Image.open(image_filename), refs[i]])
	return ls

def createBoard(path, res):

	H = int(input('Insert Height (Mts): '))
	if H == -1:
		H = giftWrappedBoardSize(path)
	W = H
	print(H, W)

	while H > 10000:
		print('Board Height > 10000')
		H = int(input('Insert Height (Mts): '))
		W = H

	return Image.new("RGB", (int(H * res), int(W * res)), "black")


def createBoardPerfectSquares():

	H = sqrt((len(os.listdir(os.getcwd()+'/images/'))-1))*Image.open('images/image-0.jpg').size[0]

	W = H

	print(H, W)

	if H > 10000:
		print('Board Height > 10000')
		H = int(input('Insert Height (Mts): '))
		W = H

	return Image.new("RGB", (int(H), int(W)), "black")

def fitTiles(board, tiles, res):

	print('Stitching Tiles')
	for i in tqdm(range(len(tiles))):
		print((int(tiles[i][1][0] * res), int(tiles[i][1][1] * res)))
		print(i)
		board.paste(tiles[i][0], (int(tiles[i][1][0] * res), int(tiles[i][1][1] * res)))
		board.save('files/premap-saved-{}.bmp'.format(i))
	return board

def stitchImages(path, res, amt = None, correction=False):

	images = loadImages(path, amt, correction)
	board = createBoard(path, res)

	#board =  createBoardPerfectSquares()

	full = fitTiles(board, images, res)

	full.save('files/stitched-images.png')

def stitchMasks(path, res, amt = None, correction=False):

	images = loadTiles(path, amt, correction)
	board = createBoard(path, res)
	#board =  createBoardPerfectSquares()

	full = fitTiles(board, images, res)

	full.save('files/stitched-masks.png')
