
from itertools import groupby
def compress(chars):
  result = []
  for k, g in groupby(chars):
    group = tuple(g)
    if len(group) > 1:
      result.append(k + str(len(group)))
    else:
      result.append(k)
  return ''.join(result)

