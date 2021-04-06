
def row_sum(n):
    start = 1
    for r in range(1, n + 1):
        start = start + (r - 1)
    s = sum([start + k for k in range(n)])
    return s

