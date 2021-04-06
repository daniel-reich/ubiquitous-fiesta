
from math import factorial as f
def non_repeats(r):
    return sum(f(r -1)//f(i) for i in range(r))*(r -1)

