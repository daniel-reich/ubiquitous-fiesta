
from operator import itemgetter
def sort_authors(lst):
  temp = [" ".join(itm) for itm in sorted([itm.lower().split() for itm in lst], key=itemgetter(-1))]
  res = [temp.index(itm.lower()) for itm in lst]
  return [lst[i] for i in res]

