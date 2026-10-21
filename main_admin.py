import QLSP   # File QLSP.py
from muaHang import ban_san_pham

def menu_admin():
    while True:
        print("\n╔════════════════════════════════════════════╗")
        print("║           QUẢN LÝ SẢN PHẨM CỬA HÀNG        ║")
        print("╠════════════════════════════════════════════╣")
        print("║ 1. Thêm sản phẩm                           ║")
        print("║ 2. Sửa thông tin sản phẩm                  ║")
        print("║ 3. Xóa sản phẩm                            ║")
        print("║ 4. Tìm kiếm sản phẩm                       ║")
        print("║ 5. Hiển thị danh sách sản phẩm             ║")
        print("║ 6. Bán sản phẩm                            ║")
        print("║ 7. Doanh thu                               ║")
        print("║ 8. Thoát chương trình                      ║")
        print("╚════════════════════════════════════════════╝")
        chon = input("Chọn chức năng (1-8): ")
        print("-" * 77)

        if chon == '1':
            QLSP.them_san_pham()
        elif chon == '2':
            QLSP.sua_san_pham()
        elif chon == '3':
            QLSP.xoa_san_pham()
        elif chon == '4':
            QLSP.tim_san_pham()
        elif chon == '5':
            QLSP.hien_thi_danh_sach()
        elif chon == '6':
            ban_san_pham()
        elif chon == '7':
            print(f"Doanh thu hiện tại: {QLSP.doanh_thu:,} VND")
        elif chon == '8':
            print("Thoát chương trình.")
            break
        else:
            print("Vui lòng chọn đúng từ 1-8.")



