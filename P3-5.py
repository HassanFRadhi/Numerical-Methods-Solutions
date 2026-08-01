import numpy as np
true_value = np.float32((np.pi)**4 / 90)
sum = 0
sumr = 0
for i in range(1,10001,1):
    sum = np.float32(sum + (1/i**4))
for i in range (10000,0,-1):
    sumr = np.float32(sumr + (1/i**4))
Error1 = (true_value - sum) / true_value * 100
Error2 = (true_value - sumr) / true_value * 100
print(Error1)
print(Error2)

