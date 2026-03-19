def tinh_giai_thua(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * tinh_giai_thua(n - 1)
try:
    nhap_so = int(input("nhap so nguyen duong: "))
    if nhap_so < 0:
        print("nhap so lon hon 0!")
    else:
        ket_qua = tinh_giai_thua(nhap_so)
        print(f"giai thua cua {nhap_so} la : {ket_qua}")
except ValueError:
    print("nhap so nguyen !")
