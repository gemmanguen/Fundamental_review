

# create flipped versions of an image
from PIL import Image
from matplotlib import pyplot
# load image
image = Image.open("opera_house.jpg")
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
