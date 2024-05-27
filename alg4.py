# Task 4 - DP for Problem 2 in O(mn^2)
def alg4(matrix, h):
    m, n = len(matrix), len(matrix[0])

    # converting elements under threshold to 0 and rest as 1
    binaryMatrix = [[0] * (n) for _ in range(m)]
    for i in range(m):
        for j in range(n):
            binaryMatrix[i][j] = 0 if matrix[i][j]<h else 1
    
    # create prefix sum
    prefixSum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + binaryMatrix[i - 1][j - 1]

    i1,j1,i2,j2 = 0,0,0,0
    maxSquareSize = 0
    for i in range(m):
        for j in range(n):
            # above two for loops for selecting an element
            for k in range(1,min(m-i,n-j)+1):
                # above for loop for incrementing the diagonal element
                subSquareSum = prefixSum[i+k][j+k] - prefixSum[i][j+k] - prefixSum[i+k][j] + prefixSum[i][j]
                cornerSum = 0
                if k>1:
                    cornerSum = binaryMatrix[i][j] + binaryMatrix[i+k-1][j+k-1] + binaryMatrix[i][j+k-1] + binaryMatrix[i+k-1][j]
                else:
                    cornerSum = binaryMatrix[i][j]
                # inside sum is sum of subsquare minus the sum of corners, that should be greater than max no of 1s -4 1s belonging to corner
                insideSum = subSquareSum-cornerSum
                if insideSum>=(k*k-4):
                    if k>=maxSquareSize:
                        maxSquareSize = k
                        i1, j1 = i+1, j+1
                        i2, j2 = i1+k-1, j1+k-1
    return i1,j1,i2,j2
