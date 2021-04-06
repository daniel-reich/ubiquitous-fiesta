
from collections import Counter
​
def max_occur(text):
    C = Counter(text)
    m = max(C.values())
    if m <= 1:
        return "No Repetition"
    return sorted([k for k,v in C.items() if v == m])

