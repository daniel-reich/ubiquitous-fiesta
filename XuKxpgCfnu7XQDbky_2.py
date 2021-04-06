
from math import sqrt
def sum_and_product(s, p):
    delta = s**2 - 4*p
    if delta < 0:
        return None
    elif delta == 0:
        return (s/2, s/2)
    else:
        return (round((s - sqrt(delta))/2, 3), round((s + sqrt(delta))/2, 3))

