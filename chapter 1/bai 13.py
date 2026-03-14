try:
    num1 = int(input("Nhập số bị chia: "))
    num2 = int(input("Nhập số chia: "))
    result = num1 / num2
    print(f"Kết quả: {result}")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0.")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")