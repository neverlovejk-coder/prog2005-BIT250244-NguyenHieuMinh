#7
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, s):
        name, age = s.split("-")
        return cls(name, int(age))


# Tạo đối tượng từ chuỗi
p = Person.from_string("Nam-20")

print("Name:", p.name)
print("Age:", p.age)