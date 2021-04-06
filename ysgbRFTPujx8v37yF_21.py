
def row_sum(n):
    beg = (n**2 - n + 2) // 2
    return sum(x for x in range(beg, beg + n))

