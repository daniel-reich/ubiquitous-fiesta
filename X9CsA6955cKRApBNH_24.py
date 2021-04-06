
from itertools import groupby
def longest_run(lst):
  try:
    differences= list(map(lambda x: x[1]-x[0],zip(lst[:-1],lst[1::])))
    groups = [list(g) for k, g in groupby(differences)]
    newlst = list(filter(lambda x: abs(x[0]) == 1,groups))
    longest = max(list(map(lambda x: len(x),newlst)))
    return longest + 1
  except ValueError:
    return 1

