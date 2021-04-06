
from collections import Counter
def make_anagram(a, b):
    res, s = 0, set(a) & set(b)
    cnt_a, cnt_b = Counter(a), Counter(b)
    for k, v in cnt_a.items():
        if k not in s:
            res += v
    for k, v in cnt_b.items():
        if k not in s:
            res += v
    for c in s:
        res += abs(cnt_a[c] - cnt_b[c])
    return res

