from PIL import Image
from tools import *

def loadTiles():
	ls = []
	for i in range(1, 50):
		image_filename = 'test_set_images/test_'+str(i)+'/test_' + str(i) + '.png'
		#print(str(image_filename))
		ls.append([Image.open(image_filename), ])
	return ls

def createBoard(tiles):
	H = 0
	W = 0
	H = tiles[0].size[0] * sqrt(len(tiles))
	W = tiles[0].size[1] * sqrt(len(tiles))
	#for tile in tiles:
		#H += tile.size[0]
		#W += tile.size[1]
	print(len(tiles) ,'\n',H, W)

	return im = Image.new("RGB", (H, W), "black")
	#for i, img in ls:
	#	im.paste(img, (H/i """here goes georeferentiated position"""))

def fitTiles(board, tiles):
	for tile in tiles:
		board.paste(tile, ("""georeferentiated position"""))
	return board

createBoard(loadTiles())
