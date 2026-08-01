from sympy import isprime
sum = 0
for i in range(0,2000001):
    if isprime(i):
        sum += i
print(sum)