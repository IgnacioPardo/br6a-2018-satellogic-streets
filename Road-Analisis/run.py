from visualization import *
from stitching import *
from skeletonization import *
from vectorization import *
from tools import *
from skimage import data_dir

def multiple():

	createDirecories() #tools.py

	#Neural Net Predicts roads from /images and saves to /predictions

	for i in tqdm(range(len(os.listdir(os.getcwd()+'/predictions/')))):
	#for i in range(len(predictions)):
		predictionDepiction(i)  #visualization.py Creates 'tiles/tile-i.bmp' from 'predictions/prediction-i.png'

	georeferencesPath = 'images/georeferences.csv'

	tiles = loadTiles(georeferencesPath) #stitching.py Returns list of PIL.Images from 'tiles/'' files and appends locations to each from '/dataset/georeferences.csv'
	
	board = createBoard(georeferencesPath) #stitching.py Returns PIl.Image of dimentions extracted from '/dataset/georeferences.csv' outmosts latitude and longitud converted to meters (Res of 1m^2/pix)

	premap = fitTiles(board, tiles) #stitching.py Pastes tiles into board with lat/long coordinates as reference
	premap.save('files/premap.bmp')
	premap.save(data_dir+'/files/premap.bmp')

	sekeletonize('files/premap.bmp', 'skeletons/map.bmp') #skeletonization.py Creates line image out of original squares.

	bmp_to_svg('skeletons/map.bmp', 'maps/map.svg') #vectorization.py Vectorizes line image.


def single():

	createDirecories()

	#Neural Net Predicts roads from /images and saves to /predictions

	predictionDepiction(0)

	premap = fitTiles(board, tiles)

	premap.save('tiles/tile_0.bmp')

	premap.save(data_dir+'/files/premap.bmp')

	sekeletonize('files/premap.bmp', 'skeletons/map.bmp') #skeletonization.py Creates line image out of original squares.

	bmp_to_svg('skeletons/map.bmp', 'maps/map.svg')


def separated():

	createDirecories()

	#Neural Net Predicts roads from /images and saves to /predictions

	for i in tqdm(range(len(os.listdir(os.getcwd()+'/predictions/')))):
	#for i in range(len(predictions)):
		predictionDepiction(i)

		premap = fitTiles(board, tiles)

		premap.save('tiles/tile_{}.bmp'.format(i))

		premap.save(data_dir+'/files/premap_{}.bmp'.format(i))

		sekeletonize('files/premap_{}.bmp'.format(i), 'skeletons/map_{}.bmp'.format(i)) #skeletonization.py Creates line image out of original squares.

		bmp_to_svg('skeletons/map_{}.bmp'.format(i), 'maps/map_{}.svg'.format(i))




