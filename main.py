import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread("images/original.jpg")
print(img.shape)
print(img.dtype)
print(img.min())
print(img.max())
print(img[0,0])