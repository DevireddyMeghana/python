def fun(*a):
    print(a)
fun(1,2,3,4,5,6,7,8,9,10)

def fun2(**b):
    print(b)
fun2(a=75,b=30,c=67,d=69,e=75)

def fun3(*c):
    print(c)
fun3(1,7,5,3,2)

def fun5(a,b):
    print(a,b)
def fun4(**d):
    print(d)
    fun5(**d)
fun4(a=70,b=75)

def fun6(*e,**f):
    print(e,f,sep="/n")
    print(type(e),type(f),sep="/n")
fun6(1,2,4,5,7,6,a=75,b=75,c=89,d=45)

def fun7(*a):
    for i in a:
        if(i % 2 == 0):
            print(i)
fun7(1,2,3,4,5,6,7,8,9,10)

def fun9(*a):
    print(sum(a))
fun9(7,8,6,5,2,3,9)

def fun10(a,b):
    print(a+b)
    return a+b
print(fun10(10,15))

def fun11(a,b):
    print(a+b)
print(fun11(10,15))

def fun12(a,b):
    return a+b
def fun13(x,y):
    return x+y
fun13(fun12(7,8),fun12(9,15))


