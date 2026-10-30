import pandas as pd
data = [
    [111, "Hong", 20],
    [222, "Tai", 19],
    [333, "Tam", 23],
    [444, "Phuong", 22],
    [555, "Huy", 21],
]
df = pd.DataFrame(data)
df.index = ["SV1", "SV2", "SV3", "SV4", "SV5"]
df.columns = ["MSSV", "HoTen", "Tuoi"]
print(df)
print(df.loc["SV2"])
print(df["HoTen"])
df_new = df[["MSSV", "HoTen"]]
print(df_new)