
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    lst_a = [ord(c) for i, c in enumerate(str_A) if i not in ind_Z]
    lst_z = [ord(c) for i, c in enumerate(str_Z) if i not in ind_A]
    res = {'A': 0, 'Z': 0}
    for i in range(len(lst_a)):
        if lst_a[i] > lst_z[i]:
            res['A'] += lst_a[i] - lst_z[i]
        elif lst_a[i] < lst_z[i]:
            res['Z'] += lst_z[i] - lst_a[i]
    return res

