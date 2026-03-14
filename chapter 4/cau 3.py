def kiem_tra_key(d, key):
    if key in d:
        return f"Key '{key}' có tồn tại."
    else:
        return f"Key '{key}' không tồn tại."

# Thử nghiệm
data = {"brand": "Apple", "model": "iPhone 15"}
print(kiem_tra_key(data, "brand"))
print(kiem_tra_key(data, "year"))