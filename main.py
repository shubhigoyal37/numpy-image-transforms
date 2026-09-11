import matplotlib.image as mpimg
from transforms import grayscale

img = mpimg.imread("images/original.jpg")

gray = grayscale(img)

print(gray.dtype)
print(gray.shape)
print(gray[0,0])
