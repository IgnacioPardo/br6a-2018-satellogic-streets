from visualization import *
from stitching import *
from skeletonization import *
from vectorization import *
from tools import *
from skimage import data_dir

def main():

	createDirecories()

	for i in range(len(images)):
		predictionDepiction(t)

	tiles = loadTiles()
	
	board = createBoard(tiles)

	premap = fitTiles(board, tiles)
	premap.save('files/premap.bmp')
	premap.save(data_dir+'/files/premap.bmp')

	sekeletonize('files/premap.bmp', 'skeletons/map.bmp')

	bmp_to_svg('skeletons/map.bmp', 'maps/map.svg')





