
def relation_lst(lst):
  return sorted(list((y,x)for x in lst for y in lst if x>=y))

