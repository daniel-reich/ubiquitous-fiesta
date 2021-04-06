
import itertools
def combo(lst, n):
  return [list(x) for x in itertools.combinations(lst,n)]

