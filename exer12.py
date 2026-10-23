import string
def tach_tu(chuoi):
    sach = "".join(c for c in chuoi.lower() if c not in string.punctuation)
    return sach.split()


def tu_chung(chuoi1, chuoi2):
    tap2 = set(tach_tu(chuoi2))
    kq = []
    for t in tach_tu(chuoi1):
        if t in tap2 and t not in kq:
            kq.append(t)
    return kq


def bai12():
    s1 = input("Nhập chuỗi 1: ")
    s2 = input("Nhập chuỗi 2: ")
    kq = tu_chung(s1, s2)
    print("Các từ chung:", ", ".join(kq) if kq else "(không có)")