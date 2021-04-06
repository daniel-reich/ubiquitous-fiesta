
def pricey_prod(d):
    prices = sorted(([k, v] for k, v in d.items() if v >= 500), key=lambda l: l[1], reverse=True)
    return [p[0] for p in prices]

