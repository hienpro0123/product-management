import QLSP  

def ban_san_pham():
    ma_mua = input("Nhập mã sản phẩm muốn mua: ")
    tim_duoc = False

    for sp in QLSP.danh_sach_san_pham:
        if sp['ma'] == ma_mua:
            tim_duoc = True
            try:
                so_luong_mua = int(input("Nhập số lượng muốn mua: "))
                if so_luong_mua <= 0:
                    print("Số lượng phải lớn hơn 0.")
                    return
                if so_luong_mua > sp['so_luong']:
                    print("Không đủ hàng trong kho.")
                    return
                sp['so_luong'] -= so_luong_mua
                tong_tien = so_luong_mua * sp['gia']
                QLSP.doanh_thu += tong_tien  # Cập nhật trực tiếp biến trong QLSP
                print(f"Mua thành công {so_luong_mua} sản phẩm. Tổng tiền: {tong_tien:,} VND")
                return
            except ValueError:
                print("Nhập sai định dạng số.")
                return
    if not tim_duoc:
        print("Không tìm thấy sản phẩm.")
