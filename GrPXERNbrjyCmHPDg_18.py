
from collections import Counter
def duplicate_count(txt):
  return len([x for x in Counter(list(txt)).values() if x > 1])

