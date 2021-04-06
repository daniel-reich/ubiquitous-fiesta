
from itertools import combinations
​
def zero_indices(lst, k):
  lst = list(map(str, lst))
  best_run = 0
  indices = ()
  
  zero_positions = [idx for idx, i in enumerate(lst) if i == '0']
  for comb in combinations(zero_positions, k):
    arr = lst[:]
    for i in comb:
      arr[i] = '1'
    max_run = max(len(i) for i in ''.join(arr).split('0'))
    if max_run > best_run:
      best_run = max_run
      indices = comb
      
  return list(indices)

