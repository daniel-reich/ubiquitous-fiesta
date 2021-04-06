
import math
def simple_comp(lst1, lst2):
  if lst2 == None or lst1 == None:
    return False
  lst1 = list(map(abs, lst1))
  lst2 = list(map(lambda num: int(math.sqrt(num)), lst2))
  return sorted(lst1) == sorted(lst2)

