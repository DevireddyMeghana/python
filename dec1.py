from plotly.figure_factory.utils import validate_positive_scalars


def login(func):
    def inner():
        un=input("Enter the Username:")
        psd=input("Enter the Password:")
        if un=="silent_soul" and psd=="Maggi":
           return func()
        else:
            return "Invalid Credentials"
    return inner
@login
def securefile():
    return "Secret File"
print(securefile())

def my_decorator(func):
    def wrapper():
        print("Function is starting")
        func()
        print("Function is done")
    return wrapper
@my_decorator
def greet():
    print("Hello!")
greet()


def Upper(x):
    for i in x:
        if i.isupper():
            return True
    return False

def vaild(func):
    uns = []
    special_char = ['@',"!","#","$","%","^","&","*"]
    def inner(us:str,psd:str,age:int):
        nonlocal uns
        if us not in uns:
            if 8 <= len(psd) <= 15:
                k = list(filter(lambda x: x in special_char, psd))
                n = list(filter(lambda x: x.isdigit, psd))
                up = Upper(psd)
                print(k)
                print(n)
                print(up)

                if up and n and k:
                    uns.append(us)
                    if age >= 18:
                        return func(us,psd,age)
                    else:
                        return "Age must be greater than 17"
                else:
                    return "Invalid Password"
            else:
                return "Minimum length of the password is 8 characters"
        else:
            return "Username already exists"
    return inner


@vaild
def register(username,password,age):
    return f"{username}'s Register Successful"

print(register("praveen","Dhaya143$$",19))
print(register("praveen","Dhaya143$$",19))

import functools

def ann(func):
    @functools.wraps(func)
    def inner(x,y):
        # print(func.__name__)
        # print(func.__annotations__)
        # print(func.__doc__)
        print(x,y)
        return func(x,y)
    return inner


@ann
def fun(a:int,b:int) -> int:
    """Just adding a Doc for the function"""
    return a+b

print(fun(10,24))
print(fun.__name__)
print(fun.__annotations__)
print(fun.__doc__)

import time
# Timing decorator
def timer2(delay):
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # start = time.asctime()
            start = time.time()
            print("Started: ", start)
            time.sleep(delay)
            print(f"Sum : {func(*args, **kwargs)}")
            # end = time.asctime().split()
            end = time.time()
            print(f"End : {end}")
            print("Time taken: ",end-start)
        return wrapper
    return timer

@timer2(5)
def add(x,y):
    """ This is a Doc String"""
    su = 0
    for i in range(1, x + y + 1):
        su += i
    return su

add(100000,200000)
print(add.__doc__)
print(time.asctime())
print(list(time.asctime().split()))


def tim(delay=3):
    def dec(fn):
        @functools.wraps(fn)
        def indec(*args, **kwargs):
            print(f"Just adding {delay}sec Delay to start the function")
            print(f"Address inside Decorator : {fn}")
            time.sleep(delay)
            result = fn(*args,**kwargs)
            print("Execution Completed")
            return result
        print(f"Address fn: {fn}")
        print(f"Address indec : {indec}")
        return indec
    return dec

k = int(input("Enter Delay : "))
@tim(k)
def add(a,b,c):
    """ Just adding A DOC"""
    return a+b+c
print(f"Address add : {add}")
print(add(10,15,25))
print(add.__doc__)
del k

def validate_positive(func):
    @functools.wraps(func)
    def inner(*args):
        for i in args:
            if i < 0:
                print("Error Message")
                return None
        return func(*args)
    return inner

@validate_positive
def mul(a,b):
    return a*b
mul(10,20)
print(mul)