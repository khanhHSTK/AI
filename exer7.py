if __name__ == '__main__':
    ds = [15, 32, 10, 32, 29, 48, 15]

    for d in ds:
        if d % 2 == 0:
            continue
        else: ds.remove(d)

    print(ds)