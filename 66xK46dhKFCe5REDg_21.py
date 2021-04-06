
def x_and_o(board):
    matrix, codes = [], {'X': 1, 'O': -1, ' ': 0}
    for s in board:
        matrix.append([codes[c] for c in s.split('|')])
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                if sum(matrix[i]) == 2 \
                        or matrix[0][j] + matrix[1][j] + matrix[2][j] == 2:
                    return [i + 1, j + 1]
                if i == 1 and j == 1:
                    if matrix[0][0] + matrix[2][2] == 2 \
                            or matrix[2][0] + matrix[0][2] == 2:
                        return [i + 1, j + 1]
                if i == 0 and j == 0:
                    if matrix[1][1] + matrix[2][2] == 2:
                        return [i + 1, j + 1]
                if i == 0 and j == 2:
                    if matrix[1][1] + matrix[2][0] == 2:
                        return [i + 1, j + 1]
                if i == 2 and j == 0:
                    if matrix[1][1] + matrix[0][2] == 2:
                        return [i + 1, j + 1]
                if i == 2 and j == 2:
                    if matrix[1][1] + matrix[0][0] == 2:
                        return [i + 1, j + 1]
    return False

