
from functools import *
from operator import *
def find_odd(l): return reduce(xor, l, 0)

