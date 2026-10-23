if __name__ == '__main__':
    t = input("Nhập số (hoặc nhập 'e'/'E' để dừng): ")
    tong = 0
    while t != 'e' and t != 'E':
        tong += int(t)
        t = input()

    print(tong)