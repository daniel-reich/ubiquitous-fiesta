
def less_or_equal(lst, k):
  
  lst = sorted(lst)
  
  tcheck = lst[k-1]
  
  return tcheck if lst[k:].count(tcheck) == 0 else None if k != 0 else 1 if lst != [1] else None

