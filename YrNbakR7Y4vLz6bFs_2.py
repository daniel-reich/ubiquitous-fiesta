
from itertools import product
def combinator(*lst):
  sep = lst[1] if len(lst) > 1 else ''
  return list(map(lambda x: sep.join(x),product(*lst[0])))

