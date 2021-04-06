
from itertools import zip_longest
​
def can_patch(bridge, planks):
  gaps = ''.join(str(i) for i in bridge).split('1')
  gaps = sorted([len(str(i)) for i in gaps], reverse=True)
  planks = sorted(planks, reverse=True)
  
  if not planks:
    return True if max(gaps) == 1 else False 
  return all(b >= a-1 for a, b in zip_longest(gaps, planks, fillvalue=0))

