import csv
ten = input("Ten nhan vien: ")
tuoi = input("Tuoi: ")
id_nv = input("ID: ")
with open("nhanvien.txt", "a", encoding="utf-8") as f:
    f.write(f"Ten: {ten}, tuoi: {tuoi}, ID: {id_nv}\n")
with open("nhanvien.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([ten, tuoi, id_nv])
print("\nNoi dung:")
with open("nhanvien.txt", "r", encoding="utf-8") as f:
    print(f.read())
print("noidung CV:")
with open("nhanvien.csv", "r", encoding="utf-8") as f:
    print(f.read())