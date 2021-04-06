
def relation_lst(lst):
  lst.sort()
  return [(e, lst[i]) for e in lst for i in range(len(lst)) if e<=lst[i]]

