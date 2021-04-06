
def discount(n, txt):
    p, t = [], []
    if not txt:
        return n
    for i in txt.split(", "):
        if "%" in i:
            p.append(float(i[:-1]))
        else:
            t.append(float(i))
    for x in p:
        n *= (100 - x) / 100
    for y in t:
        n -= y
    return round(n, 2)

