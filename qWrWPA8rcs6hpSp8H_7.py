
def determinant(matrix):
    det = 0
    if len(matrix) == 1:
        det += matrix[0][0]
    else:
        for i in range(0, len(matrix)):
            det += ((-1) ** (i))*matrix[i][0] * determinant([matrix[j][1:] for j in range(0, len(matrix)) if j != i])
    return det

