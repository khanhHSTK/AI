def tao_ds():
    return {
        1: {"msv": 9253, "ho_ten": "Đặng Thị Lan Anh", "nam_sinh": 2000, "gioi_tinh": "Nữ", "dan_toc": "Hoa"},
        2: {"msv": 7034, "ho_ten": "Nguyễn Thị Phương Anh", "nam_sinh": 2002, "gioi_tinh": "Nữ", "dan_toc": "Kinh"},
        3: {"msv": 6198, "ho_ten": "Trần Anh Tài", "nam_sinh": 2001, "gioi_tinh": "Nam", "dan_toc": "Kinh"},
    }


def in_ds(ds):
    print(f"{'STT':<5}{'MSV':<7}{'Họ và tên':<25}{'Năm sinh':<10}{'Giới tính':<11}{'Dân tộc'}")
    for stt, sv in ds.items():
        print(f"{stt:<5}{sv['msv']:<7}{sv['ho_ten']:<25}{sv['nam_sinh']:<10}{sv['gioi_tinh']:<11}{sv['dan_toc']}")


def bai13():
    ds = tao_ds()
    print("Danh sách ban đầu:")
    in_ds(ds)

    print("\na) Năm sinh của sinh viên STT 1:", ds[1]["nam_sinh"])

    nam = sum(1 for sv in ds.values() if sv["gioi_tinh"] == "Nam")
    nu = sum(1 for sv in ds.values() if sv["gioi_tinh"] == "Nữ")
    print(f"b) Sinh viên nam: {nam}, sinh viên nữ: {nu}")

    ds.pop(3, None)
    print("\nc) Sau khi xóa sinh viên STT 3:")
    in_ds(ds)

    moi = [
        {"msv": 7503, "ho_ten": "Trần Hải Nam", "nam_sinh": 2000, "gioi_tinh": "Nam", "dan_toc": ""},
        {"msv": 3010, "ho_ten": "Đỗ Minh Hạnh", "nam_sinh": 2002, "gioi_tinh": "Nữ", "dan_toc": ""},
    ]
    stt = max(ds) + 1 if ds else 1
    for sv in moi:
        ds[stt] = sv
        stt += 1
    print("\nd) Sau khi thêm 2 sinh viên mới:")
    in_ds(ds)