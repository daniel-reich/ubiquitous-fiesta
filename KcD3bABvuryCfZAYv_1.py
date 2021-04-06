
import collections
​
def most_frequent_char(lst):
  counter = collections.Counter("".join(lst))
  return sorted(k for k, v in counter.items() if v == counter.most_common(1)[0][1])

