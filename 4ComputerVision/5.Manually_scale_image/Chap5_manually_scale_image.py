# -*- coding: utf-8 -*-
"""
Created on Fri May 27 17:00:27 2022

@author: ADMIN
"""

#------------------------------------------------------------------------------
# to load library
#------------------------------------------------------------------------------

from PIL import Image
from numpy import asarray
from numpy import clip


#------------------------------------------------------------------------------
# SUBMODULES
#------------------------------------------------------------------------------

# load an image with Matplotlib
def load_image(image_name):
    image = Image.open(image_name)
    # summarize some details about the image
    print(image.format)
    print(image.mode)
    print(image.size)
    # show the image
    image.show()
    
# normalizing pixel values
def normalizing_pixel_values(image_name):
    # load image
    image = Image.open(image_name)
    pixels = asarray(image)
    # confirm pixel range is 0-255
    print('Data Type: %s' %pixels.dtype)
    print('Min: %.3f, Max: %.3f' %(pixels.min(), pixels.max()))
    # convert from integers to floats
    pixels = pixels.astype('float32')
    # normalize to the range 0-1
    pixels /= 255.0
    # confirm the normalization
    print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))

# Centering Pixel Values 
def global_centering(image_name):
    # load image
    image = Image.open(image_name)
    pixels = asarray(image)
    # convert from integers to floats
    pixels = pixels.astype('float32')
    # calculate global mean
    mean = pixels.mean()
    print('Mean: %.3f' % mean)
    print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))
    # global centering of pixels
    pixels = pixels - mean
    # confirm it had the desired effect
    mean = pixels.mean()
    print('Mean: %.3f' % mean)
    print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))

def local_centering(image_name):
    # load image
    image = Image.open(image_name)
    pixels = asarray(image)
    # convert from integers to floats
    pixels = pixels.astype('float32')
    # calculate per-channel means and standard deviations
    means = pixels.mean(axis=(0,1), dtype='float64')
    print('Means: %s' % means)
    print('Mins: %s, Maxs: %s' % (pixels.min(axis=(0,1)), pixels.max(axis=(0,1))))
    # per-channel centering of pixels
    pixels -= means
    # confirm it had the desired effect
    means = pixels.mean(axis=(0,1), dtype='float64')
    print('Means: %s' % means)
    print('Mins: %s, Maxs: %s' % (pixels.min(axis=(0,1)), pixels.max(axis=(0,1))))

# Standardizing Pixel Values
def global_standardization(image_name):
    # load image
    image = Image.open(image_name)
    pixels = asarray(image)
    # convert from integers to floats
    pixels = pixels.astype('float32')
    # calculate global mean and standard deviation
    mean, std = pixels.mean(), pixels.std()
    print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
    # global standardization of pixels
    pixels = (pixels - mean) / std
    # confirm it had the desired effect
    mean, std = pixels.mean(), pixels.std()
    print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
    
def positive_global_standardization(image_name):
    # load image
    image = Image.open(image_name)
    pixels = asarray(image)
    # convert from integers to floats
    pixels = pixels.astype('float32')
    # calculate global mean and standard deviation
    mean, std = pixels.mean(), pixels.std()
    print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
    # global standardization of pixels
    pixels = (pixels - mean) / std
    # clip pixel values to [-1,1]
    pixels = clip(pixels, -1.0, 1.0)
    # shift from [-1,1] to [0,1] with 0.5 mean
    pixels = (pixels + 1.0) / 2.0
    # confirm it had the desired effect
    mean, std = pixels.mean(), pixels.std()
    print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
    print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))

def local_standardization(image_name):
    # load image
    image = Image.open(image_name)
    pixels = asarray(image)
    # convert from integers to floats
    pixels = pixels.astype('float32')
    # calculate per-channel means and standard deviations
    means = pixels.mean(axis=(0,1), dtype='float64')
    stds = pixels.std(axis=(0,1), dtype='float64')
    print('Means: %s, Stds: %s' % (means, stds))
    # per-channel standardization of pixels
    pixels = (pixels - means) / stds
    # confirm it had the desired effect
    means = pixels.mean(axis=(0,1), dtype='float64')
    stds = pixels.std(axis=(0,1), dtype='float64')
    print('Means: %s, Stds: %s' % (means, stds))
    

#------------------------------------------------------------------------------ 
# TOP-MODULES
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# TESTBENCHS
#------------------------------------------------------------------------------

# testbench for load_image(image_name)
def tb_load_image():
    load_image('sydney_bridge.jpg')
    
# testbench for normalizing_pixel_values(image_name)
def tb_normalizing_pixel_values():
    normalizing_pixel_values('sydney_bridge.jpg')

# testbench for global_centering(image_name)
def tb_global_centering():
    global_centering('sydney_bridge.jpg')

# testbench for local_centering(image_name)
def tb_local_centering():
    local_centering('sydney_bridge.jpg')
    
# testbench for global_standardization(image_name)
def tb_global_standardization():
    global_standardization('sydney_bridge.jpg')
    
# testbench for positive_global_standardization(image_name)
def tb_positive_global_standardization():
    positive_global_standardization('sydney_bridge.jpg')
    
# testbench for local_standardization(image_name)
def tb_local_standardization():
    local_standardization('sydney_bridge.jpg')

#------------------------------------------------------------------------------
# MAIN FUNCTIONS
#------------------------------------------------------------------------------

if __name__ == "__main__":
    tb_load_image()
    #tb_normalizing_pixel_values()
    #tb_global_centering()
    #tb_local_centering()
    #tb_global_standardization()
    #tb_positive_global_standardization()
    #tb_local_standardization()