
def farey(n):
    dct = {0: (0,1), 1: (1,1)}
    for den in range(n,0,-1):
        for num in range(1, den):
            dct[num/den] = (num, den)
    res = sorted(dct.items(), key=lambda x: x[0])
    return ['{}/{}'.format(*b) for _, b in res]

