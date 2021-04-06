
import itertools
def get_subsets(lst, n):
  combs = []
  
  for i in range(len(lst)+1):
    combinations = itertools.combinations(lst,i)
    for c in combinations:
      if sum(c) == n:
        combs.append(list(c))
​
  res = []
  for j in range(1,len(lst)+1):
    res += sorted([item for item in combs if len(item)==j])
​
  return res

