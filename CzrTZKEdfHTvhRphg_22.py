
from fractions import Fraction
def mixed_number(frac):
    frac= Fraction(str(frac)) 
    n, d = (frac.numerator, frac.denominator)
    m, p = divmod(abs(n), d)
    if n==0:
        return '0'
    if n < 0:
        m = -m
    return '{} {}/{}'.format(m, p, d) if m != 0 and p > 0 \
        else '{}'.format(m) if m != 0 \
        else '{}/{}'.format(n,d)

