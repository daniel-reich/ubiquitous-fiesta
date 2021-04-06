
from fractions import Fraction
import math
def vol_shell(r1, r2):
    R = max(r1,r2)
    r = min(r1,r2)
    return round(Fraction(4, 3) * math.pi * (R**3 - r**3), 3)

