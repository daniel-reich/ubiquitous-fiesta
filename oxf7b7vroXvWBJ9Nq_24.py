
def discount(n, txt):
    if not txt:
        return n
​
    percents = [float(p[:-1]) for p in txt.split(', ') if '%' in p]
    while percents:
        n -= n * (percents.pop() / 100)
    total = round(n - sum(float(n) for n in txt.split(', ') if '%' not in n), 2)
​
    return int(total) if str(total)[-2:] == '.0' else total

