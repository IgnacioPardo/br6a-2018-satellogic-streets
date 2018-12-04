import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
import cv2
import datetime

print(datetime.datetime.time(datetime.datetime.now()))

imB = (np.array(Image.open(os.getcwd()+'/image_1/LC08_123032_20140515.B2.tif'))*255)
imG = (np.array(Image.open(os.getcwd()+'/image_1/LC08_123032_20140515.B3.tif'))*255)
imR = (np.array(Image.open(os.getcwd()+'/image_1/LC08_123032_20140515.B4.tif'))*255)

print(imB.shape)

h, w = imB.shape

composite = Image.new("RGB", (w, h), 'black')

grid = composite.load()

a = False
if a:
	for i in range(w):
		for j in range(h):
			R = int(imR[i][j] * 255)
			G = int(imG[i][j] * 255)
			B = int(imB[i][j] * 255)
			grid[j, i] = (R, G, B)

	composite.save('merged.tif')

imRGB = np.dstack((imR, imG, imB))#np.array(composite)
imBGR = np.dstack((imB, imG, imR))#np.array(composite)

#test1 = np.array(zip((imR.tolist(), imG.tolist(), imB.tolist()))).astype(float)
test2 = np.array(zip((imB.tolist(), imG.tolist(), imR.tolist()))).astype(float)

gamma = 0.8


imRGB = ((imRGB/255) ** gamma * 255).astype(int)
imBGR = ((imBGR/255) ** gamma * 255).astype(int)

null = np.empty([w, h])

imB = np.dstack((null, null, imB))
imG = np.dstack((null, imG, null))
imR = np.dstack((imR, null, null))

print(imRGB)
print(datetime.datetime.time(datetime.datetime.now()))
#print(imB.tolist())

#cv2.imshow('Composite', imRGB)
cv2.imwrite('merged-imBGR.tif', imBGR)
cv2.imwrite('merged-imRGB.tif', imRGB)

print(imBGR.shape)

print(cv2.split(imBGR))
print(cv2.split(imRGB))

fig, axes = plt.subplots(2, 3, figsize=(8, 8), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(imB)
ax[0].set_title('Blue')
ax[0].axis('off')

ax[1].imshow(imG)
ax[1].set_title('Green')
ax[1].axis('off')

ax[2].imshow(imR)
ax[2].set_title('Red')
ax[2].axis('off')

ax[3].imshow(imBGR)
ax[3].set_title('BGR')
ax[3].axis('off')

ax[4].imshow(imRGB)
ax[4].set_title('RGB')
ax[4].axis('off')

print(test2)
#
ax[5].imshow(test2)
ax[5].set_title('RGB-BGR')
ax[5].axis('off')

plt.show()
