import numpy as np

from numpy.lib.stride_tricks import sliding_window_view

def grayscale(img):
    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]
    gray = 0.2989*r + 0.5870*g + 0.1140*b
    return gray.astype(np.uint8)

def box_blur(gray):
    windows = sliding_window_view(gray, (3, 3))
    blurred = windows.mean(axis=(2,3))
    return blurred.astype(np.uint8)

def resize(img, new_h, new_w):
    old_h, old_w = img.shape[0], img.shape[1]
    row_idx = np.arange(new_h) * old_h // new_h
    col_idx = np.arange(new_w) * old_w // new_w
    return img[row_idx][:, col_idx]
