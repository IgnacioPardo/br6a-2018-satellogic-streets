from tools import *

def main():

	bulk = createBulk(100)

	for i, file in enumerate(bulk):
		with open("dataset/poly_%s.kml" % i, "w") as f:
			f.write(file)

main()