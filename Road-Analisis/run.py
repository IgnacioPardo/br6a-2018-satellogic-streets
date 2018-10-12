from visualization import *
from stitching import *
from skeletonization import *
from vectorization import *
from tools import *

def main():

	for t in originalTiles:
		predictionDepiction(pathIn, pathOut)

	tiles = loadTiles()
	
	board = createBoard(tiles)

	fitTiles(board, tiles).save('premap.bmp')

	sekeletonize('premap.bmp', 'map.bmp')

	bmp_to_svg('map.bmp', 'map.svg')





