
from collections import Counter
​
def mode(nums):
  c = Counter(nums)
  return [x for x,y in sorted(c.items()) if y == max(c.values())]

