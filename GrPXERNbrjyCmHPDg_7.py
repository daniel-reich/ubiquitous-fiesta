
from collections import Counter
def duplicate_count(txt):
  c = Counter(txt)
  d = [k for k,v in c.items() if v >= 2]
  return len(d)

