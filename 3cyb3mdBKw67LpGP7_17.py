
from itertools import groupby
​
def numbers_need_friends_too(n):
  newnum = ""
​
  for k, g in groupby(str(n)):
    group = list(g).copy()
    newnum += k * 3 if len(group) == 1 else "".join(group)
​
  return int(newnum)

