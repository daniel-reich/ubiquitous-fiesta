
from collections import Counter
​
def make_anagram(a, b):
    Ca = Counter(a)
    Cb = Counter(b)
    ans = 0
    for k in range(97, 123):
        c = chr(k)
        ans += abs(Ca.get(c, 0) - Cb.get(c, 0))
    return ans

