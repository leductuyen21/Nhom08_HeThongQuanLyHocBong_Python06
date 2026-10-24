
def main():
    while True:
        print("\n===== HE THONG QUAN LY HOC BONG =====")
        print("1. Quan ly sinh vien")
        print("2. Quan ly hoc bong")
        print("3. Quan ly ho so")
        print("4. Xet duyet hoc bong")
        print("5. Thong ke")
        print("0. Thoat")

        chon = input("Nhap lua chon: ")

        if chon == "1":
            print("Chuc nang quan ly sinh vien")
        elif chon == "2":
            print("Chuc nang quan ly hoc bong")
        elif chon == "3":
            print("Chuc nang quan ly ho so")
        elif chon == "4":
            print("Chuc nang xet duyet")
        elif chon == "5":
            print("Chuc nang thong ke")
        elif chon == "0":
            print("Tam biet!")
            break
        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()
