from main_admin import menu_admin
from main_user import menu_user

def main():
    while True:
        print("\n╔════════════════════════════════════════════╗")
        print("║       CHỌN CHẾ ĐỘ SỬ DỤNG CHƯƠNG TRÌNH     ║")
        print("╠════════════════════════════════════════════╣")
        print("║ 1. Chế độ Quản trị (Admin)                 ║")
        print("║ 2. Chế độ Khách hàng (User)                ║")
        print("║ 3. Thoát                                   ║")
        print("╚════════════════════════════════════════════╝")
        chon = input("Chọn chế độ (1-3): ")

        if chon == '1':
            menu_admin()
        elif chon == '2':
            menu_user()
        elif chon == '3':
            print("Tạm biệt!")
            break
        else:
            print("Vui lòng chọn đúng từ 1-3.")


if __name__ == "__main__":
    main()
