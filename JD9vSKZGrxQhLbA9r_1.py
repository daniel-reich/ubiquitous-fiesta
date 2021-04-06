
def pile_of_cubes(m):
    n = 0
    while (m > 0):
        n += 1
        m -= n**3
    return n if m == 0 else None

