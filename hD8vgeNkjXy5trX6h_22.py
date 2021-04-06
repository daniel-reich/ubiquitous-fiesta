
import itertools
def combo(lst, n):
  return [list(i) for i in itertools.combinations(lst,n)]

