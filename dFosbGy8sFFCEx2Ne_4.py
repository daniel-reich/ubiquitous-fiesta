
def rank(lst):
    d = dict()
    for p in [[val, i] for i, val in enumerate(sorted(lst))]:
        if p[0] in d:
            d[p[0]] += p[1]
        else:
            d[p[0]] = p[1]
    for k, v in d.items():
        d[k] /= lst.count(k)
    return [d[k] for k in lst]

