
from itertools import groupby
​
def look_and_say(start, n):
    seq = [start]
    for _ in range(n-1):
        seq.append(int(''.join(str(len(list(g))) + k for k, g in groupby(str(seq[-1])))))
    return seq

