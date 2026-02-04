n = int(input("Nhap 1 so: "))
tong = 0
while n > 0:
    tong += n % 10  # Lấy chữ số cuối
    n = n // 10     # Cắt bỏ chữ số cuối
print("Tong cac chu so:", tong)