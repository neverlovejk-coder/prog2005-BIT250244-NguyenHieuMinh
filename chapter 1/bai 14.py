import math

try:
    n = float(input("Nhập một số: "))
    if n < 0:
        print("Lỗi: Không thể tính căn bậc hai của số âm.")
    else:
        print(f"Căn bậc hai của {n} là: {math.sqrt(n):.2f}")
except ValueError:
    print("Lỗi: Đầu vào không phải là số.")