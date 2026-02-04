n = int(input("Nhap so 5 chu so: "))
max_val = 0
for i in range(5):
    chu_so = n % 10
    if chu_so > max_val:
        max_val = chu_so
    n = n // 10
print("Chu so lon nhat la:", max_val)
