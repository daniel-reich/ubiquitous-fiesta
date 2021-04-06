
def unique_lst(lst):
  return sorted(set(x for x in lst if x>0), key=lst.index)

