import salaryPackage
salaryPackage.salary(20000)

import salaryPackage as sp
sp.salary(50000)
print(sp.salaries)

from salaryPackage import salary
salary(4000)

#Exceptions
a = 10
b = 0
c = "2"

try:
    print(a/b)
except ZeroDivisionError:
    print("ZeroDivisionError")

try:
    print(a/c)
except TypeError:
    print("TypeError")
