
from itertools import zip_longest
def bridge_shuffle(lst1, lst2):
  return [y for x in zip_longest(lst1,lst2) for y in x if y]
print(bridge_shuffle(["C", "C", "C", "C"], ["D"]))

