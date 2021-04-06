
from fractions import Fraction as frac
​
def binary_sum(lst):
    groups = []
    for s in lst:
        left, right = s.split('.')
        groups += [frac(int(left, 2))] + [frac(0.5**idx*int(i)) for idx, i in enumerate(right, 1)]
    res = sum(groups)
    n, d = res.numerator, res.denominator
    if d == 1:
        return str(n)
    return '{} {}'.format(n//d, str(res - frac(n//d))).lstrip('0 ')

