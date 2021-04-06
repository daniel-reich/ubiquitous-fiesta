
from itertools import groupby as gb
def compress(chars):
  A=[(x, len(list(g))) for x, g in gb(chars)]
  B=['{}{}'.format(x[0], x[1] if x[1]>1 else '') for x in A]
  return ''.join(B)

