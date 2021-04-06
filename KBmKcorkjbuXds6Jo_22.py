
import itertools
def chocolates_parcel(n_small, n_big, order):
  res = []
  for c in itertools.product(list(range(n_small+1)), list(range(n_big+1))):
    if c[0]*2 + c[1]*5 == order:
      res.append((c[0], c[1]))
  if res == []:
    return -1 
  else:
    return sorted(res)[0][0]

