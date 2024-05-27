# Task 2 - Brute force for Problem 1 in O(m^2n^2)
def alg2(matrix, h):
    rows, cols = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
    maxSquareSize = 0
    i1, j1, i2, j2 = None, None, None, None
    for i in range(rows):
        for j in range(cols):
            # above two for loops for selecting element in matrix
            if matrix[i][j] >= h:
                squareSize = 1
                flag = True
                while squareSize + i < rows and squareSize + j < cols and flag:
                    # above while loop for incrementing diagonal element
                    for k in range(j, squareSize + j + 1):
                        # above for loop for checking every element in a column including diagonal element
                        if matrix[i + squareSize][k] < h:
                            flag = False
                    for k in range(i, squareSize + i + 1):
                        # above for loop for checking every element in a row including diagonal element
                        if matrix[k][j + squareSize] < h:
                            flag = False
                    if flag:
                        squareSize += 1
                if squareSize >= maxSquareSize:
                    maxSquareSize = squareSize
                    i1, j1 = i+1, j+1
                    i2, j2 = i+maxSquareSize, j+maxSquareSize
    return i1, j1, i2, j2