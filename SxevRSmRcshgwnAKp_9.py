
def pricey_prod(d):
    x = sorted([(v,k) for k,v in d.items() if v >= 500], reverse = True)
    return [k for v,k in x]

