CHU_SO = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
DON_VI = ["", " nghìn", " triệu", " tỷ", " nghìn tỷ", " triệu tỷ"]

def doc_nhom_3(n, day_du):
    tram, chuc, dv = n // 100, (n // 10) % 10, n % 10
    kq = []
    if tram > 0 or day_du:
        kq.append(CHU_SO[tram] + " trăm")
    if chuc == 0:
        if dv > 0:
            if tram > 0 or day_du:
                kq.append("linh")
            kq.append(CHU_SO[dv])
    elif chuc == 1:
        kq.append("mười")
        if dv == 5:
            kq.append("lăm")
        elif dv > 0:
            kq.append(CHU_SO[dv])
    else:
        kq.append(CHU_SO[chuc] + " mươi")
        if dv == 1:
            kq.append("mốt")
        elif dv == 4:
            kq.append("tư")
        elif dv == 5:
            kq.append("lăm")
        elif dv > 0:
            kq.append(CHU_SO[dv])
    return " ".join(kq)

def doc_so(so):
    if so == 0:
        return "Không"
    am = so < 0
    so = abs(so)
    nhom = []
    while so > 0:
        nhom.append(so % 1000)
        so //= 1000

    parts = []
    for i in range(len(nhom) - 1, -1, -1):
        if nhom[i] == 0:
            continue
        la_nhom_dau = (i == len(nhom) - 1)
        parts.append(doc_nhom_3(nhom[i], not la_nhom_dau) + DON_VI[i])
    kq = " ".join(parts)
    if am:
        kq = "âm " + kq
    return kq[0].upper() + kq[1:]

def bai11():
    try:
        so = int(input("Nhập một số nguyên: "))
    except ValueError:
        print("Giá trị nhập không hợp lệ!")
        return
    print(doc_so(so))