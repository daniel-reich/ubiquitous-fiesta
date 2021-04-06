
from numpy import sign
def modulo(x, y):
    if abs(x) < abs(y):
        return x
    if sign(x) == sign(y):
        return modulo(x-y, y)
    else:
        return modulo(x+y,y)

