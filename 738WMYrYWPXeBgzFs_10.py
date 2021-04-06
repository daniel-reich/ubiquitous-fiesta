
from collections import Counter
​
def is_valid(txt):
    vals = list(Counter(txt).values())
    if len(set(vals)) == 1:
        return "YES"
    if len(set(vals)) > 2:
        return "NO"
    m = max(vals)
    return "YES" if vals.count(m) == 1 and m - min(vals) == 1 else "NO"

