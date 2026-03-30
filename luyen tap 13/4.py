def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
n = int(input("nhap so: "))
if n < 0:
    print("khong nhan so am!")
else:
    print(f"giai thua {n} là:", giai_thua(n))