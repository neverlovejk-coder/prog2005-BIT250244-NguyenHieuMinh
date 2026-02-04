n = int(input("Nhap so nguyen duong: "))
dao_nguoc = 0
while n > 0:
    chu_so_cuoi = n % 10
    dao_nguoc = dao_nguoc * 10 + chu_so_cuoi
    n = n // 10
print("So dao nguoc:", dao_nguoc)