def fun(x:int,y:int)->int:
    print(x+y)
    return x+y
fun(10,20)

def fun(x:int,y:int)->int:
    print(x+y)
print(fun("Hello","hii"))
print(fun.__annotations__)

def greet(name:str,age:int)->str:
    """ Just a greeting """
    print(f"Hello, {name}")
    print(f"age:{age}")
print(greet.__name__)
print(greet.__doc__)
print(greet.__class__.__name__)
print(greet.__class__.__doc__)
print(greet.__closure__)