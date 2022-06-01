"""
Created on May 27 2022
@author: DUC

"""
#------------------------------------------------------------------------------
# to load library
#------------------------------------------------------------------------------

from os import listdir
from matplotlib import image

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

# cropping an image
def crop_image():
    return

#------------------------------------------------------------------------------ 
# TOP-MODULES
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# TESTBENCHS
#------------------------------------------------------------------------------

# testbench for convert_images_to_numpy_array(directory_name)
def tb_convert_images_to_numpy_array():
    directory_name = 'images'
    convert_images_to_numpy_array(directory_name)

# testbench for crop_image
def tb_crop_image():
    return

#------------------------------------------------------------------------------
# MAIN FUNCTIONS
#------------------------------------------------------------------------------

if __name__ == "__main__":
    #tb_convert_images_to_numpy_array()
    tb_crop_image()