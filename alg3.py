# Task 3 - DP for Problem 1 in O(mn)
def alg3(matrix, h):
    rows, cols = len(matrix), len(matrix[0])

    # Initialize dp array with 0
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    # To store maximum square size
    maxSquareSize = 0

    # To store bounding indices of the max square
    i1,j1,i2,j2 = None, None, None, None

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] >= h:
                # bellman equation: value of current element = minimum value of top, left, diagonal element + 1
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                if dp[i][j] >= maxSquareSize:
                    # keeping track of max size in same loop
                    maxSquareSize = dp[i][j]
                    i1,j1 = i-maxSquareSize + 1, j - maxSquareSize + 1
                    i2,j2 = i,j
    return  i1, j1, i2, j2
