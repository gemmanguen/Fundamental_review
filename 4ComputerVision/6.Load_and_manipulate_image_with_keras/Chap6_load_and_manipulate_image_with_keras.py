

#------------------------------------------------------------------------------
# to load library
#------------------------------------------------------------------------------

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import save_img


#------------------------------------------------------------------------------
# SUBMODULES
#------------------------------------------------------------------------------

# loading image with keras
def loading_image(image_name):
    # load the image
    img = load_img(image_name)
    # report details about the image
    print(type(img))
    print(img.format)
    print(img.mode)
    print(img.size)
    # show the image
    img.show()

# Converting an Image to Numpy array
def convert_images_to_numpy_array(image_name):
    # load the image
    img = load_img(image_name)
    print(type(img))
    # convert to numpy array
    img_array = img_to_array(img)
    print(img_array.dtype)
    print(img_array.shape)
    # convert back to image
    img_pil = array_to_img(img_array)
    print(type(img_pil))

# Saving an image
def save_image(image_name):
    # load image as as grayscale
    img = load_img(image_name, color_mode='grayscale')
    # convert image to a numpy array
    img_array = img_to_array(img)
    # save the image with a new filename
    save_img('./images/grayscale.jpg', img_array)
    # load the image to confirm it was saved correctly
    img = load_img('./images/grayscale.jpg')
    print(type(img))
    print(img.format)
    print(img.mode)
    print(img.size)
    img.show()


#------------------------------------------------------------------------------ 
# TOP-MODULES
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# TESTBENCHS
#------------------------------------------------------------------------------

# testbench for loading_image(image_name)
def tb_loading_image():
    loading_image('./images/bondi_beach.jpg')

# testbench for convert_images_to_numpy_array(image_name)
def tb_convert_images_to_numpy_array():
    convert_images_to_numpy_array('./images/bondi_beach.jpg')
    
# testbench for save_image(image_name)
def tb_save_image():
    save_image('./images/bondi_beach.jpg')


#------------------------------------------------------------------------------
# MAIN FUNCTIONS
#------------------------------------------------------------------------------
if __name__ == "__main__":
    #tb_loading_image()
    #tb_convert_images_to_numpy_array()
    tb_save_image()
    
    