import numpy as np
x = [[3,1],[8,6],[0,4]]
y = [[5,9],[7,2]]
z = [[0,0],[0,0],[0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            z[i][j] += x[i][k] * y[k][j]
print(z)