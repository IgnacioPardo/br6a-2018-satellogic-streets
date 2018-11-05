from visualization import *
from stitching import *
from skeletonization import *
from vectorization import *
from tools import *
from skimage import data_dir

def main():

	createDirecories() #tools.py

	for i in range(len(images)):
		predictionDepiction(i)  #visualization.py Creates 'tiles/tile-i.bmp' from 'images/image-i.png'

	tiles = loadTiles() #stitching.py Returns list of PIL.Images from 'tiles/'' files and appends locations to each from '/dataset/georeferences.csv'
	
	board = createBoard() #stitching.py Returns PIl.Image of dimentions extracted from '/dataset/georeferences.csv' outmosts latitude and longitud converted to meters (Res of 1m^2/pix)

	premap = fitTiles(board, tiles) #stitching.py Pastes tiles into board with lat/long coordinates as reference
	premap.save('files/premap.bmp')
	premap.save(data_dir+'/files/premap.bmp')

	sekeletonize('files/premap.bmp', 'skeletons/map.bmp') #skeletonization.py Creates line image out of original squares.

	bmp_to_svg('skeletons/map.bmp', 'maps/map.svg') #vectorization.py Vectorizes line image.