if __name__ == '__main__':
    ds = [5, 2, 10, 32, 11, 48, 34]
    tong = 0
    for d in ds:
        if d % 2 != 0:
            continue
        else: tong += d

    print(tong)
