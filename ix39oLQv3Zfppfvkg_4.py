
def multiply_matrix(m1, m2):
    rows1, cols1 = len(m1), len(m1[0])
    rows2, cols2 = len(m2), len(m2[0])
    if cols1 == rows2:
        res = [[0] * cols2 for r in range(rows1)]
        for r in range(rows1):
            for c in range(cols2):
                res[r][c] = sum(m1[r][i] * m2[i][c] for i in range(cols1))
        return res
    return "ERROR"

