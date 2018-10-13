from visualization import *
from stitching import *
from skeletonization import *
from vectorization import *
from tools import *
from skimage import data_dir

def main():

	createDirecories()

	for t in originalTiles:
		predictionDepiction(pathIn, pathOut)

	tiles = loadTiles()
	
	board = createBoard(tiles)

	fitTiles(board, tiles).save('files/premap.bmp')
	
	fitTiles(board, tiles).save(data_dir+'/files/premap.bmp')

	sekeletonize('files/premap.bmp', 'skeletons/map.bmp')

	bmp_to_svg('skeletons/map.bmp', 'maps/map.svg')





