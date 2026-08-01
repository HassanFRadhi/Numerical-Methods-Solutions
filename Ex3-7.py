import numpy as np
def sum(n):
    summ = 0
    for i in range (0,100000):
        summ += n
    return np.float32(summ)


print(sum(0.00001))
