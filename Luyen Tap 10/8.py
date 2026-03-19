ban_dau = []
for i in range(5):
    chuoi = input(f"nhap ki tu {i+1}")
    ban_dau.append(chuoi)
n = len(ban_dau)
for i in range(n):
    hoan_doi = False
    for m in range(0, n - i - 1):
        if len(ban_dau[m]) < len(ban_dau[m + 1]):
            ban_dau[m], ban_dau[m + 1] = ban_dau[m + 1], ban_dau[m]
            hoan_doi = True
    print(f"buoc {i + 1}: {ban_dau}")
    if not hoan_doi:
        break
print("-" * 30)
print(f"doi dai danh sach:\n{ban_dau}")