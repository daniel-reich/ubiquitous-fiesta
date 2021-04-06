
from math import log10, floor
count = lambda n: 1 if n == 0 else floor(log10(abs(n))) + 1

