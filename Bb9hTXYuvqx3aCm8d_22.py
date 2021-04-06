
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    res = {'A': 0, 'Z': 0}
    A = [ord(i) for idx, i in enumerate(str_A) if idx not in ind_Z]
    Z = [ord(i) for idx, i in enumerate(str_Z) if idx not in ind_A]
​
    for a, z in zip(A, Z):
        if a >= z:
            res['A'] += a - z
        else:
            res['Z'] += z - a
    return res

