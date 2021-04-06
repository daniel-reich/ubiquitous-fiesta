
import itertools
def max_total(nums):
  return max(sum(c) for c in itertools.combinations(nums,5))

