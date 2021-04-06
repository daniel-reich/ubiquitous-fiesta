
from itertools import zip_longest
​
def bridge_shuffle(lst1, lst2):
  result = []
  for item1, item2 in zip_longest(lst1, lst2):
      if item1:
        result.append(item1)
      if item2:
        result.append(item2)
  return result

