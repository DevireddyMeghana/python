l=[1,2,[3,4]]
import copy
k=copy.deepcopy(l)
from copy import deepcopy
k=deepcopy(l)
k[2].append(37)
print(k)
print(l)
