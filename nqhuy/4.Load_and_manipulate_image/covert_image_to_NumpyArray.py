# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:03:04 2022

@author: ADMIN
"""
'''
# load and display an image with Matplotlib

from matplotlib import image
from matplotlib import pyplot
# load image as pixel array
data = image.imread("opera_house.jpg")
# summarise shape of the pixel array
print(data.dtype)
print(data.shape)
# display the array of pixels as an image
pyplot.imshow(data)
pyplot.show()
'''

'''
# load image and convert to and from NumPy array
from PIL import Image
from numpy import asarray
# load the image
image = Image.open("opera_house.jpg")
# convert image to numpy array
data = asarray(image)
# summarize shape
print(data.shape)
# create Pillow image
image2 = Image.fromarray(data)
# summarize image details
print(image2.format)
print(image2.mode)
print(image2.size)

'''

# load all images in a directory
from os import listdir
from matplotlib import image
# load all images in a directory
loaded_images = list()
for filename in listdir('images'):
    # load image
    img_data = image.imread('images/'+filename)
    # store loaded image
    loaded_images.append(img_data)
    print('> loaded %s %s' % (filename, img_data.shape))
