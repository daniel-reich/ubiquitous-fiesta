
def invert_list(lst):
  lst2=[]
  if not len(lst): return []
  for i in lst:
    lst2.append(i * -1)
  return lst2

