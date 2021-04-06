
from fractions import gcd
def fractions(decimal):
    d,l = decimal.index('.'), decimal.index('(')
    bd, ad, rp = decimal[:d], decimal[d+1:l], decimal[l+1:-1]
    den = 10**(len(ad)+len(rp)) - 10**int(len(ad))
    num = int(bd+ad+rp) - int(bd+ad)
    g = gcd(den, num)
    return '{}/{}'.format(num//g, den//g)

