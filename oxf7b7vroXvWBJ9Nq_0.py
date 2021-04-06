
def discount(n, txt):
    if not txt:
        return n
    discounts = sorted(txt.split(', '), key=lambda x: not x.endswith('%'))
    for i in discounts:
        if i.endswith('%'):
            n *= (100 - float(i[:-1])) / 100
        else:
            n -= float(i)
    return round(n, 2)

