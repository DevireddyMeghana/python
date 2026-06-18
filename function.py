def work(w):
    print("gone out")
    print(f"brought sweet with {w}")
    print("come back")
work(50)
work(100)

def fun2():
    print("Hello")
fun2()

def fun3(x):
    print(x*x)
fun3(3)

def fun4(x,y,z):
    print(x+y+z)
fun4(10,20,30)

def details(name,age,branch):
    print(f"name:{name}")
    print(f"age:{age}")
    print(f"branch:{branch}")
details("Meghana",21,"CSE(AI&ML)")
details(age=21,branch="CSE(AI&ML)",name="Meghana")

def fun5(x,y):
    print(x,y)
    print(x*y)
fun5(10,20)

x=300
def fun6():
    x=200
print(x)
fun6()
print(x)

def fun7(x,y=30):
    print(x,y)
fun7(10,20)
fun7(70)

def fun9(y,x=70):
    print(x,y)
fun9(80,80)
fun9(80)

def fun10(b,c=60,a=20):
    if(b>c):
        print(b+c)
    else:
        print(c+a)
fun10(60)
fun10(50,70)

def fun11(a,b):
    a=sum(a)
    b=sum(b)
    print(f"list1:{a}")
    print(f"list2:{b}")
    print(f"total:{a+b}")
fun11([1,2,3,4,5],[6,7,8,9,10])


