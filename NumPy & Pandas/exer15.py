from asyncio.windows_events import NULL

import pandas as pd

df = pd.read_csv("C:\\Users\\admin\\Desktop\\AI\\sinhvien.csv", sep=";")
#print(df.head())

df.columns = ["ID", "Name", "BDD", "Gender", "Mark", "Class"]
df["Gender"] = df["Gender"].astype(str).str.strip()

# print(df["Gender"].value_counts())

# print(df.groupby(["Class", "Gender"]).size().unstack(fill_value=0))

df.rename(columns={"ID": "MS", "Name": "Ten", "BDD": "NgaySinh", "Gender": "GT", "Mark": "Diem", "Class": "Lop"}, inplace=True)

#print(df.head())

#print(df[(df["GT"] == "F") & (df["Diem"] > 7)])

#print(df[df["Diem"].isna()].sort_values("MS"))

diem_min = df["Diem"].min()
df["Diem"] = df["Diem"].fillna(diem_min)

def xep_loai(d):
    if d >= 8:
        return "Giỏi"
    elif d >= 6:
        return "Khá"
    return "Trung Bình"

df["XepLoai"] = df["Diem"].apply(xep_loai)
print(df.head())

top2 = (df.sort_values("Diem", ascending=False)
          .groupby("Lop")
          .head(2)
          .sort_values(["Lop", "Diem"], ascending=[True, False]))
print(top2[["Ten", "Lop", "Diem"]])

print(df[df["GT"] == "M"]["Diem"].agg(["max", "min", "mean"]))