
from itertools import combinations
​
def zero_indices(lst, k):
  indices = [idx for idx, i in enumerate(lst) if not i]
  combos = [list(i) for i in combinations(indices, k)]
  
  return max(combos, key=lambda x: longest_run(flip_bits(lst, x)))
  
def flip_bits(lst, combo):
  return [i or int(idx in combo) for idx, i in enumerate(lst)]
  
def longest_run(lst):
  return max(len(i) for i in ''.join(map(str, lst)).split('0'))

