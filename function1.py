#defining functions
def say_hello():
    print("Welcome to Python")
say_hello()

def add(a,b):
    print(a+b)
    return a+b
add(10,20)

def add(a,b):
    print(a+b)
add(40,60)

def area_of_rectangle(length,width):
    return length*width
area_of_rectangle(6,4)

#parameters
def multiply(a,b,c):
    return a*b*c
multiply(10,20,30)

def describe_pet(animal, name):
    print(f"My {animal} is named {name}")
describe_pet("Dog", "chinni")



