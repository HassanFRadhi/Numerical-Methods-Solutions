import math
true_value = 6.737947e-3
x = 5
sum1 = 0
sum2initial = 0
for i in range(0,20):
    sum1 += (x**i / math.factorial(i)) * (-1)**(i)
    sum2initial += (x**i / math.factorial(i))
sum2  = 1/sum2initial
Te1 = (true_value - sum1)/ true_value 
Te2 = (true_value - sum2) / true_value
print(Te1)
print(Te2)
