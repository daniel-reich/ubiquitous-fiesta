
from collections import Counter
def duplicate_count(txt):
  return sum([1 for v in Counter(txt).values() if v > 1])

