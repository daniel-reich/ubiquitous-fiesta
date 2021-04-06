
def two_product(arr, N):
    import itertools
    r = []
    for i in list(itertools.combinations(arr, 2)):
        if i[0] * i[1] == N:
            r.append([i[0],i[1]])
    if r:
        r1 = []
        for i in r:
            r1.append(sum(arr.index(j) for j in i))
        return r[r1.index(min(r1))]
    return None

