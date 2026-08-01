import math
import numpy as np
x1 = 0
c1 = 0
xu = 1.3
ea = 100
c2 = 0
test = 0
fx1 = 0
while ea > 0.05:
    fx1 = x1**10 - 1
    c1 = (x1 + xu) / 2
    ea = np.abs(c1 - c2) / c1 * 100
    y = c1**10 - 1
    test = fx1 * y
    if test > 0:
        x1 = c1
    elif test < 0:
        xu = c1
    else:
        break
    c2 = c1
print(c1)
print(ea)

     