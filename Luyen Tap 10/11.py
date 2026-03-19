while True:
    print("\n===== MENU =====")
    print("1. bai 7")
    print("0. exit")
    chon = input("chon 1 hoac 0: ")
    if chon == "1":
        print("----Dang chon bai 7----")
        mat_khau = "python123"
        nhap_mat_khau = input("nhap mat khau: ")
        if nhap_mat_khau == mat_khau:
            print("chao mung")
        else:
            print("mat khau sai!")
    elif chon == "0":
        print("tam biet")
        break
    else:
        print("loi lua chon!")
