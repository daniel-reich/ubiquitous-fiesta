
def relation_lst(lst):
  lst = sorted(lst)
  return [(i, j) for i in lst for j in lst if i <= j]

