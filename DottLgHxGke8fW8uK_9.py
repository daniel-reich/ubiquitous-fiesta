
from math import factorial, log2
nPr = lambda n, r: round(2 ** sum([log2(n - i) for i in range(r)]))
​
nCr = lambda n, r: round(nPr(n, min(r, n - r)) / factorial(min(r, n - r)))

