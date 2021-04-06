
def transpose(a):
    rows, cols = len(a), len(a[0])
    return [[a[c][r] for c in range(rows)] for r in range(cols)]
​
def matrix_product(m1, m2):
    rows1, cols1 = len(m1), len(m1[0])
    rows2, cols2 = len(m2), len(m2[0])
    if cols1 == rows2:
        res = [[0] * cols2 for r in range(rows1)]
        for r in range(rows1):
            for c in range(cols2):
                res[r][c] = sum(m1[r][i] * m2[i][c] for i in range(cols1))
        return res
​
def trace(m):
    return sum(m[i][i] for i in range(len(m)))
​
def double_dot(d1, d2):
    return trace(matrix_product(d1, transpose(d2)))

