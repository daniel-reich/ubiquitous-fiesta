
from collections import Counter
​
​
def advanced_sort(lst):
    c = Counter(lst)
    pairs = ((k, [k] * v) for k, v in c.items())
    return [
        b
        for a, b in sorted(pairs, key=lambda x: lst.index(x[0]))
    ]

