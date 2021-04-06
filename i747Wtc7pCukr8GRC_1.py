
#brute force ftw
from itertools import combinations as c
​
def max_product(lst):
  return max(x*y*z for x,y,z in c(lst,3))
​
def min_product(lst):
  return min(x*y*z for x,y,z in c(lst,3))

