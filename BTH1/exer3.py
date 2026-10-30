if __name__ == '__main__':
    t = input("Nhập số nguyên dương chẵn (s để dừng): ")

    tong = 0
    mylist = []

    while True:
        mylist.append(t)
        if not t.isdigit():
            break
        if int(t) < 0 or int(t) % 2 != 0:
            print("Đây không phải số chẵn / nguyên dương")
            t = input()
        else:
            tong += int(t)
            t = input()

    print(mylist)
    print(tong)