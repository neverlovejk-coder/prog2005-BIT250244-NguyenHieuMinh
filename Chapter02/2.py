n = int(input("Nhap 1 so tu 1-9: "))
for i in range(1, 10):
    print(n, "x", i, "=", n * i)
#2
n = int(input("Nhap 1 so nguyen duong: "))
if n < 2:
    print(n, "Khong la so nguyen to")
else:
    la_so_nguyen_to = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(n, "La so nguyen to")
    else:
        print(n, "Khong la so nguyen to")
