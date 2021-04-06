
def relation_lst(lst):
  lst.sort()
  return [(x,y) for x in lst for y in lst if x<=y]

