
from math import ceil
def hats(lst):
  best=min(lst[1])
  t=best*ceil(lst[0]*(1/best)/(sum(1/i for i in lst[1])))
  while sum(t//i for i in lst[1])<lst[0]:t+=1
  if sum(t//i for i in lst[1])==lst[0]:
    return '1 minute' if t==1 else '{} minutes'.format(t)

