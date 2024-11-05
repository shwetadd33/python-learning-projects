import numpy as np


a = np.arange(12).reshape(3,4)
print(a)

for x in np.nditer(a,order='C'):
    print(x)

print("\n\n Fortran order is: ")
for x in np.nditer(a,order="F"):
    print(x)

print("\n\n Fortran order with flag is: ")
for x in np.nditer(a,order="F",flags=['external_loop']):
    print(x)

for x in np.nditer(a,op_flags =['readwrite']):
    x[...]=x*x

print(a)

b = np.arange(3,15,4).reshape(3,1)

for x,y in np.nditer([a,b]):
    print(x,y)