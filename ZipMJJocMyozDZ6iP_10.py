
from math import ceil
def group(lst, size):
  lst_count = ceil(len(lst)/size)
  res = [[] for i in range(lst_count)]
  i =  -1
  for itm in lst:
    i = (i + 1)%lst_count
    res[i].append(itm)
  return res

