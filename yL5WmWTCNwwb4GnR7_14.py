
def return_unique(lst):
  
  Unique = []
  
  for x in lst:
    if (lst.count(x) == 1):
      Unique.append(x)
    
  return Unique

