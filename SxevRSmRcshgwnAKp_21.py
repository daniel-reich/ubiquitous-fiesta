
def pricey_prod(d):
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return [k for k, v in d if v > 499]

