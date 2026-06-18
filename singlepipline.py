from functools import reduce
c=[20,30,40,55,26]
k=sorted(filter(lambda x:60<x<120,map(lambda x:int((x*9/5)+32),c)),key=lambda x:x%4)
print(k)

l=[5,8,9,2,3,4,6,12,15]
s=reduce(lambda x,y:x+y,(filter(lambda x:x%3==0,(map(lambda x:x*7,l)))))
print(s)


def apply_operation(a, b, op):
    return op(a, b)
print(apply_operation(10, 5, lambda x, y: x + y))
print(apply_operation(10, 5, lambda x, y: x - y))
print(apply_operation(10, 5, lambda x, y: x * y))

nums = list(range(1, 21))
a = filter(lambda x: x % 3 == 0, nums)
b = map(lambda x: x * x, a)
print(list(b))


