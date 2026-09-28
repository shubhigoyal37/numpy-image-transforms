import matplotlib.image as mpimg
from transforms import (grayscale,box_blur)

img = mpimg.imread("images/original4.jpg")

# grayscale
gray = grayscale(img)

# print(gray.dtype)
# print(gray.shape)
# print(gray[0,0])

mpimg.imsave("images/grayscale3.png", gray, cmap="gray")

#blur
blurred = box_blur(gray)

print(gray.shape)
print(blurred.shape)

mpimg.imsave("images/blurred.png", blurred, cmap="gray")
