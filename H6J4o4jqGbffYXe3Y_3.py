
def relation_lst(lst):
  return sorted([(x,y) for x in lst for y in lst if x <= y])

