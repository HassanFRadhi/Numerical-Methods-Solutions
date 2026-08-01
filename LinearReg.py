import matplotlib.pyplot as plt
def linreg(x,y):
    n = len(x)
    sumx,sumy, sumxy, sumx2, Sr, St = 0,0,0,0,0,0
    for i in range(0,n):
        sumx += x[i]
        sumy += y[i]
        sumxy += x[i] * y[i]
        sumx2 += x[i]**2
    Xmean = sumx / n
    Ymean = sumy / n
    a1 = (n * sumxy - sumx * sumy)/(n * sumx2 - sumx**2)
    a0 = Ymean - a1*Xmean
    for i in range(0,n):
        St += (y[i] - Ymean)**2
        Sr += (y[i] - a1*x[i] - a0)**2
    
    syx = (Sr/(n-2))**0.5
    r2 = (St - Sr)/St
    print(f" y = {a0} + {a1}x\n")
    print(f"R^2 = {r2}")
    return a0,a1,r2
a0,a1,r = linreg(x,y)
for i in range(0, len(x)):
    y[i] = a0 + a1 * x[i]
plt.plot(x,y)
plt.show()