
from math import log
def josephus(n):
    return 2*(n-(2**int(log(n)/log(2))))+1

