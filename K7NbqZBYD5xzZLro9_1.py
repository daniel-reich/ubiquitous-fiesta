
from math import log10
def digits_sum(start, stop):
    res = 0
    if stop < 1000:
        for i in range(start, stop + 1):
            res += sum(int(c) for c in str(i))
    else:
        n = int(log10(stop))
        total = 45 * pow(10, n - 1) * n
        before = 0
        for i in range(start):
            before += sum(int(c) for c in str(i))
        res = total + 1 - before
    return res

