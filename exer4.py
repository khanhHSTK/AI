if __name__ == '__main__':
    n = int(input("Nhập số cần tính: "))
    tong = 0

    for i in range(1, n + 1):
        tong += i

    print(tong)