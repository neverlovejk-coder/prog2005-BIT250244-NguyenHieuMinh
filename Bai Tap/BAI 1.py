names = []
for i in range(5):
    n = input(f"Nhap ten nguoi thu {i+1}: ")
    names.append(n)
print("Danh sach 5 nguoi:", names)
if len(names) >= 2:
    deleted_name = names.pop(1)
    print(f"Da xoa: {deleted_name}")
print("Danh sach cuoi cung:", names)