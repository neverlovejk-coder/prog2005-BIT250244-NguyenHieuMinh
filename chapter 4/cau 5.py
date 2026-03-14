class Product:
    def __init__(self, price):
        self.price = price # Gọi setter để kiểm tra giá ngay khi khởi tạo

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Lỗi: Giá phải lớn hơn 0!")
            self._price = 1 # Gán giá trị mặc định nếu sai

    def __str__(self):
        return f"Product Price: {self._price}"

# Thử nghiệm
sp1 = Product(150)
print(sp1)

sp2 = Product(-50) # Sẽ báo lỗi và gán giá trị mặc định
print(sp2)