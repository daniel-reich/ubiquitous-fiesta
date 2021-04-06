
def sort_array(lst):
  lst2 = []
  for x in range(min(lst) - 1,max(lst) + 1):
    if x in lst:
      lst2.append(x)
  return lst2

