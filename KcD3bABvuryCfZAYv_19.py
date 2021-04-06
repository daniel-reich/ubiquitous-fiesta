
from collections import Counter
def most_frequent_char(lst):
  S = "".join(lst)
  L = []
  for k,v in Counter(S).items():
    if v > 3:
      L.append(k)
  return sorted(L)

