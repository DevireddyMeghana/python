m=lambda a,b:a+b
print(m(1,2))

l=lambda k:k**k
a=l(2)
print(a)

m=lambda x,y,z:(x+y)*z
print(m(10,2,3))

s=lambda x:print(x*5)
print(s(20))

def s(x):
    print(x*5)
    return
print(s(10))

x=10
y=20
print(x if x>y else y)

d=lambda a,b:a if a<b else b
print(d(10,20))

s=lambda x:x not in 'AEIOUaeiou'
k=input()
for i in k:
    if s(i):
        print(i)

def fun(x):
    if x not in "AEIOUaeiou":
        return x
    return ""
l=["Hello","Hii","Who','are","You?"]
k=[]
for i in l:
    s=list(map(fun,i))
    s="".join(s)
    k.append(s)
print(k)