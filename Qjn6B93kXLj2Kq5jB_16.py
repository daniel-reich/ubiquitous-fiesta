
from fractions import Fraction
​
​
def simplify_frac(f):
    n1, n2 = f.split("/")
    return str(Fraction(int(n1), int(n2)))

