
from math import factorial as f
​
def paths(x, y):
    if x == 0 or y == 0:
        return 1
    return f(x+y) / (f(x)*f(y))

