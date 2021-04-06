
from itertools import product as PD
def combinator(*lst):
  if [] in lst[0]:
    return []
  
  else:
    if len(lst)==1:
      B=[''.join(list(x)) for x in PD(*lst[0])]
      return B
    else:
      return [' '.join(list(x)) for x in PD(*lst[0])]

