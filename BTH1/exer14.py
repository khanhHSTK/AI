TEN_FILE = "vanban.txt"
NOI_DUNG = (
    "Phân tích dữ liệu là một quá trình kiểm tra, làm sạch, chuyển đổi và mô "
    "hình hóa dữ liệu với mục tiêu khám phá thông tin hữu ích, thông báo kết "
    "luận và hỗ trợ ra quyết định. Phân tích dữ liệu có nhiều khía cạnh và cách "
    "tiếp cận, bao gồm các kỹ thuật đa dạng dưới nhiều tên khác nhau và được "
    "sử dụng trong các lĩnh vực kinh doanh, khoa học và khoa học xã hội khác nhau."
)

def dem_cum(van_ban, cum):
    """Đếm số lần cụm từ xuất hiện (không phân biệt hoa/thường, không dùng count)."""
    vb, c = van_ban.lower(), cum.lower()
    dem, i = 0, 0
    while i <= len(vb) - len(c):
        if vb[i:i + len(c)] == c:
            dem += 1
            i += len(c)
        else:
            i += 1
    return dem


def bai14():
    with open(TEN_FILE, "w", encoding="utf-8") as f:
        f.write(NOI_DUNG)
    print(f"Đã tạo file {TEN_FILE}")

    with open(TEN_FILE, "r", encoding="utf-8") as f:
        van_ban = f.read()
    print("\nNội dung file:\n" + van_ban)

    so_chu = len(van_ban.split())
    so_ky_tu = len(van_ban)
    so_ky_tu_khong_cach = len(van_ban.replace(" ", "").replace("\n", ""))
    print(f"\nSố chữ: {so_chu}")
    print(f"Số ký tự (cả khoảng trắng): {so_ky_tu}")
    print(f"Số ký tự (không tính khoảng trắng): {so_ky_tu_khong_cach}")

    print('Số lần xuất hiện "dữ liệu":', dem_cum(van_ban, "dữ liệu"))

    cau_dau = "Khái niệm về phân tích dữ liệu ứng dụng trong doanh nghiệp"
    van_ban = cau_dau + "\n" + van_ban

    cau_cuoi = "Phân tích dữ liệu đã mang lại nhiều lợi ích cho doanh nghiệp trong việc tìm ra các giá trị từ dữ liệu"
    van_ban = van_ban + "\n" + cau_cuoi

    with open(TEN_FILE, "w", encoding="utf-8") as f:
        f.write(van_ban)

    with open(TEN_FILE, "r", encoding="utf-8") as f:
        print("\nNội dung file sau khi chèn đầu/cuối:\n" + f.read())