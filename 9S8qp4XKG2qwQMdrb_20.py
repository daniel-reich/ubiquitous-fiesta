
def ways_to_climb(n):
  from itertools import permutations
  import math
​
  paths = []
  shortest = math.ceil(n/2)
​
  #iterate over different string lengths
  for l in range(shortest,n+1): 
    nums = []
​
    #figure out how many different 2s and 1s I should use for a given length l
    for i in range(n-l):
      nums.append(2)
​
    for i in range(l - len(nums)):
      nums.append(1)
​
    #get permutations. Add if not already in path
    new_paths = list(set([p for p in permutations(nums)]))
    for p in new_paths:
      if p not in paths:
        paths.append(p)
  return len(paths)

