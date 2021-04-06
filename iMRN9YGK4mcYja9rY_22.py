
def accumulating_product(lst):
  import itertools
  import operator
  nlst = []
  res = itertools.accumulate(lst,operator.mul)
  for i in res:
    nlst.append(i)
  return nlst

