
def unique_lst(lst):
  return sorted(set(i for i in lst if i > 0), key=lst.index)

