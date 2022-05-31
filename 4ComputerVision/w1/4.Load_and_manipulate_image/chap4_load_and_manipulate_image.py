# -*- coding: utf-8 -*-
"""
Created on Fri May 27 08:55:21 2022

@author: ADMIN
"""

#------------------------------------------------------------------------------
# to load library
#------------------------------------------------------------------------------

from os import listdir
from matplotlib import image
from PIL import Image
from matplotlib import pyplot

#------------------------------------------------------------------------------
# SUBMODULES
#------------------------------------------------------------------------------

# loading all images in a directory
def convert_images_to_numpy_array(directory_name):
    loaded_images = list()
    for filename in listdir(directory_name):
        # load image
        img_data = image.imread(directory_name +'/'+ filename)
        # store loaded image
        loaded_images.append(img_data)
        print('> loaded %s %s' % (filename, img_data.shape))

# load an image with Matplotlib
def load_image(image_name):
    image = Image.open(image_name)
    # summarize some details about the image
    print(image.format)
    print(image.mode)
    print(image.size)
    # show the image
    image.show()
    
# cropping an image
def crop_image(image_name, x1, y1, x2, y2):
    # load image
    image = Image.open(image_name)
    # create a cropped image
    cropped = image.crop((x1, y1, x2, y2))
    # show cropped image
    cropped.show()
    
# flipping image
def flip_image(image_name):
    # load image
    image = Image.open(image_name)
    # horizontal flip
    hoz_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
    # vertical flip
    ver_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
    # plot all three images using matplotlib
    # row, column, index
    pyplot.subplot(131)
    pyplot.imshow(image)
    pyplot.subplot(132)
    pyplot.imshow(hoz_flip)
    pyplot.subplot(133)
    pyplot.imshow(ver_flip)
    pyplot.show()

# resizing image and preserve aspect ratio
def resize_image_as_a_thumbnail(image_name, width, height):
    image = Image.open(image_name)
    # report the size of the image
    print(image.size)
    # create a thumbnail and preserve aspect ratio
    image.thumbnail((width, height))
    # report the size of the modified image
    print(image.size)
    # show the image
    image.show()
    
# resizing image and forcing an aspect ratio
def resize_image(image_name, width, height):
    # load the image
    image = Image.open(image_name)
    # report the size of the image
    print(image.size)
    # resize image and ignore original aspect ratio
    img_resized = image.resize((width, height))
    # report the size of the thumbnail
    print(img_resized.size)
    # show the image
    img_resized.show()

def rotate_image(image_name, degree):
    # load image
    image = Image.open(image_name)
    pyplot.subplot(111)
    pyplot.imshow(image.rotate(degree))
    pyplot.show()

#------------------------------------------------------------------------------ 
# TOP-MODULES
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# TESTBENCHS
#------------------------------------------------------------------------------
# testbench for convert_images_to_numpy_array(directory_name)
def tb_convert_images_to_numpy_array():
    directory_name = 'Image'
    convert_images_to_numpy_array(directory_name)

# testbench for load_image(image_name)
def tb_load_image():
    load_image('opera_house.jpg')

# testbench for crop_image
def tb_crop_image():
    crop_image('opera_house.jpg', 100, 100, 200, 300)

# testbench for flip_image(image_name)
def tb_flip_image():
    flip_image('opera_house.jpg')

# testbench for resize_image_as_a_thumbnail(image_name, width, height)
def tb_resize_image_as_a_thumbnail():
    resize_image_as_a_thumbnail('opera_house.jpg', 200, 200)
    
# testbench for resize_image(image_name, width, height)
def tb_resize_image():
    resize_image('opera_house.jpg', 200, 200)

# testbench for rotate_image(image_name, degree)
def tb_rotate_image():
    rotate_image('opera_house.jpg', 45)

    
#------------------------------------------------------------------------------
# MAIN FUNCTIONS
#------------------------------------------------------------------------------

if __name__ == "__main__":
    #tb_convert_images_to_numpy_array()
    #tb_crop_image()
    #tb_load_image()
    #tb_flip_image()
    #tb_resize_image_as_a_thumbnail()
    #tb_resize_image()
    #tb_rotate_image()
    
    
    
