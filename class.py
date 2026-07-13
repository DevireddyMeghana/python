class A:
    def m1(self, name):
        self.name = name
        print(f"Hola {name}")

    @classmethod
    def m2(cls, s):
        cls.something = s
        print(cls.something)

    @staticmethod
    def greet(name):
        print(f"Byee {name}")


a1 = A()
A.greet("Hello")
a1.greet("Byee")
a1.m2("Just")


#1
class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
            return self.marks >40
student1 = Student("Jhon", 20)
student2 = Student("Billa", 200)
for student in [student1, student2]:
    if student.is_passed():
        print(f"Student {student.name} is passed")
    else:
        print(f"Student {student.name} is not passed")

#2
class Employee:
    company_name="TechCrop"
    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
e1 = Employee("Jhon")
e2 = Employee("Billa")
print(e1.company_name)
print(e2.company_name)
print("Change Company After:")
Employee.change_company("Infosys")
print(e1.company_name)
print(e2.company_name)

#3
class MathOps:
    @staticmethod
    def is_even(num):
        return num % 2 == 0
m= MathOps()
print(m.is_even(3))

#4
class Car:
    wheels=4
    def __init__(self, mileage):
        self.mileage = mileage
    def display_specs(self):
        print(self.mileage)
        print(Car.wheels)
    @classmethod
    def display_wheels(cls,num):
        Car.wheels = num
c=Car(40)
c.display_specs()
Car.display_wheels(4)
c.display_specs()


#5
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    @staticmethod
    def fahrenheit(celsius):
        return celsius * 1.8 + 32
    def show_conversion(self):
        print("CELSIUS:",self.celsius)
        print("FAHRENHEIT:",Temperature.fahrenheit(self.celsius))
m=Temperature(32)
m.show_conversion()