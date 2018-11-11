from tools import *
from imageDownloader import *

def imagePicker(amt, latRange=[20,20.005], lonRange=[80, 80.005], size=100, path='images/georeferences.csv'):
	lineas = [[]]

	for i in range(amt):

		lat, lon = randomPair(latRange, lonRange)

		lat2, lon2 = offset(lat, lon, size)
		#image = i (es el id)
		#latTopLeftCorner = x
		#longTopLeftCorner = y
		#latDownRightCorner, longDownRightCorner = offset(latTopLeftCorner,longTopLeftCorner, Dimension del cuadrado)
		#lineas.append([image, latTopLeftCorner, longTopLeftCorner, latDownRightCorner, longDownRightCorner])

		#Guardar la imagen en /images

		#downloadImage(i, lat, lon, lat2, lon2)

		lineas.append([i, lat, lon, lat2, lon2])

	lineas = lineas[1:]
	print(lineas)
	lisToCSV(lineas, path)

def run():
	#imagePicker(cantidad de imagenes, rango de latitud en donde seleccionar, ango de longitud en donde seleccionar, alto/ancho de cada imagen en metros):
	
	cantImagenes = 5
	rangoLatitud = [20,20.005]
	rangoLongitud = [80, 80.005]
	alto_ancho = 100
	georeferencias = 'images/georeferences.csv'

	imagePicker(cantImagenes, rangoLatitud, rangoLongitud, alto_ancho, georeferencias)

run()
