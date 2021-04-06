
#########################################################################
# A * B
def matrixmult (A, B):
    C = [[0 for row in range(len(A))] for col in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C
​
def multiply_matrix(m1, m2):
    return "ERROR" if len(m2) != len(m1[0]) else matrixmult(m1, m2)

