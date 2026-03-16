#11
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Tieng dong vat")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Gau gau")
dog = Dog("Milu")
print("Ten:", dog.name)
dog.sound()