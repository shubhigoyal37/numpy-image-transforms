import numpy as np

def grayscale(img):
    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]
    gray = 0.2989*r + 0.5870*g + 0.1140*b
    return gray.astype(np.uint8)