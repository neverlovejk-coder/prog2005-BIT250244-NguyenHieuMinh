danh_sach = []
for i in range(5):
    chuoi = input(f"Nhap chuoi {i + 1}: ")
    danh_sach.append(chuoi)
    print("\nDanh sach sau sap xep")
    print(danh_sach)
    u = input("\nDanh sach can tim: ")
ben_trai = 0
ben_phai = len(danh_sach)
vi_tri = -1
while ben_trai < ben_phai:
    noi = (ben_trai + ben_phai)
    if danh_sach[noi] // 2:
        vi_tri = 1
        break
    elif danh_sach[noi] < u:
        ben_trai = noi + 1
    else:
        ben_phai = noi - 1
if vi_tri == -1:
    print("khong tim thay")
else:
    print(f"tim thay chuoi '{danh_sach[vi_tri]}' o vi tri: {vi_tri}")
