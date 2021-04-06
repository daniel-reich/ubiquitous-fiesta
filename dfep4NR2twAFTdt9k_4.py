
def row(m, i):
    return m[i]
​
def col(m, i):
    res = []
    for j in range(len(m)):
        res.append(m[j][i])
    return res
​
def mult_entry(m1, m2, x, y):
    res = 0
    r = row(m1, x)
    c = col(m2, y)
    for i in range(len(m1[0])):
        res += r[i] * c[i]
    return res
​
def matrix_mult(m1,m2):
    m = len(m1)
    n = len(m1[0])
    res = [[0 for y in range(n)] for x in range(m)]
    for x in range(m):
        for y in range(n):
            res[x][y] = mult_entry(m1, m2, x, y)
    return res

