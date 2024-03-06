import numpy as np

np.random.seed(12345)
a = np.random.randint(1, 50, (4, 5))

def sorting(a):
    print("Original array:\n", a)
    a = np.sort(a, axis=0)
    print("Sorted array:\n", a)
print(sorting(a))
