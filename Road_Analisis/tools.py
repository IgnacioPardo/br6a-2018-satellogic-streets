import os
from skimage import data_dir

def cmd(line):
	os.system(line)

def carResults():
	csvPath = os.getcwd() + '/car_count.csv'

	raw = open(csvPath, "r").read()

	for count in raw.split('\n'):
		print(count)

def openCarPredictions():
	cmd('open Car_Detection/car_predictions')

def openMap():
	cmd('open files/stitched-images.png')

def openRoadMap():
	cmd('open maps/map.svg')

def openRoadPremap():
	cmd('open files/premap.bmp')

def runSh(path):
	lines = open(path, "r").read().split('\n')
	for l in lines:
		print(l)
		cmd(l)

def sqrt(n):
	return n**(0.5)

def createDirectories():
	if not os.path.exists(data_dir+'/skeletons/'):
		os.makedirs(data_dir+'/skeletons/')
	if not os.path.exists(data_dir+'/files/'):
		os.makedirs(data_dir+'/files/')
	if not os.path.exists(os.getcwd()+'/skeletons/'):
		os.makedirs(os.getcwd()+'/skeletons/')
	if not os.path.exists(os.getcwd()+'/tiles/'):
		os.makedirs(os.getcwd()+'/tiles/')
	if not os.path.exists(os.getcwd()+'/files/'):
		os.makedirs(os.getcwd()+'/files/')
	if not os.path.exists(os.getcwd()+'/maps/'):
		os.makedirs(os.getcwd()+'/maps/')
	if not os.path.exists(os.getcwd()+'/tests/'):
		os.makedirs(os.getcwd()+'/tests/')
	if not os.path.exists(os.getcwd()+'/images/'):
		os.makedirs(os.getcwd()+'/images/')
	if not os.path.exists(os.getcwd()+'/dataset/'):
		os.makedirs(os.getcwd()+'/dataset/')
	if not os.path.exists(os.getcwd()+'/predictions/'):
		os.makedirs(os.getcwd()+'/predictions/')
	if not os.path.exists(os.getcwd()+'/Car_Detection/car_predictions'):
		os.makedirs(os.getcwd()+'/Car_Detection/car_predictions')