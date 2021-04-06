
def rotate_matrix(mat, turns=1):
    turns = turns % 4
    res = mat.copy()
    while turns:
        res = [list(tpl)[::-1] for tpl in zip(*res)]
        turns -= 1
    return res

