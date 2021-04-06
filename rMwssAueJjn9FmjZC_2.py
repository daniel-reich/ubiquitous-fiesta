
from collections import Counter
def number_pairs(txt):
  cnt = Counter(txt[2:].split())
  return sum(cnt[e]//2 for e in cnt)

