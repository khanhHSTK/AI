def thay_the(doan_van, cu, moi):
    if cu == "":
        return doan_van
    kq = []
    i, n = 0, len(cu)
    while i < len(doan_van):
        if doan_van[i:i + n] == cu:
            kq.append(moi)
            i += n
        else:
            kq.append(doan_van[i])
            i += 1
    return "".join(kq)


doan_van = input("Nhập đoạn văn: ")
cu = input("Nhập từ cần thay (vd: data): ")
moi = input("Nhập từ thay thế (vd: dữ liệu): ")
print("Chuỗi mới:", thay_the(doan_van, cu, moi))