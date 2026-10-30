import numpy as np
import pandas as pd
v = np.array([20, 17, 32, 19, 65])
s = pd.Series(v)
print(s)
s.index = ["a", "b", "c", "d", "e"]
print(s)
print(s.iloc[1])
print(s.tail(3))