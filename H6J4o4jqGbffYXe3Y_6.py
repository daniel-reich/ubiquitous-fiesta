
def relation_lst(lst):
  return sorted((a,b) for a in lst for b in lst if a<=b)

