
import itertools
def simple_pair(lst, n):
  pairs = list(itertools.combinations(lst, 2))
  result = [pair for pair in pairs if (pair[0] * pair[1]) == n]
  return list(result[0]) if len(result) != 0 else None

