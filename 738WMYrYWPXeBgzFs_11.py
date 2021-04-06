
from collections import Counter
​
​
def is_valid(txt):
    c = Counter(txt)
    l = [c.get(i) for i in c]
    if len(set(l)) == 1 or (len(set([i for i in sorted(l)[:-1]])) == 1 and sorted(l)[-1] == sorted(l)[-2]+1):
        return "YES"
​
    return "NO"

