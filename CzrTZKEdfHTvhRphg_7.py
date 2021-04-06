
def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
​
def mixed_number(frac):
    if frac[0] == '-':
        ans = "-"
        frac = frac[1:]
    else:
        ans = ""
    n, d = [int(_) for _ in frac.split('/')]
    if n % d == 0:
        return ans + str(n // d) 
    if n > d:
        ans += str(n // d) + ' '
        n %= d
    g = gcd(n, d)
    n //= g
    d //= g
    ans += str(n) + '/' + str(d)
    return ans

