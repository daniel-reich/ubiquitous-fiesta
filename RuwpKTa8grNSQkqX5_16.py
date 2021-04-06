
def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
​
def fractions(decimal):
    a, b = decimal.split('.')
    a = int(a)
    c, d = b.replace(')', '').split('(')
    n = len(d)
    m = len(c)
    d = int(d)
    if m == 0:
        # repeat starts immediately after decimal point:
        denom = 10**n - 1
        num = a * denom + d
        g = gcd(num, denom)
        denom //= g
        num //= g
        return str(num) + '/' + str(denom)
    else:
        # repeat does NOT start immediately after decimal point:
        c = int(c)
        f1 = 10**(n+m)
        f2 = 10**m
        f3 = 10**n
        denom = f1 - f2
        num = a * (f1 - f2) + c * f3 + int(d) - int(c)
        g = gcd(num, denom)
        denom //= g
        num //= g
        return str(num) + '/' + str(denom)

