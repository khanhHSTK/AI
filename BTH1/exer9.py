if __name__ == '__main__':
    van = input('Nhập đoạn văn: ')
    key = input("Nhập keyword: ")
    van_list = van.split()
    dem = 0
    for line in van_list:
        if key in line:
            dem += 1

    print(f"{key} xuất hiện {dem} lần")