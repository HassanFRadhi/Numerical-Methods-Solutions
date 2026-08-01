import math
a = float(input('A: '))
e = 0
if a > 0:
    tol = 10**(-5)
    x = a/2
    y = (x + (a/x))/2
    e = math.fabs((y - x)/y)
    while e > tol:
        y = (x + (a/x))/2
        e = math.fabs((y - x)/y)
        x = y
    SquareRoot = x
else:
    SquareRoot = 0
print(SquareRoot)    