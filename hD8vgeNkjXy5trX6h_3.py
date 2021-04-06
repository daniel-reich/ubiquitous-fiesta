
import itertools
def combo(lst, n):
  tmp = []
  for comb in itertools.combinations(lst, n):
    tmp.append(list(comb))
  return tmp

