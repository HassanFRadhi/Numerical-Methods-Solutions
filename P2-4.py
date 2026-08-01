import math
def fourier_cos(x,n):

    cosx = 0
    j = 0
    for i in range(0,n+1,2):
        cosx = (x**i / math.factorial(i)) * (-1)**j + cosx
        j += 1
        
    error = (math.cos(x) - cosx) / (math.cos(x)) * 100 
    print(cosx)

fourier_cos(1.25,6)