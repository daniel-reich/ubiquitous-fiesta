
def pascals_triangle(row):
    n, res = 1, [1, 1]
    while n < row:
        res = [1] + [sum(res[n:n+2]) for n in range(n+1)]
        n += 1
    return ' '.join(map(str, res))

