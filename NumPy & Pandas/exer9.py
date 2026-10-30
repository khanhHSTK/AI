import numpy as np
ds = [15, 32, 10, 32, 29, 48, 21]
v = np.array(ds)
print(v)
print(v.size)
print(v.ndim)
v = np.insert(v, 1, 55)
print(v)
m = v.reshape(4, 2)
print(m)
print(v[1::2])