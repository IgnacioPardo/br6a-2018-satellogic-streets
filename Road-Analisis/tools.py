import os

def cmd(line):
	os.system(line)
	
def runSh(path):
	lines = open(path, "r").read().split('\n')
	for l in lines:
		print(l)
		cmd(l)

def sqrt(n):
	return n**(0.5)