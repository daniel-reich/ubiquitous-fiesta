
def accumulating_product(lst):
  if len(lst) == 0:
    return lst
  lst2 = []
  lst2.append(lst[0])
  for i in range(1, len(lst)):
    lst2.append(lst[i]*lst2[-1])
  return lst2

