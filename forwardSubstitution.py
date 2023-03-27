A = [[1,0,0,0],
     [2,3,0,0],
     [4,5,6,0],
     [7,8,9,10]]

b = [1,5,15,34]

x = [0,0,0,0]

def forwardSub(A,b,n):
    x[0] = b[0]/A[0][0]
    for i in range(1, n+1):
        sum = b[i]
        for j in range(0,i):
            sum = sum - A[i][j]*x[j]
        x[i] = sum/A[i][i]

forwardSub(A,b,3)

print('The solution is: ',x)