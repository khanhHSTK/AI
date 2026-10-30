import numpy as np
a = np.array([99, 46, 87, 62, 11, 32])
print("Max:", a.max())
print("Min:", a.min())
print("Tăng dần:", np.sort(a))
print("Vị trí chẵn:", a[::2])
x = a[3]
print(f"Phần tử thứ 4 là {x}:", "số chẵn" if x % 2 == 0 else "số lẻ")
print("Số phần tử chẵn:", np.sum(a % 2 == 0))
mean = a.mean()
print("Mean:", mean)
print("Median:", np.median(a))
print("Tổng:", a.sum())
a = a.astype(float)
a[a == 87] = mean
print(a)
a = np.delete(a, np.where(a == 62))
print(a)