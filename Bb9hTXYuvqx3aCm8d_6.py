
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    a = ''.join(i for i in str_A if str_A.index(i) not in ind_Z)
    z = ''.join(i for i in str_Z if str_Z.index(i) not in ind_A)
    a_score = sum(max(ord(a[i]) - ord(z[i]), 0) for i in range(16))
    z_score = sum(max(ord(z[i]) - ord(a[i]), 0) for i in range(16))
    return {'A': a_score, 'Z': z_score}

