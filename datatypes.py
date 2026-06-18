#string
name = "Python"
print(name[0]) # P — indexing
print(name[1:4]) # yth — slicing
print(name.upper()) # PYTHON

#list
fruits = ['apple', 'banana', 'cherry', 'date']
fruits[1] = 'blueberry' # Modify in place
print(len(fruits))   #4

#tuple
point = (10, 20)
x, y = point # Tuple unpacking
print(x) # 10

#set
nums = {1, 2, 3, 2, 1}
print(nums) # {1, 2, 3} — duplicates removed
nums.add(4)
print(3 in nums) # True — fast membership check

#frozenset
fs = frozenset({1, 2, 3})
# fs.add(4) ← This would raise AttributeError
print(fs)

#dict
student = {'name': 'Alice', 'age': 21, 'grade': 'A'}
print(student['name']) # Alice
student['age'] = 22 # Update value
student['city'] = 'Hyderabad' # Add new key

#bytes
ba=bytearray(b'hello')
ba[0]=72
print(ba)

#bytearray
ba=bytearray(b'hello')
ba[0]=72
print(ba)

#memoryview
data=bytearray(b'python')
mv=memoryview(data)
print(mv[0])
mv[0]=112
print(mv[0])


