import math
n = 2
x = 0.5
es = 0.05
e = 1.5
ein = 1
etrue = 1.648721
E = (etrue - e) / etrue * 100
ea = (e - ein) / e * 100
while math.fabs(ea) >= es :
    ein = e
    e = e + (x**n / math.factorial(n))
    n += 1
    E = (etrue - e) / etrue * 100
    ea = (e - ein) / e * 100
print(e)