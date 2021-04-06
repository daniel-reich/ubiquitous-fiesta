
from collections import Counter
​
def frequency_sort(s):
    C = Counter(s)
    A = []
    for c, cnt in C.items():
        A.append([c, ord(c), cnt])
    A.sort(key=lambda x: (-x[2], x[1]))
    ans = ""
    for c, o, cnt in A:
        ans += c * cnt
    return ans

