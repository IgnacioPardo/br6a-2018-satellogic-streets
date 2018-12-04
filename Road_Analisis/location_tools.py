import os
import math
from math import sin, cos, sqrt, atan2, radians, ceil
from random import uniform
from PIL import Image
from matrixMirroring import *

def loadLocations(path):
	csvPath = os.getcwd()+ path

	raw = open(csvPath, "r").read()

	# image, latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	#latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	return [loc.split(',')[1:] for loc in raw.split('\n')]


def dictGeoreferences(path, correction=False):
	csvPath = os.getcwd()+ path

	raw = open(csvPath, "r").read()

	# image, latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	#latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	dictionary = {}

	for loc in raw.split('\n'):

		imid = loc.split(',')[0]

		dictionary[str(imid)] = loc.split(',')[1:]
	if not correction:
		return dictionary
	else:
		new_dictionary = {}
		poss = getMirrored()

		for i in range(len(raw.split('\n'))):
			#new_dictionary[str(ncti(oitc(i)))] = dictionary[str(i)]
			new_dictionary[str(poss[str(i)])] = dictionary[str(i)]

		return new_dictionary
		

def calcRes(path, correction=False):
	dicty = dictGeoreferences(path, correction)

	x = [dicty['0'][1], dicty['0'][0]]
	y = [dicty['0'][3], dicty['0'][0]]

	meters = coordinatesToMeters(x, y)

	width = Image.open('images/image-0.jpg').size[0]

	return width/meters

def randomPair(latRange, lonRange):
	lat = round(uniform(latRange[0], latRange[1]), 8)
	lon = round(uniform(lonRange[0], lonRange[1]), 8)

	return lat, lon

def offset(lat, lon, offset):
	 #Earth’s radius, sphere

	 lat = float(lat)
	 lon = float(lon)

	 R=6378137

	 #offsets in meters
	 dn = offset
	 de = offset

	 #Coordinate offsets in radians
	 dLat = dn/R
	 dLon = de/(R*math.cos(math.pi*lat/180))

	 #OffsetPosition, decimal degrees
	 latO = round(lat + dLat * 180/math.pi, 8)
	 lonO = round(lon + dLon * 180/math.pi, 8)

	 return latO, lonO

def coordinatesToMeters(point, point2):
	
	lat1 = radians(float(point[1]))
	lon1 = radians(float(point[0]))
	lat2 = radians(float(point2[1]))
	lon2 = radians(float(point2[0]))

	# approximate radius of earth in km
	R = 6378.137

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c

	return distance*1000
	

def coordinatesToPixels(coordinates):

	outmosts = outmostLatLong(coordinates, north = True, east = True)

	top = outmosts[0]
	left = outmosts[0]

	pixReferences = [(coordinatesToMeters([top, coord[1]], [coord[0], coord[1]]), coordinatesToMeters([coord[0], left], [coord[0], coord[1]])) for coord in coordinates]

	return pixReferences


def outerPoints(path):

	coordinates = loadLocations(path)

	#latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	maxLatTop = max([coord[0] for coord in coordinates])
	minLonTop = min([coord[1] for coord in coordinates])
	minLatDown = min([coord[2] for coord in coordinates])
	maxLonDown = max([coord[3] for coord in coordinates])

	full_Corner1 = [minLonTop,maxLatTop]
	full_Corner2 = [maxLonDown,maxLatTop]
	full_Corner3 = [maxLonDown,minLatDown]
	full_Corner4 = [minLonTop,minLatDown]

	return full_Corner1, full_Corner2, full_Corner3, full_Corner4

def randomRectangle(latRange, lonRange, size):

	x_Lat = round(uniform(latRange[0], latRange[1]), 8)
	y_100 = round(uniform(lonRange[0], lonRange[1]), 8)

	x_100 = offset(x_Lat, y_100, size)[0]
	y_Lon = offset(x_Lat, y_100, size)[1]

	return [[x_Lat, y_Lon], [x_100, y_Lon],	[x_100, y_100], [x_Lat, y_100]]

def tileReferences(path):

	#latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	refs_0_0, full_Corner2, full_Corner3, full_Corner4 = outerPoints(path)

	full_Corner2 = None
	full_Corner3 = None
	full_Corner4 = None

	refs = [[]]

	coordinates = loadLocations(path)

	boardMinLon, boardMaxLat = refs_0_0[0], refs_0_0[1]

	for coord in coordinates:

		lonTopLeftCorner = coord[1]
		latTopLeftCorner = coord[0]

		x = coordinatesToMeters([boardMinLon, latTopLeftCorner], [lonTopLeftCorner, latTopLeftCorner])

		y = coordinatesToMeters([lonTopLeftCorner, boardMaxLat], [lonTopLeftCorner, latTopLeftCorner])

		refs.append([x,y])

	return refs


def dictTileReferences(path, correction=False):

	refs_0_0, full_Corner2, full_Corner3, full_Corner4 = outerPoints(path)

	full_Corner2 = None
	full_Corner3 = None
	full_Corner4 = None

	boardMinLon, boardMaxLat = refs_0_0[0], refs_0_0[1]

	# image, latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	#latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	refs = dictGeoreferences(path, correction)

	dictionary = {}

	for i in range(len(refs)):

		coord = refs[str(i)]

		lonTopLeftCorner = coord[1]
		latTopLeftCorner = coord[0]

		x = coordinatesToMeters([boardMinLon, latTopLeftCorner], [lonTopLeftCorner, latTopLeftCorner])

		y = coordinatesToMeters([lonTopLeftCorner, boardMaxLat], [lonTopLeftCorner, latTopLeftCorner])

		#dictionary[imid] = [x,y]
		dictionary[i] = [x,y]

	return dictionary
