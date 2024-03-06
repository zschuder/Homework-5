import numpy as np

arr_zeros = np.zeros(64).reshape((8,8))
arr_zeros[::2,::2] = 1
arr_zeros[1::2,1::2] = 1
print(arr_zeros)