
from collections import Counter
​
def most_frequent_char(lst):
  c = Counter(c for word in lst for c in word)
  l = [p[0] for p in c.most_common() if p[1] == c.most_common()[0][1]]
  return sorted(l)

