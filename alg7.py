def transformList(i,j,k_list):
    # transforming the perspective of 0s according to index of current element
    return [(k[0]-i,k[1]-j) for k in k_list if (k[0] -i >=0 and k[1]-j>=0)]


def prefixSum(i,j,matrix,prefixSumDP):
    # recursive code to generate prefix sum matrix
    if i == 0 or j == 0:
        prefixSumDP[i][j]=0
        return 0
    elif prefixSumDP[i][j] != -1:
        return prefixSumDP[i][j]
    else:
        prefixSumDP[i][j] = prefixSum(i - 1,j,matrix,prefixSumDP) + prefixSum(i,j-1,matrix,prefixSumDP) - prefixSum(i-1,j-1,matrix,prefixSumDP) + matrix[i - 1][j - 1]
        return prefixSumDP[i][j]


# Task 7A - Top Down Recursion + Memoization for Problem 3 in O(mnk)
def alg7a(matrix,h,k):
    matrix = [[0 if i<h else 1 for i in j] for j in matrix]
    m = len(matrix)
    n = len(matrix[0])
    k_list = []
    dp = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                k_list.append((i,j))

    prefixSumDP = [[-1]*(n+1) for i in range(m+1)]
    for i in range(m):
        for j in range(n):
            # above two for loops to select an element in matrix
            flag = False
            max_size = 0
            max_zeros = m*n+1
            for z in transformList(i,j,k_list):  
                # above for loop for selecting k zeros that are allowd
                size = max(z[0],z[1]) + 1
                if i+size <= m and j+size <= n:
                    # for every element checking the subsquare sum is 0s less than allowed k
                    # making RECURSIVE calls to generate prefix sum DP
                    subSquareSum = prefixSum(i+size,j+size,matrix,prefixSumDP) - prefixSum(i,j+size,matrix,prefixSumDP)  - prefixSum(i+size,j,matrix,prefixSumDP) + prefixSum(i,j,matrix,prefixSumDP)
                    zeros = size*size-subSquareSum
                    if zeros>k and zeros<max_zeros:
                        flag=True
                        max_size = size
                        max_zeros = zeros
            if not flag:
                dp[i][j]=min(m-i,n-j)
            else:
                dp[i][j]=max_size-1
    x,y,size=0,0,0
    for i in range(m):
        for j in range(n):
            # single pass to get the max solution
            if dp[i][j]>=size:
                x,y=i+1,j+1
                size = dp[i][j]
    if x+size-1 >= x or y+size-1 >= y:
        return x,y, x+size-1, y+size-1
    else:
        return None, None, None, None


# Task 7B - Bottom Up DP for Problem 3 in O(mnk)
def alg7b(matrix,h,k):
    matrix = [[0 if i<h else 1 for i in j] for j in matrix]
    m = len(matrix)
    n = len(matrix[0])
    k_list = []
    dp = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                k_list.append((i,j))
    prefixSum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # populating the values of prefixsum FP
            prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + matrix[i - 1][j - 1]
    for i in range(m):
        for j in range(n):
            # above two for loops to select an element in matrix
            flag = False
            max_size = 0
            max_zeros = m*n+1
            for z in transformList(i,j,k_list): 
                # above for loop for selecting k zeros that are allowd 
                size = max(z[0],z[1]) + 1
                if i+size <= m and j+size <= n:
                    # for every element checking the subsquare sum is 0s less than allowed k
                    # using precomputed DP matrix to get the sub square sum
                    subSquareSum = prefixSum[i+size][j+size] - prefixSum[i][j+size] - prefixSum[i+size][j] + prefixSum[i][j]
                    zeros = size*size-subSquareSum
                    if zeros>k and zeros<max_zeros:
                        flag=True
                        max_size = size
                        max_zeros = zeros
            if not flag:
                dp[i][j]=min(m-i,n-j)
            else:
                dp[i][j]=max_size-1
    x,y,size=0,0,0
    for i in range(m):
        for j in range(n):
            # single pass to get the max solution
            if dp[i][j]>=size:
                x,y=i+1,j+1
                size = dp[i][j]

    if x+size-1 >= x or y+size-1 >= y:
        return x,y, x+size-1, y+size-1
    else:
        return None, None, None, None