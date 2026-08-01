import math
def summ(x,n): 
    y = 0
    for i in range (0,n):
        y = y + (x**i / math.factorial(i))
    return y
E1 = (math.exp(-10) - summ(-10,100)) / (math.exp(-10)) * 100
print(E1)
#print(sum(-10,100))