
from collections import Counter
​
def number_pairs(txt):
    C = Counter([int(_) for _ in txt.split()[1:]])
    ans = 0
    for v in C.values():
        ans += v // 2
    return ans

