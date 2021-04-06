
from itertools import product
​
​
def relation_lst(lst):
  return list(
    (i, j)
    for i, j in product(sorted(lst), repeat=2)
    if i <= j
  )

