def polyreg(x,y,m):
    for i in range(0,m+1):
        for j in range(0,i):
            k = i + j - 2
            sum = 0
            for l in range(0,n):
                sum += x[l]