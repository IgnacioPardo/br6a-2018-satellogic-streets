# import the necessary packages
from __future__ import print_function
import sys
from flask import Flask
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#import utils
from PIL import Image, ImageCms
import numpy as np
import cv2
 

app = Flask(__name__)

#@app.route('/')

@app.route('/', defaults={'int' : 10})
@app.route('/<int:clusterAmmount>')

def main(clusterAmmount):
	# construct the argument parser and parse the arguments
	#ap = argparse.ArgumentParser()

	#args, unknown = ap.parse_known_args()

	#ap.add_argument("-i", "--image", default= "image.png", required = False, help = "Path to the image")
	#ap.add_argument("-c", "--clusters", default=20, required = False, type = int, help = "# of clusters")

	#ap.add_argument("-i", "--image", default= "image.png")
	#ap.add_argument("-c", "--clusters", type = int, default=20)

	#args = dir(ap.parse_known_args())
	 
	# load the image and convert it from BGR to RGB so that
	# we can dispaly it with matplotlib
	#image = cv2.imread(args["image"])

	print(1, file=sys.stderr)
	#im = cv2.imread("image.png", cv2.COLOR_BGR2RGB)
	#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# reshape the image to be a list of pixels


	im = np.asarray(Image.open('image.png'))
	image = im.reshape((im.shape[0] * im.shape[1], 3))

	print(im, file=sys.stderr)
	print(image, file=sys.stderr)



	# cluster the pixel intensities
	print(1.1, file=sys.stderr)
	clt = KMeans(n_clusters = clusterAmmount)
	print(1.2, file=sys.stderr)
	clt.fit(image)
	print(2, file=sys.stderr)
	# show our image
	#plt.figure()
	#plt.axis("off")
	
	cluster_centers = clt.cluster_centers_
	#cluster_centers
	cluster_labels = clt.labels_
	print(cluster_labels, file=sys.stderr)
	cluster_centers[cluster_labels].reshape(im.shape[0], im.shape[1], im.shape[2])

	print(3, file=sys.stderr)
	
	cv2.imwrite('cluster.png', cluster_centers[cluster_labels].reshape(im.shape[0], im.shape[1], im.shape[2]))
	cv2.imwrite('cluster2.png', cluster_centers[cluster_labels])

	print(cluster_centers[cluster_labels].reshape(im.shape[0], im.shape[1], im.shape[2]), file=sys.stderr)

	for i in cluster_labels:
		cv2.imwrite(str(i)+'cluster.png', cluster_centers[i])
		print(i, file=sys.stderr)

	def centroid_histogram(clt):
		# grab the number of different clusters and create a histogram
		# based on the number of pixels assigned to each cluster
		numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
		(hist, _) = np.histogram(clt.labels_, bins = numLabels)
	 	
		# normalize the histogram, such that it sums to one
		hist = hist.astype("float")
		hist /= hist.sum()
	 
		# return the histogram
		print(4, file=sys.stderr)
		return hist

	def plot_colors(hist, centroids):
		# initialize the bar chart representing the relative frequency
		# of each of the colors
		bar = np.zeros((50, 300, 3), dtype = "uint8")
		startX = 0
	 
		# loop over the percentage of each cluster and the color of
		# each cluster
		for (percent, color) in zip(hist, centroids):
			# plot the relative percentage of each cluster
			endX = startX + (percent * 300)
			cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
				color.astype("uint8").tolist(), -1)
			startX = endX
		
		# return the bar chart
		print(4.5, file=sys.stderr)
		return bar

		# build a histogram of clusters and then create a figure
	# representing the number of pixels labeled to each color
	hist = centroid_histogram(clt)
	bar = plot_colors(hist, clt.cluster_centers_)
	print(5, file=sys.stderr)
	
	# show our color bart
	#plt.figure()
	#plt.axis("off")
	cv2.imwrite('bar.png', bar)
	#plt.show()
	return str(cluster_labels)