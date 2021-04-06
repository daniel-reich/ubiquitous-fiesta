
def relation_lst(lst):
  lst = sorted(lst)
  lst2 = []
  for i in lst:
    for j in lst:
      if j>=i:
        lst2.append((i,j))
  return lst2

