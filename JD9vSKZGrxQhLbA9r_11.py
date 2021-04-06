
def pile_of_cubes(m):
    if m >= 10252519345963644753026: return None
    x = m**0.5
    if (x%1==0):
        c = 1
        while (x != c and x > 0):
            x = x - c
            c = c + 1
        if (x == c):
            return c
    return None

