import numpy as np
m1 = np.array([[5, 10, 21],
               [11, 23, 18],
               [22, 19, 35]])
m2 = np.array([[50, 10, 41],
               [61, 23, 28],
               [42, 11, 25]])
m3 = np.array([[96, 22, 26],
               [87, 56, 23],
               [90, 75, 32]])
a = np.array([m1, m2, m3])
print(a[0][-2:])
a = a.astype(float)
a[1, :, 0] = a[0].mean()
print(a[2].sum())
a[2, -1, :] = -1
m_new = a[1].copy()
print(m_new.ndim, m_new.shape)
v = m_new.flatten()
v = np.append(v, 45)
v = np.insert(v, 0, 99)
print(v)
lst = a.flatten().tolist()
print(lst)