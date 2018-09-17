from __future__ import print_function
import sys
from flask import Flask
import numpy as np
import PIL
from PIL import Image
import math

def roadish(colorTuple, strictness=0):

	roadsDataset = [(int(i.split(',')[0]), int(i.split(',')[1]), int(i.split(',')[2])) for i in [i[1:-1] for i in open("data_set_gen/roads.txt", "r").read().split(":")]]
	notRoadsDataset = [(int(i.split(',')[0]), int(i.split(',')[1]), int(i.split(',')[2])) for i in [i[1:-1] for i in open("data_set_gen/notRoads.txt", "r").read().split(":")]]

	distanceList = []
	antiDistanceList = []

	for i in range(len(roadsDataset)):
		distanceList.append(math.sqrt(((colorTuple[0] - roadsDataset[i][0])**2)+((colorTuple[1] - roadsDataset[i][1])**2)+((colorTuple[2] - roadsDataset[i][2])**2)))

	for i in range(len(notRoadsDataset)):
		antiDistanceList.append(math.sqrt(((colorTuple[0] - notRoadsDataset[i][0])**2)+((colorTuple[1] - notRoadsDataset[i][1])**2)+((colorTuple[2] - notRoadsDataset[i][2])**2)))	

	max = math.sqrt((255**2)*3)

	roadDistance = (sum(distanceList) / float(len(distanceList))) / max

	notRoadDistance = (sum(antiDistanceList) / float(len(antiDistanceList))) / max

	case = roadDistance < notRoadDistance + strictness

	return (case, roadDistance) if case is True else (case, notRoadDistance)

def redefineClusters(correct, full):

	matrix = full.load()

	for x in range(len(correct)):
		for i in range(full.size[0]):
			for j in range(full.size[1]):
				if full.getpixel((i, j)) == correct[x]:
					matrix[i, j] == (255, 255, 0)
	return full


app = Flask(__name__)

@app.route('/')

def main():

	cl = Image.open('color-cluster/cluster.png')

	print(cl.getcolors(), file=sys.stderr)

	bg = Image.open('color-cluster/image.png')

	clPixList = []

	for i in range(cl.size[0]):
		for j in range(cl.size[1]):
			#if im.getpixel((i, j)) == colorToCheck:
			#print(roadish(bg.getpixel((i, j))), file=sys.stderr)
			#print(type(similarity(bg.getpixel((i, j)))), file=sys.stderr)
			prob = roadish(bg.getpixel((i, j)))
			if prob[0]:
				clPixList.append(cl.getpixel((i, j)))

	clEnd = list(set(clPixList))
	
	detected = redefineClusters(clEnd, cl)

	detected.save('finalOutput.png')

	return str(len(cl.getcolors()))