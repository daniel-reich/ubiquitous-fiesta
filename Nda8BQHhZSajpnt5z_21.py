
import fractions
from functools import reduce
​
def GCD(lst):
    return reduce(fractions.gcd, lst)

