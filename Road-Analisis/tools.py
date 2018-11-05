import os
from skimage import data_dir

def cmd(line):
	os.system(line)
	
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

