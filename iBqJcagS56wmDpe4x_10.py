
from math import pi 
​
def vol_shell(r1, r2):
    v = abs(round(((4 / 3) * pi) * (r1**3 - r2**3), 3))
    return v

