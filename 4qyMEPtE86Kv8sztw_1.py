
from fractions import Fraction
​
def bin_to_fraction(b):
    ap, pp = b.split('.')
    return Fraction(int(ap,2) + int(pp, 2) / 2**len(pp))
​
def binary_sum(lst):
    sf = bin_to_fraction(lst[0]) + bin_to_fraction(lst[1])
    w, f = divmod(sf.numerator, sf.denominator)
    if w and f:
        return '{} {}/{}'.format(w, f, sf.denominator)
    return str(sf)

