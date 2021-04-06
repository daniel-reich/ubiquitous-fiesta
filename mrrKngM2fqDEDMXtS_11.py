
from itertools import groupby
​
def can_patch(bridge, planks):
  l = [len(list(i)) for g,i in groupby(bridge) if g == 0]
  l1 = sorted([v for v in l if v>1], reverse = True)
  planks = sorted(planks, reverse= True)
  if len(planks) < len(l1):
    return False
  for i in range(len(l1)):
    if l1[i] > planks[i] + 1:
      return False 
  return True

