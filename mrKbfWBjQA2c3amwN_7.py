
def mult_table(n):
    res = [x * y for x in range(1, n + 1) for y in range(1, n + 1)]
    return [res[x:x+n] for x in range(0, len(res), n)]

