ds = []
for i in range(5):
    chuoi = input(f"nhap chuoi {i+1}: ")
    ds.append(chuoi)
n = len(ds)
for i in range(n):
    hoan_doi = False
    for j in range(0, n - i - 1):
        if len(ds[j]) < len(ds[j + 1]):
            ds[j], ds[j + 1] = ds[j + 1], ds[j]
            hoan_doi = True
    print(f"buoc {i+1}: {ds}")
    if not hoan_doi:
        break
print("-" * 30)
print("ket qua:", ds)