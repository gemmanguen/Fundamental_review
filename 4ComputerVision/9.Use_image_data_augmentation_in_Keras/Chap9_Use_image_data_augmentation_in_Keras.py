#------------------------------------------------------------------------------
# to load library
#------------------------------------------------------------------------------
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot


#------------------------------------------------------------------------------
# SUBMODULES
#------------------------------------------------------------------------------
# example of horizontal shift image augmentation

def horizontal_shift(img_name):
    # load the image
    img = load_img(img_name)
    # convert to numpy array
    data = img_to_array(img)
    # expand dimension to one sample
    samples = expand_dims(data, 0)
    # create image data augmentation generator
    datagen = ImageDataGenerator(width_shift_range=[-200,200])
    # prepare iterator
    it = datagen.flow(samples, batch_size=1)
    # generate samples and plot
    for i in range(9):
        # define subplot
        pyplot.subplot(330 + 1 + i)
        # generate batch of images
        batch = it.next()
        # convert to unsigned integers for viewing
        image = batch[0].astype('uint8')
        # plot raw pixel data
        pyplot.imshow(image)
    # show the figure
    pyplot.show()
    
# example of vertical shift image augmentation
def vertical_shift(img_name):
    # load the image
    img = load_img(img_name)
    # convert to numpy array
    data = img_to_array(img)
    # expand dimension to one sample
    samples = expand_dims(data, 0)
    # create image data augmentation generator
    datagen = ImageDataGenerator(height_shift_range=0.5)
    # prepare iterator
    it = datagen.flow(samples, batch_size=1)
    # generate samples and plot
    for i in range(9):
        # define subplot
        pyplot.subplot(330 + 1 + i)
        # generate batch of images
        batch = it.next()
        # convert to unsigned integers for viewing
        image = batch[0].astype('uint8')
        # plot raw pixel data
        pyplot.imshow(image)
    # show the figure
    pyplot.show()

#horizontal flips

def horizontal_flip(img_name):
    # load the image
    img = load_img(img_name)
    # convert to numpy array
    data = img_to_array(img)
    # expand dimension to one sample
    samples = expand_dims(data, 0)
    # create image data augmentation generator
    datagen = ImageDataGenerator(horizontal_flip=True)
    # prepare iterator
    it = datagen.flow(samples, batch_size=1)
    # generate samples and plot
    for i in range(9):
        # define subplot
        pyplot.subplot(330 + 1 + i)
        # generate batch of images
        batch = it.next()
        # convert to unsigned integers for viewing
        image = batch[0].astype('uint8')
        # plot raw pixel data
        pyplot.imshow(image)
    # show the figure
    pyplot.show()
    
#Random Rotation Augmentation
def rotate_image(img_name):
    # load the image
    img = load_img(img_name)
    # convert to numpy array
    data = img_to_array(img)
    # expand dimension to one sample
    samples = expand_dims(data, 0)
    # create image data augmentation generator
    datagen = ImageDataGenerator(rotation_range=90)
    # prepare iterator
    it = datagen.flow(samples, batch_size=1)
    # generate samples and plot
    for i in range(9):
        # define subplot
        pyplot.subplot(330 + 1 + i)
        # generate batch of images
        batch = it.next()
        # convert to unsigned integers for viewing
        image = batch[0].astype('uint8')
        # plot raw pixel data
        pyplot.imshow(image)
    # show the figure
    pyplot.show()
    
#Random Brightness Augmentation
def bright_image(img_name):
    # load the image
    img = load_img(img_name)
    # convert to numpy array
    data = img_to_array(img)
    # expand dimension to one sample
    samples = expand_dims(data, 0)
    # create image data augmentation generator
    datagen = ImageDataGenerator(brightness_range=[0.2,1.0])
    # prepare iterator
    it = datagen.flow(samples, batch_size=1)
    # generate samples and plot
    for i in range(9):
        # define subplot
        pyplot.subplot(330 + 1 + i)
        # generate batch of images
        batch = it.next()
        # convert to unsigned integers for viewing
        image = batch[0].astype('uint8')
        # plot raw pixel data
        pyplot.imshow(image)
    # show the figure
    pyplot.show()

#Random Zoom Augmentation
def zoom_img(img_name):
    # load the image
    img = load_img(img_name)
    # convert to numpy array
    data = img_to_array(img)
    # expand dimension to one sample
    samples = expand_dims(data, 0)
    # create image data augmentation generator
    datagen = ImageDataGenerator(zoom_range=[0.5,1.0])
    # prepare iterator
    it = datagen.flow(samples, batch_size=1)
    # generate samples and plot
    for i in range(9):
        # define subplot
        pyplot.subplot(330 + 1 + i)
        # generate batch of images
        batch = it.next()
        # convert to unsigned integers for viewing
        image = batch[0].astype('uint8')
        # plot raw pixel data
        pyplot.imshow(image)
    # show the figure
    pyplot.show()
    
#------------------------------------------------------------------------------ 
# TOP-MODULES
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# TESTBENCHS
#------------------------------------------------------------------------------

# testbench for horizontal_shift(img_name)
def tb_horizontal_shift():
    horizontal_shift('./images/bird.jpg')

def tb_vertical_shift():
    vertical_shift('./images/bird.jpg')
    
# testbench for horizontal_flip(img_name)
def tb_horizontal_flip():
    horizontal_flip('./images/bird.jpg')
    
# testbench for rotate_image(img_name)
def tb_rotate_image():
    rotate_image('./images/bird.jpg')
    
# testbench for bright_image(img_name)
def tb_bright_image():
    bright_image('./images/bird.jpg')

# testbench for zoom_img(img_name)
def tb_zoom_img():
    zoom_img('./images/bird.jpg')
# testbench for 

#------------------------------------------------------------------------------
# MAIN FUNCTIONS
#------------------------------------------------------------------------------
if __name__ == "__main__":
    #tb_horizontal_shift()
    #tb_vertical_shift()
    #tb_horizontal_flip()
    #tb_rotate_image()
    #tb_bright_image()
    tb_zoom_img()
    
    
    