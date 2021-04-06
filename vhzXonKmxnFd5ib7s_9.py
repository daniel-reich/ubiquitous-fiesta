
def matrix_multiply(a, b):
    n, m, p, q, res = len(a), len(a[0]), len(b), len(b[0]), []
    if m != p:
        return 'invalid'
    for i in range(n):
        res.append(q * [0])
    for i in range(n):
        for j in range(q):
            res[i][j] = sum(a[i][k] * b[k][j] for k in range(m))
    return res

