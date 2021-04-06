
from collections import Counter
​
def duplicates(txt):
  count = Counter(txt)
  res = []
  for n in count.values():
    if n > 1:
      res.append(n - 1)
  return sum(res)

