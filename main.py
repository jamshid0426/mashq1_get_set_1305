# 1
class Student:
    def __init__(self, fullname, grade):
        self.fullname = fullname
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        self.__grade = new_grade


s1 = Student("Ali Valiyev", 4)

print(s1.fullname)

grade = s1.get_grade()
print(grade)

s1.set_grade(5)
print(s1.get_grade())

# 2
class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.name, self.price

    def set_price(self, new_price):
        self.price = new_price


c1 = Car("BMW", 45000)
print(c1.get_price())

c1.set_price(50000)
print(c1.set_price)

# 4
class Teacher:
    def __init__(self, fullname, salary):
        self.fullname = fullname
        self.__salary = salary

    def get_salary(self):
        return self.__salary, self.fullname

    def set_salary(self, new_salary):
        self.__salary = new_salary


t1 = Teacher("Karimov Aziz", 500)

t1.set_salary(700)
print(t1.get_salary())

# 5
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.__ram = ram

    def get_ram(self):
        return self.__ram, self.brand

    def set_ram(self, new_ram):
        self.__ram = new_ram


l1 = Laptop("HP", 8)

l1.set_ram(16)
print(l1.get_ram())

# 6
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password, self.username

    def set_password(self, new_password):
        self.__password = new_password


u1 = User("admin", 12345)

u1.set_password(54321)
print(u1.get_password())
