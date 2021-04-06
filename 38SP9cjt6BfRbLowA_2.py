
def trace(M):
    return sum([M[i][i] for i in range(min(len(M), len(M[0])))])
​
def matrixmult(A, B):
    C = [[0 for row in range(len(A))] for col in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C
​
def double_dot(d1, d2):
    d2t = [list(i) for i in zip(*d2)]    # transpose
    return trace(matrixmult(d1, d2t))

