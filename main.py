import matplotlib.image as mpimg
from transforms import (grayscale,box_blur,resize)

img = mpimg.imread("images/original5.jpg")

# grayscale
gray = grayscale(img)

# print(gray.dtype)
# print(gray.shape)
# print(gray[0,0])

mpimg.imsave("images/grayscale3.png", gray, cmap="gray")

#blur
blurred = box_blur(gray)

mpimg.imsave("images/blurred2.png", blurred, cmap="gray")

#resize

resized = resize(gray, 160, 158)

print(gray.shape)
print(blurred.shape)
print(resized.shape)

mpimg.imsave("images/resized.png", resized, cmap="gray")