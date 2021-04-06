
def pile_of_cubes(m):
    s = n = 1
    while s < m:
        n += 1
        s += n * n * n
    return n if s == m else None

