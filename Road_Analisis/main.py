from run import *
from location_tools import *
from tools import *
from test_tools import *
from giftWrapping import *
from Road_Detection.classify import *
from Car_Detection.count import *
import shutil
import os

def cli():

	cmd('clear')

	createDirectories()

	georeferencesPath = '/images/georeferences.csv'

	res = calcRes(georeferencesPath)

	corrections = True

	while True:

		cmmd = input('Command: ')

		cmmds = ['break', 'createDirectories', 'roads', 'openRPredictions', 'cars', 'viewCars', 'simulatePr', 'multiple', 'single', 'separated', 'multiple!s', 'single!s', 'separated!s', 'convexHull', 'createGeorefs', 'ls', 'changeRes', 'changeGeorefsPath', 'stitchImages', 'stitchMasks', 'openStitchedMasks', 'openRoadPremap', 'openStitchedImages', 'openMap', 'openRoadMap', 'printRefs', 'calcRes', 'newLoc', 'quit', 'correct', 'clear']
		
		if cmmd == 'break':
			break
		elif cmmd == 'createDirectories':
			createDirectories()
		elif cmmd == 'road':
			predictRoads(full = True)
		elif cmmd == 'roads':
			if os.path.exists(os.getcwd()+'/predictions/'):
				shutil.rmtree('predictions')
			os.makedirs(os.getcwd()+'/predictions/')
			predictRoads()
		elif cmmd == 'openRPredictions':
			cmd('open predictions/')
		elif cmmd == 'cars':
			predictCars()
			carResults()
		elif cmmd == 'viewCars':
			openCarPredictions()
		elif cmmd == 'simulatePr':
			simulatePredictions(int(input('Ammount')))
		elif cmmd == 'multiple':
			multiple(georeferencesPath, res, corrections)
		elif cmmd == 'single':
			single()
		elif cmmd == 'separated':
			separated()
		elif cmmd == 'multiple!s':
			multipleNoSkeleton(georeferencesPath, res, corrections)
		elif cmmd == 'single!s':
			singleNoSkeleton()
		elif cmmd == 'separated!s':
			separatedNoSkeleton()
		elif cmmd == 'convexHull':
			coordConvexHull(georeferencesPath)
		elif cmmd == 'createGeorefs':
			createGeoreferences(int(input('Ammount')), georeferencesPath)
		elif cmmd == 'ls':
			for cm in cmmds:
				print(cm)
		elif cmmd == 'changeRes':
			print('Current Resolution: {}'.format(res))
			res = float(input('Enter New Resolution: '))
		elif cmmd == 'changeGeorefsPath':
			print('Current Path: "{}"'.format(georeferencesPath))
			georeferencesPath = str(input('Enter New Path: '))
		elif cmmd == 'stitchImages':
			cant = int(input('Ammount: '))
			if cant == -1:
				cant = None
			stitchImages(georeferencesPath, res, amt = cant, correction=corrections)
		elif cmmd == 'stitchMasks':
			cant = int(input('Ammount: '))
			if cant == -1:
				cant = None
			stitchMasks(georeferencesPath, res, amt = cant, correction=corrections)
		elif cmmd == 'openStitchedMasks' or cmmd == 'openRoadPremap':
			openRoadPremap()
		elif cmmd == 'openStitchedImages' or cmmd == 'openMap':
			openMap()
		elif cmmd == 'openRoadMap':
			openRoadMap()
		elif cmmd == 'printRefs':
			print(dictGeoreferences(georeferencesPath))
		elif cmmd == 'calcRes':
			res = calcRes(georeferencesPath)
			print(res)
		elif cmmd == 'newLoc':
			latRange = [40, 40.0005]
			lonRange = [80, 80.0005]
			rect = randomRectangle(latRange, lonRange, 100)
			print(rect)
		elif cmmd == 'quit':
			quit()
		elif cmmd == 'correct':
			corrections = True
		elif cmmd == 'clear':
			cmd('clear')
		elif cmmd[0:3] == 'cmd':
			cmd(cmmd[5:-2])
		else:
			print("'{}' is not a Command".format(cmmd))

cli()

