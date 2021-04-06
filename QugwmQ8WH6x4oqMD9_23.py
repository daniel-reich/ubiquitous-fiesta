
from collections import Counter
def count_identical_lists(lst1, lst2, lst3, lst4):
  L = [lst1,lst2,lst3,lst4]
  NL = ["".join(map(str,i)) for i in L]
  for v in Counter(NL).values():
    if v>1:
      return v
    return 0

