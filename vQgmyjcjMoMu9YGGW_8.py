
def simplify(txt):
    gcd = lambda a,b: a if b == 0 else gcd(b,a%b)
    num = [int(n) for n in txt.split('/')]
    d = gcd(*num)
    num = [n//d for n in num]
    if num[-1] == 1: num.pop()
    return '/'.join(str(n) for n in num)

