# Task 6 - Brute force for Problem 3 in O(m^3n^3)
def alg6(matrix,h,k):
    max_allowed_less_than_threshold = k
    i1,j1,i2,j2 = None, None, None, None
    maxSquareSize = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            # above for loop for selecting each element
            for k in range(rows):
                for l in range(cols):
                    # above for loops for selecting each corner of submatrix
                    squareSize = 0
                    # calculating number of elements less than threshold
                    if k-i == l-j and k-i>=0:
                        squareSize = k-i+1
                        less_than_threshold_count = 0
                        for x in range(i, i+squareSize):
                            for y in range(j, j+squareSize):
                                if matrix[x][y] < h:
                                    less_than_threshold_count += 1
                        # checking if number of elements less than threshold is a less max allowed elements
                        if less_than_threshold_count<=max_allowed_less_than_threshold:
                            if squareSize >= maxSquareSize:
                                maxSquareSize = squareSize
                                i1, j1 = i+1, j+1
                                i2, j2 = i+maxSquareSize, j+maxSquareSize
    return i1,j1,i2,j2
