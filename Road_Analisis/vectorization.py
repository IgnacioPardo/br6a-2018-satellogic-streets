from tools import *

def bmp_to_svg(path, pathOut):
	cmd('potrace --svg {} -o {}'.format(path, pathOut))