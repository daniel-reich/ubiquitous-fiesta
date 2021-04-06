
def pricey_prod(d):
    return [i[0] for i in sorted(d.items(), key=lambda kv: -kv[1]) if i[1] >= 500]

