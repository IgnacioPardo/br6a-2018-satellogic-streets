from visualization import *
from stitching import *
from skeletonization import *
from vectorization import *
from tools import *
from skimage import data_dir

def multiple(georeferencesPath, res, correction=False):

	#Neural Net Predicts roads from /images and saves to /predictions

	#for i in range(len(predictions)):

	print('Enlarging Predictions')

	cant = len(list(filter(lambda s: s.endswith(".bmp"), os.listdir("predictions/"))))

	for i in tqdm(range(cant)):
		predictionDepiction(i)  #visualization.py Creates 'tiles/tile-i.bmp' from 'predictions/prediction-i.png'

	tiles = loadTiles(georeferencesPath, correction=correction) #stitching.py Returns list of PIL.Images from 'tiles/'' files and appends locations to each from '/dataset/georeferences.csv'

	board = createBoard(georeferencesPath, res) #stitching.py Returns PIl.Image of dimentions extracted from '/dataset/georeferences.csv' outmosts latitude and longitud converted to meters (Res of 1m^2/pix)

	premap = fitTiles(board, tiles, res) #stitching.py Pastes tiles into board with lat/long coordinates as reference

	premap.save('files/premap.bmp')
	
	premap.save(data_dir+'/files/premap.bmp')

	sekeletonize('files/premap.bmp', 'skeletons/map.bmp') #skeletonization.py Creates line image out of original squares.

	bmp_to_svg('skeletons/map.bmp', 'maps/map.svg') #vectorization.py Vectorizes line image.


def single():

	#Neural Net Predicts roads from /images and saves to /predictions

	predictionDepiction(0)

	premap = Image.open('tiles/tile-0.bmp')

	premap.save(data_dir+'/files/premap.bmp')

	sekeletonize('files/premap.bmp', 'skeletons/map.bmp') #skeletonization.py Creates line image out of original squares.

	bmp_to_svg('skeletons/map.bmp', 'maps/map.svg')


def separated():

	#Neural Net Predicts roads from /images and saves to /predictions
	
	
	print('Enlarging Predictions')#for i in range(len(predictions)):
	cant = len(list(filter(lambda s: s.endswith(".bmp"), os.listdir("predictions/"))))

	for i in tqdm(range(cant)):
		predictionDepiction(i)

	print('Creating Vector Maps')
	for i in tqdm(range(len(os.listdir(os.getcwd()+'/predictions/')))):

		premap = Image.open('tiles/tile-{}.bmp'.format(i))

		premap.save(data_dir+'/files/premap-{}.bmp'.format(i))

		sekeletonize('files/premap-{}.bmp'.format(i), 'skeletons/map-{}.bmp'.format(i)) #skeletonization.py Creates line image out of original squares.

		bmp_to_svg('skeletons/map-{}.bmp'.format(i), 'maps/map-{}.svg'.format(i))

def multipleNoSkeleton(georeferencesPath, res, correction=False):

	#Neural Net Predicts roads from /images and saves to /predictions

	print('Enlarging Predictions')

	cant = len(list(filter(lambda s: s.endswith(".bmp"), os.listdir("predictions/"))))

	for i in tqdm(range(cant)):
		predictionDepiction(i)

	tiles = loadTiles(georeferencesPath, correction=correction) 

	board = createBoard(georeferencesPath, res) 

	premap = fitTiles(board, tiles, res) 
	premap.save('files/premap.bmp')
	premap.save(data_dir+'/files/premap.bmp')

	bmp_to_svg('files/premap.bmp', 'maps/map.svg')

def singleNoSkeleton():

	#Neural Net Predicts roads from /images and saves to /predictions

	predictionDepiction(0)

	premap = Image.open('tiles/tile-0.bmp')

	premap.save(data_dir+'/files/premap.bmp')

	premap.save('files/premap.bmp')
	
	bmp_to_svg('files/premap.bmp', 'maps/map.svg')

def separatedNoSkeleton():

	#Neural Net Predicts roads from /images and saves to /predictions

	print('Enlarging Predictions')
	for i in tqdm(range(len(os.listdir(os.getcwd()+'/predictions/')))):

		predictionDepiction(i)

	print('Creating Vector Maps (No Skeletons)')
	for i in tqdm(range(len(os.listdir(os.getcwd()+'/predictions/')))):

		premap = Image.open('tiles/tile-{}.bmp'.format(i))

		premap.save(data_dir+'/files/premap-{}.bmp'.format(i))

		premap.save('files/premap-{}.bmp'.format(i))

		bmp_to_svg('files/premap-{}.bmp'.format(i), 'maps/map-{}.svg'.format(i))