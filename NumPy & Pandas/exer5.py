import numpy as np
n = np.array([[5, 10, 21],
              [11, 23, 18],
              [22, 19, 35],
              [96, 22 ,26]])
print(n.ndim)
print(n.shape)
print()
print(n[1])
print(n[2])
print()
n2 = n[:, 2]
print(n2)
print()
n3 = n[1:4, 1:3]
print(n3)
print()
n[3][1] = 30
print(n)
print()