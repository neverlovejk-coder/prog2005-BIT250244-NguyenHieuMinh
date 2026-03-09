n = int(input("Nhap so phan tu: "))
a = []
for i in range(n):
    x = int(input("Nhap phan tu: "))
    a.append(x)
for i in range(n-1):
    max_i = i
    for j in range(i+1, n):
        if a[j] > a[max_i]:
            max_i = j
    a[i], a[max_i] = a[max_i], a[i]
    print("Buoc", i+1, ":", a)