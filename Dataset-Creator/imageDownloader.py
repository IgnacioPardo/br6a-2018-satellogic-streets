import ee
#from urllib import request, error
import zipfile
#import requests

def unzip(path):
	zip_ref = zipfile.ZipFile(path, 'r')
	zip_ref.extractall(path[:-4])
	zip_ref.close()

def downloadImage(i, lat, lon, lat2, lon2):

	ee.Initialize()

	geometry = [[lon,lat], [lon,lat2], [lon2,lat2], [lon2,lat]]

	image = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_123032_20140515').select(['B4', 'B3', 'B2']);
	path = image.getDownloadUrl({
	    'scale': 100,
	    'crs': 'EPSG:4326',
	    'region': geometry
	})

	print(path)

	#Descargar imagen de path descomrpimirla con unzip, componerla
	
