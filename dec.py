def dec(func):
    def inner(n):
        print("Starting this Function")
        print(func.__name__)
        print(n)
        print("ending this function")
    return inner
@dec
def greet(name):
    print(f"Hello {name}")
print(greet.__name__)
greet("Maggi")


