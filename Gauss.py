n = 3
A = [
    [2,3,4],
    [10,18,20],
    [6,8,9]
]
for k in range(0,n-1):
    for i in range(1,n):
        factor = A[i][k] / A[k][k]
        for j in range(0,n):
            A[i][j] = A[i][j] - factor * A[i-1][j] 
print(A)