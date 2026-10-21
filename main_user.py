import QLSP   # File QLSP.py
from muaHang import ban_san_pham  # File muaHang.py

def menu_user():
    while True:
        print("\n╔════════════════════════════════════════════╗")
        print("║          CỬA HÀNG TIỆN LỢI – KHÁCH HÀNG    ║")
        print("╠════════════════════════════════════════════╣")
        print("║ 1. Xem danh sách sản phẩm                  ║")
        print("║ 2. Tìm kiếm sản phẩm                       ║")
        print("║ 3. Mua sản phẩm                            ║")
        print("║ 4. Thoát                                   ║")
        print("╚════════════════════════════════════════════╝")
        chon = input("Chọn chức năng (1-4): ")
        print("-" * 77)

        if chon == '1':
            QLSP.hien_thi_danh_sach()
        elif chon == '2':
            QLSP.tim_san_pham()
        elif chon == '3':
            ban_san_pham()
        elif chon == '4':
            print("Cảm ơn bạn đã ghé thăm cửa hàng.")
            break
        else:
            print("Vui lòng chọn đúng từ 1-4.")


