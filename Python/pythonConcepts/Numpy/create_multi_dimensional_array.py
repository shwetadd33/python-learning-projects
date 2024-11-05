import numpy
import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a.ndim)
print(a.itemsize)

print(a.dtype)
print(a.shape)

a1 = np.zeros((3, 4))
print(a1)

ones = np.ones((3, 4))
print(ones)

range = np.arange(1, 5)
print(range)

range_1 = np.arange(1, 10, 2)
print(range_1)

print(a.reshape(2,3))

print(a.reshape(6,1))

print(a.ravel())

print(a.min())
print(a.max())
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(np.sqrt(a))

print(np.std(a))

