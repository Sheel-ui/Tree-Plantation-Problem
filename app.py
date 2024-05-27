import sys
import alg1,alg2,alg3,alg4,alg5,alg6,alg7

if __name__ == "__main__":

    m_n_h_k = input()
    args = m_n_h_k.split(' ')
    m,n,h,k = int(args[0]), int(args[1]), int(args[2]), 0
    if len(args)>3:
        k = int(args[3])

    matrix = []
    for i in range(m):
        row = input()
        matrix.append([int(value) for value in row.split(' ')])


    # Invoking Strategies

    if sys.argv[1] == "alg1":
        output = alg1.alg1(matrix,h)
    elif sys.argv[1] == "alg2":
        output = alg2.alg2(matrix, h)
    elif sys.argv[1] == "alg3":
        output = alg3.alg3(matrix, h)
    elif sys.argv[1] == "alg4":
        output = alg4.alg4(matrix, h)
    elif sys.argv[1] == "alg5a":
        output = alg5.alg5a(matrix, h)
    elif sys.argv[1] == "alg5b":
        output = alg5.alg5b(matrix, h)
    elif sys.argv[1] == "alg6":
        output = alg6.alg6(matrix,h,k)
    elif sys.argv[1] == "alg7a":
        output = alg7.alg7a(matrix,h,k)
    elif sys.argv[1] == "alg7b":
        output = alg7.alg7b(matrix,h,k)


    print(" ".join(str(idx) for idx in output))