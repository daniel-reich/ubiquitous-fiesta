
def rotate_matrix(mat, turns=1):
    m, n, turns = len(mat), len(mat[0]), turns%4
    if turns == 3:
        return [[mat[r][c] for r in range(m)] for c in range(n-1, -1, -1)]
    elif turns == 2:
        return [row[::-1] for row in mat[::-1]]
    elif turns == 1:
        return [[mat[r][c] for r in range(m-1, -1, -1)] for c in range(n)]
    else:
        return [row[::] for row in mat]

