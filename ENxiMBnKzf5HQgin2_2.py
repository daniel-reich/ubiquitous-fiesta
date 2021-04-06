
def pascal_row(n):
    res = [1]
    for i in range(n):
        res.append(res[i]*(n - i) // (i + 1))
    return res

