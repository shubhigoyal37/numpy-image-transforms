import matplotlib.image as mpimg
from transforms import grayscale, box_blur, resize

img = mpimg.imread("images/original.jpg")

gray = grayscale(img)
blurred = box_blur(gray)
resized = resize(gray, 160, 158)

mpimg.imsave("images/grayscale.png", gray, cmap="gray")
mpimg.imsave("images/blurred.png", blurred, cmap="gray")
mpimg.imsave("images/resized.png", resized, cmap="gray")