# Task 1 - Brute force for Problem 1 in O(m^3n^3)
def alg1(matrix,h):
    i1,j1,i2,j2 = None, None, None, None
    maxSquareSize = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            # above two for loops for selecting element in matrix
            for k in range(rows):
                for l in range(cols):
                    # above two for loops for selecting corners of submatrix
                    squareSize = 0
                    if k-i == l-j and k-i>=0:
                        squareSize = k-i+1
                        flag = True
                        for x in range(i, i+squareSize):
                            for y in range(j, j+squareSize):
                                # above two for loops for checking each element in submatrix
                                if matrix[x][y] < h:
                                    flag = False
                        if flag:
                            if squareSize >= maxSquareSize:
                                maxSquareSize = squareSize
                                i1, j1 = i+1, j+1
                                i2, j2 = i+maxSquareSize, j+maxSquareSize
    return i1,j1,i2,j2
