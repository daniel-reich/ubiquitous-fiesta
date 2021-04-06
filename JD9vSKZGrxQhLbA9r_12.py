
def pile_of_cubes(m):
    s = 0
    n = 0
    while s < m:
        n += 1
        s += n ** 3
    return [None, n][s == m]

