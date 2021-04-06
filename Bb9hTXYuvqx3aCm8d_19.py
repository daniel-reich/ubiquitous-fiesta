
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    buf_a = [str_Z[x] for x in ind_A]
    res_a = ''.join([x for x in str_Z if x not in buf_a])
    buf_z = [str_A[x] for x in ind_Z]
    res_z = ''.join([x for x in str_A if x not in buf_z])
    tot_a = [a - b for a, b in zip([ord(x) for x in res_a], [ord(x) for x in res_z])]
    A = abs(sum([x for x in tot_a if x < 0]))
    Z = abs(sum([x for x in tot_a if x > 0]))
    return {'A': A, 'Z': Z}

