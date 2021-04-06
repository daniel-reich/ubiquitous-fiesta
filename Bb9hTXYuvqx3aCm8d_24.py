
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    values_A = [ord(str_A[i]) for i in range(26) if i not in ind_Z]
    values_Z = [ord(str_Z[i] )for i in range(26) if i not in ind_A]
    A, Z = 0, 0
    for i in range(16):
        va, vz = values_A[i], values_Z[i]
        if va > vz:
            A += va - vz
        elif vz > va:
            Z += vz - va
    return {'A': A, 'Z': Z}

