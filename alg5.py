# Task 5A - Top Down Recursion + Memoization for Problem 2 in O(mn)
def alg5a(matrix, h):
    def calculateTopLeft(matrix, top_left, row, col, h):
        # Check if original element is 0
        if matrix[row][col] < h:
            top_left[row][col] = 1
        # check if top-right or bottom-left are 0 in original matrix
        elif matrix[row][col-1] < h or matrix[row-1][col] < h:
            top_left[row][col] = 1
        else:
        # make recursive call
            if top_left[row][col-1] == -1:
                    calculateTopLeft(matrix, top_left, row, col-1, h)
            if top_left[row-1][col] == -1:
                    calculateTopLeft(matrix, top_left, row-1, col, h)
            if top_left[row-1][col-1] == -1:
                    calculateTopLeft(matrix, top_left, row-1, col-1, h)
            top_left[row][col] = min(top_left[row][col-1], top_left[row-1][col], top_left[row-1][col-1])+1

    def calculateTopRight(matrix, top_right, row, col, h):
            # Check if original element is 0
            if matrix[row][col] < h:
                top_right[row][col] = 1
            # check if top-left or bottom-left are 0 in original matrix
            elif matrix[row-1][col-1] < h or matrix[row][col-1] < h:
                top_right[row][col] = 1
            else:
            # make recursive call
                if top_right[row][col-1] == -1:
                        calculateTopRight(matrix, top_right, row, col-1, h)
                if top_right[row-1][col] == -1:
                        calculateTopRight(matrix, top_right, row-1, col, h)
                if top_right[row-1][col-1] == -1:
                        calculateTopRight(matrix, top_right, row-1, col-1, h)
                top_right[row][col] = min(top_right[row][col-1], top_right[row-1][col], top_right[row-1][col-1])+1

    def calculateBottomLeft(matrix, bottom_left, row, col, h):
            # Check if original element is 0
            if matrix[row][col] < h:
                bottom_left[row][col] = 1
            # check if top-left or top_right are 0 in original matrix
            elif matrix[row-1][col-1] < h or matrix[row-1][col] < h:
                bottom_left[row][col] = 1
            else:
            # make recursive call
                if bottom_left[row][col-1] == -1:
                        calculateBottomLeft(matrix, bottom_left, row, col-1, h)
                if bottom_left[row-1][col] == -1:
                        calculateBottomLeft(matrix, bottom_left, row-1, col, h)
                if bottom_left[row-1][col-1] == -1:
                        calculateBottomLeft(matrix, bottom_left, row-1, col-1, h)
                bottom_left[row][col] = min(bottom_left[row][col-1], bottom_left[row-1][col], bottom_left[row-1][col-1])+1
    i1, j2, i2, j2 = 0,0,0,0
    rows, cols = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
    dp = [[0]*cols for _ in range(rows)]
    top_right = [[-1]*cols for _ in range(rows)]
    top_left = [[-1]*cols for _ in range(rows)]
    bottom_left = [[-1]*cols for _ in range(rows)]

    # Iterate each element
    for i in range(rows):
        for j in range(cols):
            # initializing corner values
            if i==0 or j==0:
                dp[i][j] = 1
                top_left[i][j] = 1
                top_right[i][j] = 1
                bottom_left[i][j] = 1
            else:
                # else recursively calling DP values
                if top_left[i-1][j-1] == -1:
                    calculateTopLeft(matrix, top_left, i-1, j-1, h)
                if top_right[i-1][j] == -1:
                    calculateTopRight(matrix, top_right, i-1, j, h)
                if bottom_left[i][j-1] == -1:
                    calculateBottomLeft(matrix, bottom_left, i, j-1, h)
                dp[i][j] = min(top_left[i-1][j-1], top_right[i-1][j], bottom_left[i][j-1])+1
    
    maxSquareSize = 0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            # single pass in resultant matrix to get the solution
            if dp[i][j] >= maxSquareSize:
                maxSquareSize = dp[i][j]
                i2,j2 = i+1,j+1
                i1,j1 = i2-maxSquareSize+1, j2-maxSquareSize+1
    return i1,j1,i2,j2


# Task 5B - Bottom Up DP for Problem 2 in O(mn)
def alg5b(matrix, h):
    rows, cols = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0

    # Pad original matrix with 0's for simplicity
    for i in range(rows):
        matrix[i].insert(0,0)
    matrix.insert(0,[0 for i in range(cols+1)])

    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    top = [[0] * (cols + 1) for _ in range(rows + 1)]
    left = [[0] * (cols + 1) for _ in range(rows + 1)]
    top_left = [[0] * (cols + 1) for _ in range(rows + 1)]

    # Calculating dp ignoring top-right
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if i == 1 or j == 1:
                top[i][j] = 1
            else:
                # Check if original element is <h
                if matrix[i][j] < h:
                    top[i][j] = 1
                # check if top-left or bottom-left are <h in original matrix
                elif matrix[i-1][j-1] < h or matrix[i][j-1] < h:
                    top[i][j] = 1
                else:
                    top[i][j] = min(top[i][j-1], top[i-1][j], top[i-1][j-1])+1
    
    # Calculating dp ignoring bottom-left
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if i == 1 or j == 1:
                left[i][j] = 1
            else:
                # Check if original element is <h
                if matrix[i][j] < h:
                    left[i][j] = 1
                # check if top-left or top-right are <h in original matrix
                elif matrix[i-1][j-1] < h or matrix[i-1][j] < h:
                    left[i][j] = 1
                else:
                    left[i][j] = min(left[i][j-1], left[i-1][j], left[i-1][j-1])+1

    # Calculating dp ignoring top-left
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if i == 1 or j == 1:
                top_left[i][j] = 1
            else:
                # Check if original element is <h
                if matrix[i][j] < h:
                    top_left[i][j] = 1
                # check if top-right or bottom-left are <h in original matrix
                elif matrix[i][j-1] < h or matrix[i-1][j] < h:
                    top_left[i][j] = 1
                else:
                    top_left[i][j] = min(top_left[i][j-1], top_left[i-1][j], top_left[i-1][j-1])+1
    
    maxSquareSize = 0
    i1, j1, i2, j2 = None, None, None, None
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            # single pass in resultant matrix to get the solution
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = min(top_left[i-1][j-1], top[i-1][j], left[i][j-1])+1
            if dp[i][j] >= maxSquareSize:
                maxSquareSize = dp[i][j]
                i1,j1 = i-maxSquareSize + 1, j - maxSquareSize + 1
                i2,j2 = i,j
    return i1,j1,i2,j2
