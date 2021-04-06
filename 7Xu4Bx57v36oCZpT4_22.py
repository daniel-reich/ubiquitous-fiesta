
import itertools
def where_is_waldo(lst):
  flat_list = list(itertools.chain(*lst))
  unique_list = list(set(list(itertools.chain(*lst))))
  for x in unique_list:
    if flat_list.count(x) == 1:
        unique_element = x
  l2= []
  for idx, val in enumerate(lst):
    l1 = list(set(val))
    if len(l1) > 1:
      l2.append(idx+1)
      l2.append(val.index(unique_element)+1)
  return l2

