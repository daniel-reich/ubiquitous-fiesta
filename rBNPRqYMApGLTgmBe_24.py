
def combinations(k, n):
  import operator as op
  from functools import reduce
  k = min(k, n-k)
  numer = reduce(op.mul, range(n, n-k, -1), 1)
  denom = reduce(op.mul, range(1, k+1), 1)
  return numer / denom

