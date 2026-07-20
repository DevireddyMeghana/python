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


#8
class Course:
    total_students = 0

    def __init__(self, student_name):
        self.student_name = student_name

    def enroll(self):
        Course.total_students += 1

    @classmethod
    def show_total(cls):
        print("Total Students:", cls.total_students)

    @staticmethod
    def is_eligible(age):
        return age >= 18

c1 = Course("Ram")
c2 = Course("Sita")

c1.enroll()
c2.enroll()

Course.show_total()

print(Course.is_eligible(20))

#9
class BankAccount:
    bank_name = "SBI"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount):
        return amount > 0

a = BankAccount("Ram", 5000)

a.deposit(2000)
print(a.balance)

BankAccount.change_bank_name("HDFC")
print(BankAccount.bank_name)




#2-1
class Student:
    total_students = 0
    pass_marks=35
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1
    def result(self):
        return "Pass" if self.marks > 35 else "Fail"
    @classmethod
    def curve_marks(cls,percent):
        cls.curve=percent
    @staticmethod
    def grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 50:
            return "C"
        elif marks >= 35:
            return "D"
        return "F"
s1=Student("Ram",30)
s2=Student("Sita",100)

Student.curve_marks(10)
s1.marks+=s1.marks*10/100
s2.marks+=s2.marks*10/100
for s in [s1, s2]:
    print("Name:",s.name)
    print("Marks:",s.marks)
    print("Result:",s.result())
    print("Grade:",Student.grade(s.marks))

#2-2
class Product:
    base_tax_rate = 10
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def final_price(self):
        return self.price + (self.price * int(Product.base_tax_rate / 100))
    @classmethod
    def change_price(cls,t):
        cls.base_tax_rate= int(t)
    @staticmethod
    def validate_price(price):
        return price > 0
p1=Product("Pen","20")
p2=Product("Book","300")
Product.base_tax_rate = 18
print(p1.final_price())
print(p2.final_price())
print(Product.validate_price(-10))

#2-3
class Employee:
    minimum_experience = 5

    def __init__(self, name, experience, department):
        self.name = name
        self.experience = experience
        self.department = department

    def eligibility(self):
        return self.experience >= Employee.minimum_experience

    @classmethod
    def update_experience(cls, new_experience):
        cls.minimum_experience = int(new_experience)

    @staticmethod
    def valid_department(dept):
        return dept in ["HR", "Tech", "Admin"]


e1 = Employee("Ravi", 4, "Tech")
e2 = Employee("Rose", 5, "HR")

Employee.update_experience(4)

print(e1.eligibility())
print(e2.eligibility())
print(Employee.valid_department("Sales"))

#2-4
class Loan:
    common_interest = 10
    def __init__(self, name, principal):
        self.name = name
        self.principal = principal
    def total_amount(self):
        return self.principal + (self.principal*(Loan.common_interest/100))
    @classmethod
    def update_interest(cls, interest):
        cls.common_interest = interest
    @staticmethod
    def eligibility(salary):
        return salary >=30000
l1=Loan("Raven", 100000)
l2=Loan("Ravi",50002)
Loan.update_interest(18)
print(l1.total_amount())
print(Loan.eligibility(400000))
print(l2.total_amount())
print(Loan.eligibility(20000))

#2-5
class Course:
    total=0
    min_duration=1
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.students = 0
        Course.total+=1
    def new_enroll(self):
        self.students+=1
    @classmethod
    def update_duration(cls, duration):
        cls.min_duration=duration
    @staticmethod
    def validate_duration(duration):
        return 0<duration<=365
c1=Course("Python",80)
c1.new_enroll()
Course.update_duration(10)
print(c1.students)
print(Course.validate_duration(200))

#2-7
class Inventory:
    total_items = 0
    threshold = 20

    def __init__(self):
        self.stock = {}

    def add(self, item, qty):
        if qty >= Inventory.threshold:
            self.stock[item] = qty
            Inventory.total_items += 1
            print("Item added successfully")
        else:
            print("Quantity should be at least 20")

    def remove(self, item):
        if item in self.stock:
            del self.stock[item]
            Inventory.total_items -= 1
            print("Item removed")
        else:
            print("Item not found")

    def display(self):
        print("Inventory:")
        for item in self.stock:
            print(item, ":", self.stock[item])
i1 = Inventory()
item = input("Enter item name: ")
qty = int(input("Enter quantity: "))
i1.add(item, qty)
item = input("Enter item to remove: ")
i1.remove(item)
i1.display()
print("Total Items:", Inventory.total_items)


#2-10
class Member:
    BMI_limit = 25

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def calculate(self):
        bmi = self.weight / ((self.height / 100) ** 2)
        print("BMI =", round(bmi, 2))

        if bmi > Member.BMI_limit:
            print("Unfit")
        elif bmi >= Member.BMI_limit - 6:
            print("Fit")
        else:
            print("Underweight")

    @classmethod
    def update_limit(cls, limit):
        cls.BMI_limit = limit
        print("New BMI Limit:", cls.BMI_limit)

    @staticmethod
    def eligible(age):
        return age >= 18


# Driver Code
name = input("Enter name: ")
height = float(input("Enter height (cm): "))
weight = float(input("Enter weight (kg): "))

m1 = Member(name, height, weight)

m1.calculate()

age = int(input("Enter age: "))
if Member.eligible(age):
    print("Eligible")
else:
    print("Not Eligible")

new_limit = int(input("Enter new BMI limit: "))
Member.update_limit(new_limit)

m1.calculate()