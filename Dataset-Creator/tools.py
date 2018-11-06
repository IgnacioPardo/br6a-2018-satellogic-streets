from random import uniform, randint
import math
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


def createBulk(amt):

	bulk = []

	for i in range(amt):

		lat, lon = randomPair([25, 45], [80, 100])

		lat2, lon2 = offset(lat, lon, 100)

		bulk.append(createKML(lat, lon, lat2, lon2))

	return bulk