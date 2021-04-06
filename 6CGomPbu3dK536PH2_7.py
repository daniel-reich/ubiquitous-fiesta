
def accumulating_list(lst):
  if len(lst) == 0:
    return []
  for i in range(1,len(lst)):
    lst[i] += lst[i-1]
  return lst

