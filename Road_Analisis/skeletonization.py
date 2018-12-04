from skimage.morphology import skeletonize_3d
from skimage.data import load
from skimage import io
from tools import *

def sekeletonize(path, pathOut):
	data = load(path, as_gray=True, as_grey=True)
	
	skeleton3d = skeletonize_3d(data)

	io.imsave(pathOut, skeleton3d)