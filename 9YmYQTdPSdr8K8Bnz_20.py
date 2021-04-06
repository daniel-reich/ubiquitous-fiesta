
def unique_lst(lst):
  return sorted(set(filter(lambda x: x>0,lst)), key=lst.index)

