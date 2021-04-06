
from math import log2
double_factorial = lambda num: round(2 ** sum([log2(i) for i in range(2 - num % 2, num + 1, 2)]))

