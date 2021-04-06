
def combinator(lst, string = None):
  if len(lst) == 1:
    return lst[0]
  
  if string != None:
    tr = []
    
    if len(lst) == 2:
      a, b = lst
      
      if [] in [a, b]:
        return []
        
      for item in a:
        for itm in b:
          tr.append(item + string + itm)
    
    if len(lst) == 3:
      a, b, c = lst
      
      if [] in [a, b, c]:
        return []
      
      for item in a:
        for itm in b:
          for it in c:
            tr.append(string.join([item, itm, it]))
    
    return tr
  if len(lst) == 2:
    a, b = lst
    
    if a == [] or b == []:
      return []
    
    tr = []
    
    for item in a:
      for itm in b:
        tr.append(item + itm)
  
  if len(lst) == 3:
    a, b, c = lst
    
    if a == [] or b == []:
      return []
    
    tr = []
    
    for item in a:
      for itm in b:
        for it in c:
          tr.append(item + itm + it)
  
  return tr

