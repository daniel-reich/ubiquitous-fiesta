
import itertools
def max_product(lst):
  return max([x[0]*x[1]*x[2] for x in itertools.permutations(lst)])
​
def min_product(lst):
  return min([x[0]*x[1]*x[2] for x in itertools.permutations(lst)])

