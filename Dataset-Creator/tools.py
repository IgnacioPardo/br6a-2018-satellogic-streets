from random import uniform, randint
import math
from math import sin, cos, sqrt, atan2, radians
import os

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
	
	lat1 = radians(float(point[0]))
	lon1 = radians(float(point[1]))
	lat2 = radians(float(point2[0]))
	lon2 = radians(float(point2[1]))

	# approximate radius of earth in km
	R = 6378.137

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c

	return distance*1000


def randomRectangle(latRange, lonRange, size):

	x_Lat = round(uniform(latRange[0], latRange[1]), 8)
	y_100 = round(uniform(lonRange[0], lonRange[1]), 8)

	x_100 = offset(x_Lat, y_100, size)[0]
	y_Lon = offset(x_Lat, y_100, size)[1]

	return [[x_Lat, y_Lon], [x_100, y_Lon],	[x_100, y_100], [x_Lat, y_100]]


#geometry = randomRectangle([15, 30], [15, 30], 100)

#>>>[[15.85721248, 20.488639822451322], [15.85811079528412, 20.488639822451322], [15.85811079528412, 20.48770597], [15.85721248, 20.48770597]]

def deg2HMS(ra='', dec='', round=False):
	RA, DEC, rs, ds = '', '', '', ''
	if dec:
		if str(dec)[0] == '-':
			ds, dec = '-', abs(dec)
		deg = int(dec)
		decM = abs(int((dec-deg)*60))
		if round:
			decS = int((abs((dec-deg)*60)-decM)*60)
		else:
			decS = (abs((dec-deg)*60)-decM)*60
		DEC = '{0}{1} {2} {3}'.format(ds, deg, decM, decS)
	
	if ra:
		if str(ra)[0] == '-':
			rs, ra = '-', abs(ra)
		raH = int(ra/15)
		raM = int(((ra/15)-raH)*60)
		if round:
			raS = int(((((ra/15)-raH)*60)-raM)*60)
		else:
			raS = ((((ra/15)-raH)*60)-raM)*60
		RA = '{0}{1} {2} {3}'.format(rs, raH, raM, raS)
	
	if ra and dec:
		return (RA, DEC)
	else:
		return RA or DEC

def randomPair(latRange, lonRange):
	lat = round(uniform(latRange[0], latRange[1]), 8)
	lon = round(uniform(lonRange[0], lonRange[1]), 8)

	return lat, lon

def createCSV(lat, lon, lat2, lon2):
	lis = [['Latitude', 'Longitude', 'Name', 'Description', 'Icon', '\n']]
	
	ID = 1
	
	lis.append([str(deg2HMS(dec=lat)),' ' + str(deg2HMS(dec=lon)), ' random', ' Super Random',' ' + str(ID), '\n'])
	ID+=1
	lis.append([str(deg2HMS(dec=lat2)),' ' + str(deg2HMS(dec=lon2)), ' random', ' Super Random',' ' + str(ID), '\n'])
	ID+=1
	lis.append([str(deg2HMS(dec=lat)),' ' + str(deg2HMS(dec=lon2)), ' random', ' Super Random',' ' + str(ID), '\n'])
	ID+=1
	lis.append([str(deg2HMS(dec=lat2)),' ' + str(deg2HMS(dec=lon)), ' random', ' Super Random',' ' + str(ID), '\n'])
	
	a = []
	
	for l in lis:
		a+= l
	
	datasetGeorefs = ','.join(a).replace(',\n', '\n').replace('\n,', '\n')
	
	return datasetGeorefs

def createKML(lat, lon, lat2, lon2):

	lis = [[]]
	
	lis.append(['-'+str(lon),str(lat2),str(lat2),'\n'])
	lis.append(['-'+str(lon2),str(lat2),str(lat2),'\n'])
	lis.append(['-'+str(lon2),str(lat),str(lat),'\n'])
	lis.append(['-'+str(lon),str(lat),str(lat),'\n'])
	
	a = []
	
	for l in lis:
		a+= l
	
	opening = '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://earth.google.com/kml/2.0">\n<Document>\n<Placemark>\n<Polygon>\n<outerBoundaryIs>\n<LinearRing>\n<coordinates>\n'

	ending = "</coordinates>\n</LinearRing> </outerBoundaryIs> </Polygon>\n<Style>\n<PolyStyle>\n<color>#a00000ff</color>\n<outline>0</outline>\n</PolyStyle>\n</Style>\n</Placemark>\n</Document>\n</kml>"

	datasetGeorefs = ','.join(a).replace(',\n', '\n').replace('\n,', '\n')
	
	#print(datasetGeorefs)
	
	toSave = opening+datasetGeorefs+ending
	
	return toSave

def createKMLBulk(amt):

	bulk = []

	for i in range(amt):

		lat, lon = randomPair([25, 45], [80, 100])

		lat2, lon2 = offset(lat, lon, 100)

		bulk.append(createKML(lat, lon, lat2, lon2))

	return bulk

def addEntryToList(lis, image, latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner):
	entry = [image, latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner]
	lis.append(entry)
	return lis

def lisToCSV(lis, path):
	datasetGeorefs = []
	for entry in lis:
		#createSingle(i)
		datasetGeorefs.append(','.join([str(coord) for coord in entry]))

	toSave = '\n'.join(datasetGeorefs)

	file = open(path,'w+') 
 
	file.write(toSave)
	 
	file.close()

def merge(path):

	#pathExample = /image_1/LC08_123032_20140515

	imB = (np.array(Image.open(os.getcwd()+path+'.B2.tif'))*255)
	imG = (np.array(Image.open(os.getcwd()+path+'.B3.tif'))*255)
	imR = (np.array(Image.open(os.getcwd()+path+'.B4.tif'))*255)

	print(imB.shape)

	h, w = imB.shape

	composite = Image.new("RGB", (w, h), 'black')

	grid = composite.load()

	a = False
	if a:
		for i in range(h):
			for j in range(w):
				R = int(imR[i][j] * 255)
				G = int(imG[i][j] * 255)
				B = int(imB[i][j] * 255)
				grid[j, i] = (R, G, B)

		composite.save('merged.tif')

	imRGB = np.dstack((imR, imG, imB))#np.array(composite)
	imBGR = np.dstack((imB, imG, imR))#np.array(composite)

	gamma = 0.8


	imRGB = ((imRGB/255) ** gamma * 255).astype(int) 
	imBGR = ((imBGR/255) ** gamma * 255).astype(int) #for CV2 - better

	return 



