class Person:
    count = 0
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Person.count += 1
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def set_name(self, name):
        if not isinstance(name, str) or name == "":
            raise ValueError("Tên không hợp lệ!")
        self._name = name
    def set_age(self, age):
        if age < 0:
            raise ValueError("Tuổi phải >= 0!")
        self._age = age
    def __str__(self):
        return f"Person(Name: {self._name}, Age: {self._age})"
    def introduce(self):
        return f"Xin chào, tôi là {self._name}"
    @classmethod
    def get_count(cls):
        return cls.count
    @staticmethod
    def validate_age(age):
        if age < 0:
            raise ValueError("Tuổi không hợp lệ!")
        return True
    def __eq__(self, other):
        return self._name == other._name and self._age == other._age
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.set_grade(grade)
    def get_grade(self):
        return self._grade
    def set_grade(self, grade):
        # dùng static method để validate (cách 2)
        Person.validate_age(grade)  # giả sử điểm >= 0
        self._grade = grade
    def __str__(self):
        return f"Student(Name: {self._name}, Age: {self._age}, Grade: {self._grade})"
    def study(self):
        return f"{self._name} đang học bài"
try:
    n1 = Person("An", 20)
    n2 = Person("An", 20)
    s1 = Student("Binh", 18, 9)
    print(n1)
    print(s1)
    print(n1.introduce())
    print(s1.study())
    print("so luong nguoi:", Person.get_count())
    print("so sanh n1 va n2:", n1 == n2)
except ValueError as e:
    print("Lỗi:", e)