
sub_matrix = lambda A, i, j: [[A[r][c] for c in range(len(A)) if c != j] for r in range(len(A)) if r != i]
def determinant(A):
    if len(A) == 1: return A[0][0]
    det, sign = 0, 1
    for c in range(len(A)):
        det += A[0][c] * determinant(sub_matrix(A, 0, c)) * sign
        sign = -sign
    return det

