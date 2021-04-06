
from itertools import combinations as C
def min_difference_pair(nums):
  return sorted(list(min(C(nums,2), key=lambda x: (abs(x[0]-x[-1]), x[0]))))

