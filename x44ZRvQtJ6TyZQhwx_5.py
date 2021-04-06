
def is_pandigital(n):
  lst = []
  
  for i in str(n):
    if not i in lst:
      lst.append(i)
  
  if len(lst) == 10:
    return True
    
  return False

