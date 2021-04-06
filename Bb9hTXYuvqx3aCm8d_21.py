
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    score = {'A': 0, 'Z': 0}
    A = [x for i, x in enumerate(str_A) if i not in set(ind_Z)]
    Z = [y for j, y in enumerate(str_Z) if j not in set(ind_A)]
    for a, z in zip(A, Z):
        val = ord(a) - ord(z)
        if val > 0:
            score['A'] += val
        elif val < 0:
            score['Z'] -= val
    return score

