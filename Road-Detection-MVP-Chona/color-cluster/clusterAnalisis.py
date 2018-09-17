from __future__ import print_function
import sys
from flask import Flask
import numpy
import PIL
from PIL import Image

 

app = Flask(__name__)

@app.route('/')

def main():

	cl = Image.open('color-cluster/cluster.png')

	print(cl.getcolors(), file=sys.stderr)

	bg = Image.open('color-cluster/image.png')

	for i in range(cl.size[0]):
		for j in range(cl.size[1]):

				


	return str(len(cl.getcolors()))


def similarity():

	roadsDataset = [(int(i.split(',')[0]), int(i.split(',')[1]), int(i.split(',')[2])) for i in [i[1:-1] for i in open("data_set_gen/roads.txt", "r").read().split(":")]]
	notRoadsDataset = [(int(i.split(',')[0]), int(i.split(',')[1]), int(i.split(',')[2])) for i in [i[1:-1] for i in open("data_set_gen/notRoads.txt", "r").read().split(":")]]

	return