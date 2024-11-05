import numpy as np

a = np.array([[6,7,8], [1,2,3], [9,5,0]])

for row in a:
    print(row)

for cell in a.flat:
    print(cell)


x = np.arange(6).reshape(3,2)
y = np.arange(6,12).reshape(3,2)
print(np.vstack((x,y)))
print(np.hstack((x,y)))

