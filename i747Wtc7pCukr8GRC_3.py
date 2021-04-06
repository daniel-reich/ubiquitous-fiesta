
import itertools
def max_product(lst):
  pos = list(itertools.combinations(lst,3))
  return max([get_product(p) for p in pos])
​
def min_product(lst):
  pos = list(itertools.combinations(lst,3))
  return min([get_product(p) for p in pos])
​
def get_product(nums,res=1):
  for num in nums:
    res *= num
  return res

