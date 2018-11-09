import os
from math import sin, cos, sqrt, atan2, radians

def loadLocations(path):
	csvPath = os.getcwd()+ path

	raw = open(csvPath, "r").read()

	# image, latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	#latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	return [loc.split(',')[1:] for loc in raw.split('\n')]


#locs = loadLocations('/dataset/georeferences.csv')
#for loc in locs:
#	print(loc)

#def outmostLatLong(coordinates, north = True, east = True):
#	# latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner
#
#	latsTop = [coord[0] for coord in coordinates]
#	latsBottom = [coord[2] for coord in coordinates]
#	longLeft = [coord[1] for coord in coordinates]
#	longRight = [coord[3] for coord in coordinates]
#
#	outmostLatTop = max(latsTop)
#	outmostLatBottom = min(latsBottom)
#	outmostLongLeft = min(longLeft)
#	outmostLongRight = max(longRight)
#	
#	return outmostLatTop, outmostLatBottom, outmostLongLeft, outmostLongRight
#
#locs = loadLocations('/dataset/georeferences.csv')
#print(outmostLatLong(locs))

#('9.748917', '-0.22712268471588049', '-0.071389', '96.87187494761186')

#height = outmostLatLong[0] - outmostLatLong[1]
#width = outmostLatLong[3] - outmostLatLong[2]


def coordinatesToMeters(point, point2):
	
	lat1 = radians(float(point[1]))
	lon1 = radians(float(point[0]))
	lat2 = radians(float(point2[1]))
	lon2 = radians(float(point2[0]))

	# approximate radius of earth in km
	R = 6378.137

	#lat1 = radians(52.2296756)
	#lon1 = radians(21.0122287)
	#lat2 = radians(52.406374)
	#lon2 = radians(16.9251681)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c

	return distance*1000
	#print("Result:", distance)
	#print("Should be:", 278.546, "km")

#def distances(outmostLatLong):
#
#	base1 = coordinatesToMeters([outmostLatLong[0], outmostLatLong[2]], [outmostLatLong[0], outmostLatLong[3]])
#	base2 = coordinatesToMeters([outmostLatLong[1], outmostLatLong[2]], [outmostLatLong[1], outmostLatLong[3]])
#
#	h1 = coordinatesToMeters([outmostLatLong[0], outmostLatLong[2]], [outmostLatLong[1], outmostLatLong[2]])
#	h2 = coordinatesToMeters([outmostLatLong[0], outmostLatLong[3]], [outmostLatLong[1], outmostLatLong[3]])
#
#	return (base1, base2, h1, h2)

#def boardSize(path):
#
#	coordinates = loadLocations(path)
#
#	dists = distances(outmostLatLong(coordinates, False, False))
#
#	return (dists[2] + dists[3]) / 2, (dists[0] + dists[1]) / 2

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


def tileReferences(path):

	#latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

	refs_0_0, full_Corner2, full_Corner3, full_Corner4 = outerPoints(path)

	full_Corner2 = None
	full_Corner3 = None
	full_Corner4 = None

	refs = [[]]

	coordinates = loadLocations(path)

	boardMinLon, boardMaxLat = refs_0_0[1], refs_0_0[0]

	for coord in coordinates:

		lonTopLeftCorner = coord[1]
		latTopLeftCorner = coord[0]

		x = coordinatesToMeters([boardMinLon, latTopLeftCorner], [lonTopLeftCorner, latTopLeftCorner])

		y = coordinatesToMeters([lonTopLeftCorner, boardMaxLat], [lonTopLeftCorner, latTopLeftCorner])

		refs.append([x,y])

	return refs

#latsTop = coord[0]
#latsBottom = [coord[2]
#longLeft = [coord[1]
#longRight = [coord[3]

#[-34.5355, -34.5461, -58.4740, -58.4541]
#latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner

#[[-34.5355, -58.4740, -34.5461, -58.4541], [-34.553680, -58.454227, -34.540106, -58.470613]]
#
#[40.73083, 40.72598, -73.9972, -73.9772]
#
#print(outmostLatLong([[-34.5355, -58.4740, -34.5461, -58.4541], [-34.553680, -58.454227, -34.540106, -58.470613]], False))
#print(distances(outmostLatLong([[-34.5355, -58.4740, -34.5461, -58.4541], [-34.553680, -58.454227, -34.540106, -58.470613]], False, False)))
#
#print(coordinatesToMeters([-34.5355, -58.4740], [-34.5461, -58.4740]))

#
#
#distances = distances(outmostLatLong([[-34.5355, -58.4740, -34.5461, -58.4541], [-34.553680, -58.454227, -34.540106, -58.470613]], False, False))
#
#w = (distances[0] + distances[1]) / 2
#
#h = (distances[2] + distances[4]) / 2
