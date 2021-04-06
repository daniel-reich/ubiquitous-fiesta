
def rotate_matrix(mat, turns=1):
    m = mat[:]
    pos = abs(turns)%4 * (-1 if turns < 0 else 1)
    if pos in (-2, 2):
        return [list(i[::-1]) for i in m[::-1]]
    if pos in (-3, 1):
        return [list(i[::-1]) for i in (zip(*m))]
    if pos in (-1, 3):
        return [list(i) for i in (zip(*m))][::-1]
    return m

