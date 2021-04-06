
def pricey_prod(d):
    V = []
    for value in sorted(d.values(), reverse=True):
        if value >= 500:
            v = list(d.keys())[(list(d.values())).index(value)]
            V.append(v)
    return V

