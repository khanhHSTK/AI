import pandas as pd

data = pd.read_csv("student.csv", encoding='utf-8')

'''
print(data)

n = int(input("Nhập n: "))
print(data.head(n))
print(data.tail(n))

print(data['Ten'])
print(data['Tuoi'].head(n))

print(data[["Ten", "Tuoi"]])
print(data.columns)

data = pd.DataFrame(data_dict)

print(data.info())

print(data.describe())

print(data.shape)

print(data.value_counts(dropna=False))

print(data['Ten'].value_counts())

print(data.sort_values(["Tuoi", "Ten"]))

print(data.sort_values(["Ten", "Tuoi", "Diem"], ascending=False))

'''

