import pandas as pd
df = pd.DataFrame({
    "Ten":  ["An", "Binh", None, "An"],
    "Diem": [8.0, 7.0, 6.0, 8.0],
})
print(df)
print(df.duplicated().sum())
df1 = df.copy()
kq = df1.dropna()
print(kq)
print(df1)
df2 = df.copy()
kq2 = df2.dropna(inplace=True)
print(kq2)
print(df2)
df3 = df.copy()
df3.rename(columns={"Ten": "HoTen"}, inplace=True)
df3.drop(columns="Diem", inplace=True)
print(df3)