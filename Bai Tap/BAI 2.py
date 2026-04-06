numbers = list(map(int, input("Nhap day so (cach nhau boi dau cach): ").split()))
so_le = []
for n in numbers:
    if n % 2 != 0:
        so_le.append(n)
print("Cac so le:", so_le)
print("So luong so le:", len(so_le))