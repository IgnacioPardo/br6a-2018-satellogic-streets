import numpy as np
import os
from math import ceil

def oitc(i, width, height):
	col = width - ceil(width - i / height) - 1
	row = height - 1 - i % height if col % 2 == 0 else i % height # up if column is even else down
	return (row, col)

def getMirrored(x = None, y = None):
	if x == None:
		x = y = 3

	arr = np.zeros((x,y))

	#print(arr.shape)

	xSize = arr.shape[0]
	ySize = arr.shape[1]

	for i in range(xSize*ySize):
		x, y = oitc(i, xSize, ySize)
		arr[x][1+y] = i

	arr = np.flip(arr, (0,1))

	wrong = np.flip(arr, (1,0))

	#wrong = np.transpose(wrong)

	#print(arr)

	#print(wrong)

	#print(arr == wrong)

	dicty = {}

	for i in range(arr.shape[0]):
		for j in range(arr.shape[1]):
			dicty[str(arr[i][j])[0:1]] = str(wrong[i][j])[0:1]

	return dicty