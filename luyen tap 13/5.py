class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __str__(self):
        return f"flower name: {self.name}, Color: {self.color}"
a1 = Flower("hoa cuc", "do")
print(a1)