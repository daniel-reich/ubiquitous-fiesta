
import collections as coll
def unique_lst(lst):
  return [l for i, l in enumerate(lst) if l > 0 and lst.index(l) == i]

