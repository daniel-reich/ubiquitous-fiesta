
def alpha_clash(stringA, ind_A, str_Z, ind_Z):
    str_Z = [x for i,x in enumerate(str_Z) if i not in ind_A]
    stringA = [x for i,x in enumerate(stringA) if i not in ind_Z]
    a = {'A': 0, 'Z': 0}
    for x, y in zip(stringA, str_Z):
        if ord(x) > ord(y):
            a['A'] += ord(x) - ord(y)
        elif ord(y) > ord(x):
            a['Z'] += ord(y) - ord(x)
    return a

