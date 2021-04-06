
def pile_of_cubes(m):
    i = 1;
    r = 0;
    while r <= m:
        r += pow(i, 3)
        i += 1
        if r == m:
            return i-1
    return None;

