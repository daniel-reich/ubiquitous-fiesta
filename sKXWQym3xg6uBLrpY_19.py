
def find_median(lst):
  if len(lst) % 2 == 1:
    return lst[len(lst) // 2]
  else:
    return ((lst[len(lst) // 2 - 1]) + (lst[len(lst) // 2]))/2
    
def iqr(lst):
  lst.sort()
  m = len(lst) // 2
  f = lst[:m]
  if len(lst) % 2 == 1:
    s = lst[m+1:]
  else:
    s = lst[m:]
  return find_median(s) - find_median(f)

