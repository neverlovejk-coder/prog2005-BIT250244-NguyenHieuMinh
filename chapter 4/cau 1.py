def thong_ke_tuple(numbers):
    tong = sum(numbers)
    lon_nhat = max(numbers)
    nho_nhat = min(numbers)
    return tong, lon_nhat, nho_nhat

# Thử nghiệm
day_so = (10, 20, 5, 40, 15)
tong, max_val, min_val = thong_ke_tuple(day_so)
print(f"Tổng: {tong}, Lớn nhất: {max_val}, Nhỏ nhất: {min_val}")
