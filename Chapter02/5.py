chuoi = input("Nhap chuoi: ")
ky_tu = input("Nhap ki tu: ")
dem = 0
for c in chuoi:
    if c == ky_tu:
        dem += 1
print("So la xuat hien:", dem)
