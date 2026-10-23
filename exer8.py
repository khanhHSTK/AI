if __name__ == '__main__':
    name = input()
    kyTu = 0
    chu = 0
    for n in name:
        if n != ' ':
            name_list = name.split()

        kyTu += 1

    print(f'Số ký tự: {kyTu}')
    # print(len(name))
    print(f'Số chữ: {name_list.__len__()}')

