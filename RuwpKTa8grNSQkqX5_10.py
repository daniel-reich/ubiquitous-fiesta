
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
​
​
def fractions(d):
    p, r = d.find("."), d.find("(")
    whole = (int(d[:p]), 1)
    dec = (int(d[p + 1:r]), 10 ** (r - p - 1)) if r - p > 1 else (0, 1)
    rep = (int(d[r + 1:-1]), (10 ** (len(d) - r - 2) - 1) * 10 ** len(d[p + 1:r]))
    rep = [i / gcd(rep[1], rep[0]) for i in rep]
    e = dec[1] * rep[1] / gcd(dec[1], rep[1])
    f = [whole[0] * e + dec[0] * e / dec[1] + rep[0] * e / rep[1], e]
    return str(int(f[0] / gcd(f[1], f[0]))) + "/" + str(int(f[1] / gcd(f[1], f[0])))

