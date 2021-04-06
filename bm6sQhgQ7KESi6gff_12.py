
from collections import Counter
def find_the_difference(s, t):
  scnt = Counter(s)
  tcnt = Counter(t)
  for l in tcnt:
    if tcnt[l]>scnt[l]:
      return l

