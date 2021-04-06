
from itertools import groupby
def is_there_consecutive(lst, n, times):
  return (times == 0 and not n in lst) or any(True for g in groupby(lst) if g[0] == n and len(list(g[1])) == times)

