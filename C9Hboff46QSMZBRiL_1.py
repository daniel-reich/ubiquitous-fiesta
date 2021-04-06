
from math import ceil
def kth_string(s, m, k):
    n = len(s)
    res = [0] * m
    lens = [0] * (m - 1)
    lens[0] = n + 1
    for i in range(1, m - 1):
        lens[i] = lens[i - 1] * n + 1
    lens = lens[::-1]
    for i in range(m - 1):
        digit = ceil(k / lens[i])
        res[i] = digit
        k -= (digit - 1) * lens[i] + 1
        if k == 0:
            break
    else:
        res[m - 1] = k
    letters = sorted(s)
    return ''.join(letters[i - 1] for i in res if i > 0)

