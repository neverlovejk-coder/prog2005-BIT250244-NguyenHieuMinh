danh_sach = []
for i in range(5):
    chuoi = input(f"Nhap chuoi {i + 1}: ")
    danh_sach.append(chuoi)
print("\nDanh sach ban dau:")
print(danh_sach)
for i in range(1, len(danh_sach)):
    n = danh_sach[i]
    m = i - 1
    while m >= 0 and len(danh_sach[m]) < len(n):
        danh_sach[m + 1] = danh_sach[m]
        m -= 1
    danh_sach[m + 1] = n
    print(f"\nBuoc {i}:")
    print(danh_sach)
print("\nDanh sach sau khi sap xep:")
print(danh_sach)