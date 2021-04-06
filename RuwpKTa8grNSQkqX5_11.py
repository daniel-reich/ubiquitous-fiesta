
import re
from fractions import Fraction
​
def fractions(decimal):
    i, f, p = re.match(r'(\d+)\.(\d*)\((\d+)\)', decimal).groups()
    pow1, pow2 = 10**len(f), 10**len(p)
    i, f, p = int(i), int(f or '0'), int(p)
    print(i,f,p)
    return str(Fraction(f, pow1) + Fraction(p, pow1 * (pow2-1)) + i)

