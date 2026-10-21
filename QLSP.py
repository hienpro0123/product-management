import datetime

# Danh sách sản phẩm và doanh thu
danh_sach_san_pham = []
doanh_thu = 0

# Hàm kiểm tra hạn sử dụng sản phẩm
def tinh_trang_san_pham(hsd):
    today = datetime.date.today()
    if hsd >= today:
        return "Còn hạn"
    else:
        return "Hết hạn"

# Hàm thêm sản phẩm
def them_san_pham():
    ma = input("Nhập mã sản phẩm: ")
    ten = input("Nhập tên sản phẩm: ")
    loai = input("Nhập loại sản phẩm: ")
    gia = float(input("Nhập giá sản phẩm: "))
    so_luong = int(input("Nhập số lượng tồn kho: "))
    han_su_dung = input("Nhập hạn sử dụng (định dạng YYYY-MM-DD): ")

    try:
        ngay_hsd = datetime.datetime.strptime(han_su_dung, "%Y-%m-%d").date()
    except ValueError:
        print("Ngày không hợp lệ. Sản phẩm không được thêm.")
        return

    sp = {
        "ma": ma,
        "ten": ten,
        "loai": loai,
        "gia": gia,
        "so_luong": so_luong,
        "hsd": ngay_hsd
    }
    danh_sach_san_pham.append(sp)
    print("Đã thêm sản phẩm thành công.")

# Hàm sửa thông tin sản phẩm
def sua_san_pham():
    ma = input("Nhập mã sản phẩm cần sửa: ")
    for sp in danh_sach_san_pham:
        if sp["ma"] == ma:
            print("Nhập thông tin mới (bỏ trống nếu không muốn thay đổi):")

            ten_moi = input(f"Tên ({sp['ten']}): ").strip()
            loai_moi = input(f"Loại ({sp['loai']}): ").strip()
            gia_moi = input(f"Giá ({sp['gia']}): ").strip()
            so_luong_moi = input(f"Số lượng ({sp['so_luong']}): ").strip()
            hsd_moi = input(f"HSD ({sp['hsd']} - dạng YYYY-MM-DD): ").strip()

            try:
                if ten_moi:
                    sp['ten'] = ten_moi
                if loai_moi:
                    sp['loai'] = loai_moi
                if gia_moi:
                    sp['gia'] = float(gia_moi)
                if so_luong_moi:
                    sp['so_luong'] = int(so_luong_moi)
                if hsd_moi:
                    sp['hsd'] = datetime.datetime.strptime(hsd_moi, "%Y-%m-%d").date()

                print("Sửa thông tin sản phẩm thành công.")
            except ValueError:
                print("Lỗi: Dữ liệu nhập không hợp lệ. Vui lòng kiểm tra lại.")
            return
    print("Không tìm thấy sản phẩm.")

# Hàm xóa sản phẩm
def xoa_san_pham():
    ma = input("Nhập mã sản phẩm cần xóa: ")
    for sp in danh_sach_san_pham:
        if sp["ma"] == ma:
            danh_sach_san_pham.remove(sp)
            print("Đã xóa sản phẩm.")
            return
    print("Không tìm thấy sản phẩm.")

# Hàm tìm sản phẩm
def tim_san_pham():
    tu_khoa = input("Nhập tên hoặc mã sản phẩm để tìm: ").lower()
    ket_qua = [sp for sp in danh_sach_san_pham if tu_khoa in sp["ten"].lower() or tu_khoa in sp["ma"].lower()]
    if not ket_qua:
        print("Không tìm thấy sản phẩm.")
    else:
        print(f"Tìm thấy {len(ket_qua)} sản phẩm:")
        for sp in ket_qua:
            in_thong_tin(sp)

# In tiêu đề bảng
def in_tieu_de():
    print(f"{'Mã':<8}{'Tên':<20}{'Loại':<15}{'Giá':<10}{'SL':<6}{'HSD':<12}{'Tình trạng':<12}{'Trạng thái':<12}")
    print("-" * 95)

# In thông tin 1 sản phẩm
def in_thong_tin(sp):
    tinh_trang = tinh_trang_san_pham(sp['hsd'])
    trang_thai = "Còn hàng" if sp['so_luong'] > 0 else "Hết hàng"
    print(f"{sp['ma']:<8}{sp['ten']:<20}{sp['loai']:<15}{sp['gia']:<10}{sp['so_luong']:<6}{str(sp['hsd']):<12}{tinh_trang:<12}{trang_thai:<12}")
    print("-" * 95)

# Hiển thị danh sách sản phẩm
def hien_thi_danh_sach():
    if not danh_sach_san_pham:
        print("Danh sách sản phẩm trống.")
        return
    print("DANH SÁCH SẢN PHẨM:")
    in_tieu_de()
    for sp in danh_sach_san_pham:
        in_thong_tin(sp)
