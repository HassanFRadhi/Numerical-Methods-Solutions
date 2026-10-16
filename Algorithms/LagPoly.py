def lagpoly(x,y,xx):
    n = len(x)
    sum = 0
    for i in range(0,n):
        product = y[i]
        for j in range(0,n):
            if j != i:
                product = product * (xx - x[j])/(x[i]-x[j])
        sum = sum + product
    return sum

t = [1,3,5,7,13]
v = [800,2310,3090,3940,4755]
print(lagpoly(t,v,10))