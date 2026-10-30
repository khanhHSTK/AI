import numpy as np
data = """1 Thanh 20
2 Tam 21
3 Binh 22
4 Chinh 23
5 Lan 21"""
with open("sinhvien.txt", "w", encoding="utf-8") as f:
    f.write(data)
sv = np.loadtxt("sinhvien.txt", delimiter=",", dtype=str, encoding="utf-8")
print(sv)
header = np.array([["Stt", "HoTen", "Tuoi"]])
sv_header = np.vstack((header, sv))
print(sv_header)
np.savetxt("sinhvien_tieude.txt", sv_header, fmt="%s", delimiter=",", encoding="utf-8")
tuoi = sv[:, 2].astype(int)
print("Tuổi trung bình:", tuoi.mean())