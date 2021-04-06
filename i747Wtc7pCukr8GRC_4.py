
from itertools import combinations
from numpy import prod
def max_product(lst):
  return max([prod(i) for i in combinations(lst,3)])
​
def min_product(lst):
  return min([prod(i) for i in combinations(lst,3)])

