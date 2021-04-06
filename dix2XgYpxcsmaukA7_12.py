
from itertools import groupby
def prime_factors(num):
    res = []
    while not num % 2:
        num //= 2
        res += [2]
    divisor = 3
    while num > 1:
        while not num % divisor:
            num //= divisor
            res += [divisor]
        divisor += 2
    return res
​
def express_factors(n):
    res = []
    for k, g in groupby(prime_factors(n)):
        len_g = len(list(g))
        res.append('{}'.format(k) if len_g < 2
                   else '{}^{}'.format(k, len_g))
    return ' x '.join(res)

