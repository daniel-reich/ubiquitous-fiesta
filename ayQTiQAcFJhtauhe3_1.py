
def even_or_odd(lst):
  
  Total = 0
  
  for x in lst:
    Total += x
    
  if (Total % 2 == 0):
    return "even"
  else:
    return "odd"

