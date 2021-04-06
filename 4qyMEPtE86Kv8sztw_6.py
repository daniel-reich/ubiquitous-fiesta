
from fractions import Fraction
​
def convert(b):
    x, y = b.split('.')
    ans = Fraction(int('0b' + x, 2), 1)
    p = 0
    for digit in y:
        p += 1
        if digit == '1':
            ans += Fraction(1, 2**p)
    return ans
​
def binary_sum(lst):
    a = convert(lst[0])
    b = convert(lst[1])
    c = a + b
    n, d = c.numerator, c.denominator
    whole = n // d
    fractional = n % d
    if fractional == 0:
        return str(whole)
    ans = "" if whole == 0 else str(whole) + ' '
    ans += str(n % d) + '/' + str(d)
    return ans

