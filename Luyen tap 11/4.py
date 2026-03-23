ds = [2, 5, 7, 4, 9, 11]
x = int(input("nhap phan tu: "))
ds.append(x)
print("danh sach sau khi them:", ds)
k = int(input("nhap gia tri: "))
dem = ds.count(k)
print(f"so lan xuat hien {k} là:", dem)
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
tong_nt = 0
for i in ds:
    if la_so_nguyen_to(i):
        tong_nt += i
print("tong:", tong_nt)
ds.sort()
print("danh sach sau sap xep:", ds)
ds.clear()
print("danh sach sau sap xep:", ds)