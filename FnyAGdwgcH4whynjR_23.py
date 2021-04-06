
import itertools
def get_subsets(lst, n):
  subsets = {}
  for i in range(len(lst)+1):
    subsets[i] = []
  for choice in itertools.product([0,1],repeat=len(lst)):
    subset = [lst[i] for i in range(len(choice)) if choice[i]]
    if sum(subset) == n:
      subsets[len(subset)].append(tuple(subset))
  return [list(t) for v in subsets.values() for t in sorted(v)]

