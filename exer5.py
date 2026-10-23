if __name__ == '__main__':
    mylist = []
    sum = 0

    while True:
        n = input("Nhập số: ")
        if n == '':
            break
        mylist.append(n)
        sum += int(n)

    print(mylist)
    print(sum)

    '''Max = max(x, y, z)
    Min = min(x, y, z)
    '''