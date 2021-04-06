
def valid_name(name):
  
  valid = True
​
  lst = name.split()
  
  if len(lst) != 2 and len(lst) != 3:
    valid = False
    return valid
  
  if len(lst[-1]) == 2:
    valid = False
    return valid
  
  if len(lst) == 3:
    
    if len(lst[0]) == 2 and len(lst[1]) > 2:
      valid = False
      return valid
  
  for n in lst:
    
    if n[0].islower():
      valid = False
      return valid
    
    elif len(n) == 1:
      valid = False
      return valid
    
    if len(n) > 2 and n[-1] == '.':
      valid = False
      return valid
    
  return True

