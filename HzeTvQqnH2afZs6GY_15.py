
def generate_rug(n, direction):
    matrix = [[i for i in range(0,n)] for j in range(0,n)]
    for i in range(0,n):
        for j in range(0,n):
            matrix[i][j] = abs(matrix[i][j] - i)
    if direction == 'left': return matrix
    else:
        return [i[::-1] for i in matrix]

