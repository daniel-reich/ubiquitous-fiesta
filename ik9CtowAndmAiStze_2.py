
from collections import Counter
def frequency_sort(s):
    cnt = [(k, v) for k, v in Counter(s).items()]
    cnt.sort(key=lambda t: (-t[1], t[0]))
    return "".join(t[0] * t[1] for t in cnt)

