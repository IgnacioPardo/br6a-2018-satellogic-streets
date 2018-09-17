from __future__ import print_function
import sys
from flask import Flask
import numpy
import PIL
from PIL import Image
import csv
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras import optimizers
from keras import applications
from keras.models import Model

app = Flask(__name__)

@app.route('/')

def main():

	#load dataset
	#roadsDataset = numpy.loadtxt("data_set_gen/roads.txt", delimiter=",")
	#notRoadsDataset = numpy.loadtxt("data_set_gen/notRoads.txt", delimiter=",")
	numpy.random.seed(7)

	imgHeight = 6973
	imgWidth = 8130

	roadsDataset = [(int(i.split(',')[0]), int(i.split(',')[1]), int(i.split(',')[2])) for i in [i[1:-1] for i in open("data_set_gen/roads.txt", "r").read().split(":")]]
	notRoadsDataset = [(int(i.split(',')[0]), int(i.split(',')[1]), int(i.split(',')[2])) for i in [i[1:-1] for i in open("data_set_gen/notRoads.txt", "r").read().split(":")]]
	
	print(roadsDataset, file=sys.stderr)
	model = Sequential()
	model.add(Dense(12, input_dim=8, activation='relu'))
	model.add(Dense(8, activation='relu'))
	model.add(Dense(1, activation='sigmoid'))



	return "ok"
	