
from math import factorial as f
def kempner(n, i=1):
    return kempner(n, i +1) if f(i)%n else i

