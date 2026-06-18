l=[1,2,3]
k=l.copy()
k.append(25)
print(l)
print(k)

import copy
original=[[1,2,3,],[4,5,6]]
shallow=copy.copy(original)
shallow[0][0]=99
print(original)