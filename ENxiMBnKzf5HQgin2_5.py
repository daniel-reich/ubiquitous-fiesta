
def pascal_row(n):
    r = [1]
    if n == 0:
        return r
    for i in range(1, n):
        add = r[-1] * (n + 1 - i) // i
        r.append(add)
    return r + [1]

