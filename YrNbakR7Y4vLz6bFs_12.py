
def combinator(lst, sep = ''):
    from numpy import prod
    lengths = list(map(len, lst))
    if not all(lengths): return []
    tot = int(prod(lengths))
    prods = [int(tot / prod(lengths[:i+1])) for i in range(len(lst))]
    res = []
    for ind, i in enumerate(lst):
        temp = []
        for j in i:
            temp += [j] * prods[ind]
        res += [temp * int(tot / len(temp))]
    return [sep.join(i) for i in zip(*res)]

