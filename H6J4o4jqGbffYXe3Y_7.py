
def relation_lst(lst):
  return sorted((y,x)for x in lst for y in lst if x >= y)

