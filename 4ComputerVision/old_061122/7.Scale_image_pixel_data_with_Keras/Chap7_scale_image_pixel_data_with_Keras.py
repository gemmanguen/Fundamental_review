

#------------------------------------------------------------------------------
# to load library
#------------------------------------------------------------------------------
# load and summarize the MNIST dataset
from keras.datasets import mnist
from keras.preprocessing.image import ImageDataGenerator

#------------------------------------------------------------------------------
# SUBMODULES
#------------------------------------------------------------------------------
def load_MNIST_dataset_and_summarize_dataset():   
    # load dataset
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    # summarize dataset shape
    print('Train', train_images.shape, train_labels.shape)
    print('Test', (test_images.shape, test_labels.shape))
    # summarize pixel values
    print('Train', train_images.min(), train_images.max(), train_images.mean(),
    train_images.std())
    print('Test', test_images.min(), test_images.max(), test_images.mean(), test_images.std())

def normalize_images_with_ImageDataGenerator():
    # load dataset
    (trainX, trainY), (testX, testY) = mnist.load_data()
    # reshape dataset to have a single channel
    width, height, channels = trainX.shape[1], trainX.shape[2], 1
    trainX = trainX.reshape((trainX.shape[0], width, height, channels))
    testX = testX.reshape((testX.shape[0], width, height, channels))
    # confirm scale of pixels
    print('Train min=%.3f, max=%.3f' % (trainX.min(), trainX.max()))
    print('Test min=%.3f, max=%.3f' % (testX.min(), testX.max()))
    # create generator (1.0/255.0 = 0.003921568627451)
    datagen = ImageDataGenerator(rescale=1.0/255.0)
    # Note: there is no need to fit the generator in this case
    # prepare a iterators to scale images
    train_iterator = datagen.flow(trainX, trainY, batch_size=64)
    test_iterator = datagen.flow(testX, testY, batch_size=64)
    print('Batches train=%d, test=%d' % (len(train_iterator), len(test_iterator)))
    # confirm the scaling works
    batchX, batchy = train_iterator.next()
    print('Batch shape=%s, min=%.3f, max=%.3f' % (batchX.shape, batchX.min(), batchX.max()))
    
def centering_images_with_ImageDataGenerator():
    # load dataset
    (trainX, trainy), (testX, testy) = mnist.load_data()
    # reshape dataset to have a single channel
    width, height, channels = trainX.shape[1], trainX.shape[2], 1
    trainX = trainX.reshape((trainX.shape[0], width, height, channels))
    testX = testX.reshape((testX.shape[0], width, height, channels))
    # report per-image mean
    print('Means train=%.3f, test=%.3f' % (trainX.mean(), testX.mean()))
    # create generator that centers pixel values
    datagen = ImageDataGenerator(featurewise_center=True)
    # calculate the mean on the training dataset
    datagen.fit(trainX)
    print('Data Generator Mean: %.3f' % datagen.mean)
    # demonstrate effect on a single batch of samples
    iterator = datagen.flow(trainX, trainy, batch_size=64)
    # get a batch
    batchX, batchy = iterator.next()
    # mean pixel value in the batch
    print(batchX.shape, batchX.mean())
    # demonstrate effect on entire training dataset
    iterator = datagen.flow(trainX, trainy, batch_size=len(trainX), shuffle=False)# get a batch
    batchX, batchy = iterator.next()
    # mean pixel value in the batch
    print(batchX.shape, batchX.mean())
    
def Standardize_images_with_ImageDataGenerator():
    # load dataset
    (trainX, trainy), (testX, testy) = mnist.load_data()
    # reshape dataset to have a single channel
    width, height, channels = trainX.shape[1], trainX.shape[2], 1
    trainX = trainX.reshape((trainX.shape[0], width, height, channels))
    testX = testX.reshape((testX.shape[0], width, height, channels))
    # report pixel means and standard deviations
    print('Statistics train=%.3f (%.3f), test=%.3f (%.3f)' % (trainX.mean(), trainX.std(),
    testX.mean(), testX.std()))
    # create generator that centers pixel values
    datagen = ImageDataGenerator(featurewise_center=True, featurewise_std_normalization=True)
    # calculate the mean on the training dataset
    datagen.fit(trainX)
    print('Data Generator mean=%.3f, std=%.3f' % (datagen.mean, datagen.std))
    # demonstrate effect on a single batch of samples
    iterator = datagen.flow(trainX, trainy, batch_size=64)
    # get a batch
    batchX, batchy = iterator.next()
    # pixel stats in the batch
    print(batchX.shape, batchX.mean(), batchX.std())
    # demonstrate effect on entire training dataset
    iterator = datagen.flow(trainX, trainy, batch_size=len(trainX), shuffle=False)
    # get a batch
    batchX, batchy = iterator.next()
    # pixel stats in the batch
    print(batchX.shape, batchX.mean(), batchX.std())
    
    
#------------------------------------------------------------------------------ 
# TOP-MODULES
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# TESTBENCHS
#------------------------------------------------------------------------------

# testbench for load_MNIST_dataset_and_summarize_dataset()
def tb_load_MNIST_dataset_and_summarize_dataset():
    load_MNIST_dataset_and_summarize_dataset()

# testbench for normalize_images_with_ImageDataGenerator()
def tb_normalize_images_with_ImageDataGenerator():
    normalize_images_with_ImageDataGenerator()
    
# testbench for centering_images_with_ImageDataGenerator()
def tb_centering_images_with_ImageDataGenerator():
    centering_images_with_ImageDataGenerator()
    
# testbench for Standardize_images_with_ImageDataGenerator()
def tb_Standardize_images_with_ImageDataGenerator():
    Standardize_images_with_ImageDataGenerator()
    
# testbench for 


#------------------------------------------------------------------------------
# MAIN FUNCTIONS
#------------------------------------------------------------------------------
if __name__ == "__main__":
    #tb_load_MNIST_dataset_and_summarize_dataset()
    #tb_normalize_images_with_ImageDataGenerator()
    #tb_centering_images_with_ImageDataGenerator()
    tb_Standardize_images_with_ImageDataGenerator()
    
    