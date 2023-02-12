#Vectorel Operations

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i]*b[i])
print(ab)

#FP

import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

print(a*b)

#Map, filter and reduce
liste = [1, 2, 3, 4, 5]
for i in liste:
    print(i+ 10)

list(map(lambda x: x*10, liste))

#filter

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
list(filter(lambda x: x%2 == 0, liste))

#reduce

from functools import reduce

liste = [1, 2, 3, 4]
reduce(lambda a,b: a+b, liste)
