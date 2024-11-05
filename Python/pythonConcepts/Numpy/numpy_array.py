"""
numpy module is used in scientific computing
numpy array vs Python list :
less memory, Fast and Convenient
"""
import sys
import time

import numpy
import numpy as np

a = np.array([1,2,3])
print(a[1])

# --------------- Memory comparison ----------------------------------
l = range(1000)
print(sys.getsizeof(5)*len(l))

array = numpy.arange(1000)
print(array.size*array.itemsize)

#------------------ Processing time --------------------------------------
size = 100000
l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()

result = [(x+y) for x,y in zip(l1,l2)]

print("List took : ", (time.time()-start)*1000)
#print(result[:4])

start = time.time()

result = a1+a2
print("Numpy array took: ", (time.time()-start)*1000)
#print(result[:4])



