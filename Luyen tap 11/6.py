n = int(input("Bao nhieu nguoi: "))
ds = {}
for i in range(n):
    ten = input(f"Nhap ten nguoi thu {i+1}: ")
    tuoi = int(input("Bao nhieu tuoi: "))
    ds[ten] = tuoi
tong = sum(ds.values())
tbc = tong / n
print("tuoi trung binh:", tbc)
ds_list = list(ds.items())
for i in range(len(ds_list)):
    max_idx = i
    for j in range(i+1, len(ds_list)):
        if ds_list[j][1] > ds_list[max_idx][1]:
            max_idx = j
    ds_list[i], ds_list[max_idx] = ds_list[max_idx], ds_list[i]
print("Danh sach sau sap xep:")
for ten, tuoi in ds_list:
    print(ten, ":", tuoi)