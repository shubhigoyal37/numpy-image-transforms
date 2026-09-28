import numpy as np
tiny = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

from numpy.lib.stride_tricks import sliding_window_view
windows = sliding_window_view(tiny, (3, 3))

# print(windows.shape)
# print(windows[0, 0])
# print(windows[1, 1])
print(windows.mean(axis=(2, 3)))
print(windows.mean(axis=1))
print(windows.mean(axis=(1, 3)))