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

def fun2(y):
    s=0
    for i in y:
        s+=ord(i)
    return s
a=list(map(fun2,k))
print(a)

#sum of two lists
def fun3(x):
    return x
l=[1,2,3,4]
b=[10,20,30,40]
s=list(map(lambda l,b:l+b,l,b))
print(s)

#divisible by 3 or 5
nums=[12,15,7,18,20,21,25]
k=list(filter(lambda x:(x%3==0 or x%5==0) and not(x%3==0 and x%5==0),nums))
print(k)
def fun5(x):
    return x
l=[1,2,3,4,5,6]
s=list(map(fun5,l))
print(s)

l=[[1,2,[3,4],[5,6]]]
print(k.append(20))
print(k+[20])

# Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use filter() to keep only the keys whose values are greater than 50.
d = {"apple": 100, "banana": 40, "cherry": 150}
k=list(filter(lambda x: d[x]>=50, d))
print(k)

#Use functools.reduce() with a lambda to find the largest number from a given list Dynamically.
from functools import reduce
li=[1,2,4,9,8]
k=reduce(lambda x,y:x if x>y else y,li)
print(k)

#5. Use map() on a string to convert each character into its ASCII value (using ord()). Print the result list.
k=input()
s=list(map(ord,k))
print(s)

#Use map() with a lambda to add 5 to every element of the following nested list [[1, 2], [3, 4], [5, 6]]
x=[[1,2],[3,4],[5,6]]
k=list(map(lambda x:x[0]+5,x))
print(k)

#Use reduce() to concatenate a list of characters into a single string.Example input: ['P', 'y', 't', 'h', 'o', 'n'].
x= ['P', 'y', 't', 'h', 'o', 'n']
k=reduce(lambda x,y:x+y,x)
print(k)

## Given a list of integers, use map() with id() to print the memory address of each element.Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.
x= [10, 350, 10, 350, 20]
k=map(id,x)
print(list(k))

'''10. Given a list of numbers:
[5, 10, 15, 20, 25, 30]
Perform the following in a single pipeline:
• Use map() to square each number
• Use filter() to keep only numbers divisible by 5
• Use reduce() to calculate the sum of remaining numbers'''
l=[5,10,15,20,25,30]
k=list(map(lambda x:x**2,l))
print(k)
s=list(filter(lambda x:x%5==0,l))
print(s)
j=reduce(lambda x,y:x+y,l)
print(j)

'''4. Given a list:
nums = [1, 2, 3, 4] 
Use reduce() with a lambda to compute the sum, but start with an initial value 
of 10.
Explain how the initial value affects the reduction process.'''

nums = [1, 2, 3, 4]
k=reduce(lambda x,y:x+y,nums,10)
print(k)

#cube
l=[1,2,3,4,5]
k=map(lambda x:x**3,l)
print(list(k))

#isalpha
s="abc@k,@/"
k=list(filter(lambda x: not x.isalpha(),s))
print(k)

#sum of the list using initial values
nums=[1,3,48,9,10,12]
k=reduce(lambda x,y:x+[y],nums,[10])
print(k)

#removing Capitals
s=input()
k=list(filter(lambda x:not x.isupper(),s))
print(k)