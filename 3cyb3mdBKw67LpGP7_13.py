
from itertools import groupby
def numbers_need_friends_too(n):
  l = [list(x) for y,x in groupby(str(n)) ]
  return  int(''.join(''.join(x*3) if len(x) == 1 else ''.join(x) for x in l))

