
from numpy import prod
def mystery_func(num):
  a=[2]
  while prod(a)*2<num:
    a.append(2)
  a.append(num-prod(a))
  return int(''.join(str(x) for x in a))

