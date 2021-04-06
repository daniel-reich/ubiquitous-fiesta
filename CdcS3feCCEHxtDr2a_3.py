
def clear_ordering(lst):
  order = {}
  
  for l in lst:
    first = l[0]
    second = l[1]
    
    order[second] = True
    if not first in order.keys():
      order[first] = False
    else:
      if order[first] == False:
        return False
  
  count = 0
  
  for key in order.keys():
    if order[key] == False:
      count += 1
  
  if count > 1:
    return False
  else:
    return True

