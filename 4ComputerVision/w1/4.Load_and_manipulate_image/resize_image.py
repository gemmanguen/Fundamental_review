# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:38:36 2022

@author: ADMIN
"""
'''
# create a thumbnail of an image
from PIL import Image
# load the image
image = Image.open("opera_house.jpg")
# report the size of the image
print(image.size)
# create a thumbnail and preserve aspect ratio
image.thumbnail((100,100))
# report the size of the modified image
print(image.size)
# show the image
image.show()

'''
# resize image and force a new shape
from PIL import Image
# load the image
image = Image.open("opera_house.jpg")
# report the size of the image
print(image.size)
# resize image and ignore original aspect ratio
img_resized = image.resize((200,200))
# report the size of the thumbnail
print(img_resized.size)
# show the image
img_resized.show()
