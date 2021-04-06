
from itertools import combinations
​
def combos(lst):
  com = []
  for s in combinations(lst, 3):
    if list(s) not in com:
      com.append(list(s))
  for x in range(len(com)):
    com[x] = com[x][0] * com[x][1] * com[x][2]
  return com
​
def max_product(lst):
  lst = combos(lst)
  return max(lst)
​
def min_product(lst):
  lst = combos(lst)
  return min(lst)

