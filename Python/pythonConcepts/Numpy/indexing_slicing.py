import numpy as np

a = np.array([6,7,8])

print(a[0:2])
print(a[-1])

a1 = np.array([[6,7,8], [1,2,3], [9,5,0]])

print(a1[1,2])
print(a1[0:2,2])
print(a1[-1])
print(a1[-1,0:2])
print(a1[:,1:3])