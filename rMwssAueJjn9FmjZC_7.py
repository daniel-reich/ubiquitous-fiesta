
from collections import Counter
def number_pairs(txt):
    return sum([v // 2  for k,v in Counter(txt.split()[1:]).items() if v > 1])

