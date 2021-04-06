
from itertools import permutations
def max_product(lst):
  perm=permutations(lst,3)
  c=-123234523
  prod=1
  for i in list(perm):
    for d in i:
      prod=prod*d
    if prod>c:
      c=prod
    prod=1
  return c
  
def min_product(lst):
  perm=permutations(lst,3)
  c=123423432
  prod=1
  for i in list(perm):
    for d in i:
      prod=prod*d
    if prod<c:
      c=prod
    prod=1
  return c

