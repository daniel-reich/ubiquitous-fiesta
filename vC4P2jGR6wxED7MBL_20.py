
def larger_than_right(lst):
  res = []
  last = False
  
  check = sorted(lst)
  if check[0] == check[len(check)-1]:
    return [check[0]]
  
  while len(lst) > 1:
    val = max(lst)
    res.append(val)
    
    if lst.index(val)+1 >= len(lst):
      last = True
      break
  
    lst = lst[lst.index(val)+1:]
  
  
  if not last:
    res.append(lst[0])
    
  
  
  return res

