
def discount(n, txt):
    percs, subs = [], []
    for disc in txt.split(','):
        if len(disc) == 0:
            continue
        if '%' in disc:
            percs.append(float(disc[:-1]))
        else:
            subs.append(float(disc))
    for perc in percs:
        n = n * (1. - perc / 100)
    n -= sum(subs)
    return round(n, 2)

