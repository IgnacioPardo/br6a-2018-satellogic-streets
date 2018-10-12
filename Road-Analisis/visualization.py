from tools import *
from PIL import Image
import cv2
	
def colorBlock(i, j, pxs, tup):
	for k in range(16):
		for q in range(16):
			pxs[i+k,j+q] = tup
	return pxs

def predictionDepiction(i):
	image = Image.open('test_set_images/test_'+str(i)+'/test_' + str(i) + '.png')
	pxs = image.load()
	prediction = open('submission.csv').read()
	image.save('test{}.png'.format(i))
	thisImagesPredictions = [(int(a.split(',')[0].split('_')[-1]), int(a.split(',')[0].split('_')[-2]), int(a.split(',')[1])) for a in prediction.split('\n') if (a.split(',')[0].split('_')[0] == ('00' if (i<10) else '0') + str(i))]

	roadBlocks = [(pred[0], pred[1]) for pred in thisImagesPredictions if pred[2] == 0]

	notRoadBlocks = [(pred[0], pred[1]) for pred in thisImagesPredictions if pred[2] == 1]
	for a in roadBlocks:
		pxs = colorBlock(a[0],a[1],pxs, (0,0,0))

	for a in notRoadBlocks:
		pxs = colorBlock(a[0],a[1],pxs, (255,255,255))

	img = cv2.imread('test{}-prediction.png'.format(i),0)
	
	#laplacian = cv2.Laplacian(img,cv2.CV_64F)

	#cv2.imwrite('test{}-prediction-laplacian.png'.format(i), laplacian)

	#cv2.imwrite('test{}-prediction-laplacian.bmp'.format(i), laplacian)