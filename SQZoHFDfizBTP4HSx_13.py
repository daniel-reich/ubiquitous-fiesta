
from collections import Counter
​
def missing_alphabets(txt):
    C = Counter(txt)
    if len(C.keys()) == 26 and len(set(C.values())) == 1:
        return ""
    m = max(C.values())
    return ''.join([c * (m - C.get(c, 0)) for c in "abcdefghijklmnopqrstuvwxyz"])

