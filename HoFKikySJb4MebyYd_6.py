
from copy import deepcopy
def transform_matrix(lst):
  colsum = lambda c: sum([lst[r][c] for r in range(len(lst))])
  rlst = deepcopy(lst)
  for r in range(len(lst)):
    for c in range(len(lst[0])):
      rlst[r][c] = sum([val for val in lst[r]]) + colsum(c) - 2 * lst[r][c]
  return rlst

