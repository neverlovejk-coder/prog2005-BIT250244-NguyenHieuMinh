chuoi = input("chuoi: ")
ky_tu_can_dem = input("ky_tu_can_dem: ")
if len(ky_tu_can_dem) != 1:
    print("chi nhap 1 ky tu")
else:
    n = 0
    for chuoi in ky_tu_can_dem:
        n += 1
        print(f"ky tu '{ky_tu_can_dem} xuat hien {n} lan")